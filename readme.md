## Flask, Pandas and plots project.

### Install venv environment.

```bash
$ sudo apt update
$ sudo apt install python3-venv -y
$ python3 -m venv .venv
$ (venv) source .venv/bin/activate
$ (venv) pip install -r requirements.txt
```

### Run project 

Start the web app in reload mode:

```bash
$ flask run --reload -h 0.0.0.0
* Environment: production
...
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open a terminal and get IP addr:

$ ip --brief addr
Fire up a web browser and navigate to http://<ip>:5000