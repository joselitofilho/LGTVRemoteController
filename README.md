# LGTVRemoteController
> LGTV WebOS Remote Controller.

**Table of contents**

- [Available commands](#available-commands)
- [Getting started](#getting-started)
  - [Setup](#setup)
  - [Usage](#usage)
- [License](#license)

## Available commands

```bash
$ lgtv scan
$ lgtv auth <host> NameTV
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

[Install python 3.9](https://www.python.org/downloads/)
![image](https://user-images.githubusercontent.com/1102589/125335354-d660e680-e322-11eb-834b-435cc36ce013.png)

Install virtualenv using pip:
```bash
pip install virtualenv
```

Create a virtual environment:
```bash
$ python -m venv venv
```

Active your virtual environment - Windows:
```bash
$ ./venv/Scripts/activate
```

Active your virtual environment - Linux or MacOS:
```bash
$ source venv/bin/activate
```

Install LGTV Remote Controller App
```bash
(venv) $ pip install git+https://github.com/joselitofilho/LGTVRemoteController
```

### Usage

**IMPORTANT**: Make sure your computer is on the same network connection as your TV.

Turn on your TV;

Search for LG TVs:
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

Authenticate your LG TV:
```bash
(venv) $ lgtv auth 192.168.0.10 NameTV
```

Output:
```bash
DEBUG:getmac:Raw MAC found: XX-XX-XX-XX-XX-XX
Please accept the pairing request on your LG TV
```

Open a URL in your LG TV:
```bash
(venv) $ lgtv NameTV openBrowserAt https://github.com/
```

Enjoy!

## License

[MIT](LICENSE "License")
