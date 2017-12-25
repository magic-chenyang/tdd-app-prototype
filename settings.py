#from docker import Client
import docker
from flask import Flask
from flask.ext.codemirror import CodeMirror

cli = docker.from_env()
SECRET_KEY = 'secret!'
# mandatory
CODEMIRROR_LANGUAGES = ['python', 'html']
app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)
