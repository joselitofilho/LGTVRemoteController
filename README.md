# LGTVRemoteController
LGTV WebOS Remote Controller.

## Available Commands

```bash
$ lgtv scan
$ lgtv auth <host> NameTV
$ lgtv NameTV openBrowserAt <url>
```

## Getting started
### Setup

// TODO

### Install

Windows:
```bash
$ python -m venv venv
$ ./venv/Scripts/activate
(venv) $ pip install git+https://github.com/joselitofilho/LGTVRemoteController
```

Linux or MacOS:
```bash
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install git+https://github.com/joselitofilho/LGTVRemoteController
```

### Run

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

## Usage

// TODO