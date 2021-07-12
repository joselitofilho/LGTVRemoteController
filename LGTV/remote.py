from ws4py.client.threadedclient import WebSocketClient
from types import FunctionType
from wakeonlan import send_magic_packet
import socket
import requests
import base64
import json
import os
import logging

from .payload import register_data


class LGTVRemote(WebSocketClient):
    __slots__ = ()

    @classmethod
    def getCommands(cls):
        excludes = [
            'opened',
            'closed',
            'received_message',
            'exec_command',
            'getCommands'
        ]
        out = []
        m = [x for x, y in cls.__dict__.items() if type(y) == FunctionType]
        for method in m:
            if method.startswith("_" + cls.__name__):
                continue
            if method in excludes:
                continue
            if method.startswith("__"):
                continue
            out.append(method)
        out.sort()
        return out

    def __init__(self, name, ip=None, mac=None, key=None, hostname=None):
        self.__command_count = 0
        self.__waiting_callback = None
        self.__commands = []
        self.__handshake_done = False

        self.__hostname = hostname
        self.__clientKey = key
        self.__macAddress = mac
        self.__ip = ip
        self.__name = name

        if self.__hostname is not None:
            # Over ride IP address when we know the hostname
            self.__ip = socket.gethostbyname(self.__hostname)

        super(LGTVRemote, self).__init__('ws://' + self.__ip + ':3000/', exclude_headers=["Origin"])

    def execute(self, command, args):
        self.__commands.append({command: args})
        if self.__handshake_done is True:
            self.__execute()

    def serialise(self):
        return {
            self.__name: {
                "key": self.__clientKey,
                "mac": self.__macAddress,
                "ip": self.__ip,
                "hostname": self.__hostname
            }
        }

    ################################################################################
    # WebSocketClient subclass
    ################################################################################

    def opened(self):
        if self.__clientKey is None:
            raise Exception("Client is not authenticated")

        logging.debug("Initiating handshake")
        register_data['payload']['client-key'] = self.__clientKey
        self.__waiting_callback = self.__handshake
        self.send(json.dumps(register_data))

    def closed(self, code, reason: str = ''):
        if type(reason) == bytes:
            reason = reason.decode('utf-8')
        print (json.dumps({
            "closing": {
                "code": code,
                "reason": str(reason)
            }
        }))

    def received_message(self, response):
        logging.debug("Received response")
        logging.debug(response)
        if self.__waiting_callback:
            self.__waiting_callback(json.loads(str(response)))

    ################################################################################
    # Internal command handling
    ################################################################################

    def __handshake(self, response):
        if 'client-key' in response['payload'].keys():
            logging.debug("Handshake complete")
            self.__handshake_done = True
            self.__execute()

    def __execute(self):
        if self.__handshake_done is False:
            print ("Error: Handshake failed")

        while len(self.__commands) > 0:
            command = self.__commands.pop(0)
            method = list(command.keys())[0]
            args = command[method]
            self.__class__.__dict__[method](self, **args)
        # TODO: Available this.
        # self.__waitClose()

    def __waitClose(self):
        self._th.join(timeout=1)
        self.close()

    def __defaultHandler(self, response):
        logging.debug(response)
        # {"type":"response","id":"0","payload":{"returnValue":true}}
        if response['type'] == "error":
            print (json.dumps(response))
            self.close()
        if "returnValue" in response["payload"] and response["payload"]["returnValue"] is True:
            print (json.dumps(response))
            self.close()
        else:
            print (json.dumps(response))

    def __send_command(self, msgtype, uri, payload=None, callback=None, prefix=None):
        if not callback:
            callback = self.__defaultHandler
        self.__waiting_callback = callback
        if prefix is None:
            messageid = str(self.__command_count)
        else:
            messageid = prefix + '_' + str(self.__command_count)

        message_data = {
            'id': messageid,
            'type': msgtype,
            'uri': uri
        }
        if type(payload) == dict:
            payload = json.dumps(payload)

        if type(payload) == str and len(payload) > 2:
            message_data['payload'] = payload

        self.__command_count += 1
        logging.debug(message_data)
        self.send(json.dumps(message_data))

    ################################################################################
    # Supported commands
    ################################################################################

    def openBrowserAt(self, url, callback=None):
        self.__send_command("request", "ssap://system.launcher/open", {"target": url}, callback)
