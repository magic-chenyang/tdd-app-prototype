import io
import os

from flask import Flask, render_template, request

from forms import MyForm
from settings import app, cli


@app.route("/", methods=['GET'])
def index_page():
    form = MyForm()
    return render_template('index.html', form=form)


@app.route("/send_code", methods=['POST'])
def execute_code():
    data = request.form['source_code']
    code = io.StringIO(data)
    create_container(code)
    output = create_container(code)
    return output


def create_container(code):
    py_container = cli.containers.run(
         image='python:3',
         command=['python','-c', code.getvalue()],
         volumes={ os.getcwd(): {
                 'bind': '/opt',
                 'mode': 'rw',
                 }
             },
         name='hello_word_from_docker',
         working_dir='/opt'
    )

    for py_container in cli.containers.list(filters={'status':'exited'}): 
          with open('/opt/py_log.txt', 'a') as f:
                  f.write(str(py_container.logs()))

    output = py_container.logs()
    py_container.remove()

    return "From docker: {}".format(output.strip())

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
