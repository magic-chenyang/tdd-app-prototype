# tdd-app-prototype
Prototype one of the views. It uses docker-py with flask. It uses docker-py API with the latest version.
```
{'PythonVersion': '3.5', 'ApiVersion': '1.32', 'GoVersion': 'go1.8.3', 'DockerVersion': '17.09.0-ce', 'MinAPIVersion': '1.12', 'Os': 'linux', 'GitCommit': 'afdb6d4', 'KernelVersion': '4.10.0-35-generic', 'Arch': 'amd64'}
```
First install requirements:
```
pip install -r requirements.txt
```
Then fire up flask application:
```
python docker_view.py
```
Right after go to `0.0.0.0:5000` and there write code that you want to be
executed inside docker container.

