# LGTVRemoteController
LGTV WebOS Remote Controller.

## Available Commands

```bash
$ lgtv scan
$ lgtv auth <host> NameTV
$ lgtv NameTV openBrowserAt <url>
$ lgtv NameTV audioStatus
$ lgtv NameTV audioVolume
$ lgtv NameTV closeApp <appid>
$ lgtv NameTV execute <command>
$ lgtv NameTV getCursorSocket
$ lgtv NameTV getForegroundAppInfo
$ lgtv NameTV getPictureSettings
$ lgtv NameTV getPowerState
$ lgtv NameTV getSoundOutput
$ lgtv NameTV getSystemInfo
$ lgtv NameTV getTVChannel
$ lgtv NameTV input3DOff
$ lgtv NameTV input3DOn
$ lgtv NameTV inputChannelDown
$ lgtv NameTV inputChannelUp
$ lgtv NameTV inputMediaFastForward
$ lgtv NameTV inputMediaPause
$ lgtv NameTV inputMediaPlay
$ lgtv NameTV inputMediaRewind
$ lgtv NameTV inputMediaStop
$ lgtv NameTV listApps
$ lgtv NameTV listLaunchPoints
$ lgtv NameTV listChannels
$ lgtv NameTV listInputs
$ lgtv NameTV listServices
$ lgtv NameTV mute <true|false>
$ lgtv NameTV notification <message>
$ lgtv NameTV notificationWithIcon <message> <url>
$ lgtv NameTV off
$ lgtv NameTV on
$ lgtv NameTV openAppWithPayload <payload>
$ lgtv NameTV openBrowserAt <url>
$ lgtv NameTV openYoutubeId <videoid>
$ lgtv NameTV openYoutubeURL <url>
$ lgtv NameTV serialise
$ lgtv NameTV setInput <input_id>
$ lgtv NameTV setSoundOutput <tv_speaker|external_optical|external_arc|external_speaker|lineout|$ headphone|tv_external_speaker|tv_speaker_headphone|bt_soundbar>
$ lgtv NameTV screenOff
$ lgtv NameTV screenOn
$ lgtv NameTV setTVChannel <channelId>
$ lgtv NameTV setVolume <level>
$ lgtv NameTV startApp <appid>
$ lgtv NameTV swInfo
$ lgtv NameTV volumeDown
$ lgtv NameTV volumeUp
```

## Getting started

### Setup

```bash
$ python -m venv venv
```

Windows:
```bash
$ ./venv/Scripts/activate
```

Linux or MacOS:
```bash
$ source venv/bin/activate
```

```bash
(venv) $ pip install git+https://github.com/joselitofilho/LGTVRemoteController
```

### Usage

**IMPORTANT**: Make sure your computer is on the same network connection as your TV.

Turn on your TV;

Search for LGTVs:
```bash
(venv) $ lgtv scan
```

Output:
```JSON
{
    "result": "ok", 
    "count": 1, 
    "list": [
        {
            "uuid": "00000000-0a17-d6ce-fa2f-0009d67a0937",
            "model": "Name",
            "address": "192.168.0.10"
        }
    ]
}
```

Authenticate you LGTV:
```bash
(venv) $ lgtv auth 192.168.0.10 NameTV
```

Output:
```bash
DEBUG:getmac:Raw MAC found: XX-XX-XX-XX-XX-XX
Please accept the pairing request on your LG TV
```

Enjoy!