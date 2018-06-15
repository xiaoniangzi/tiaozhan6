from flask import Flask, render_template, abort
import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

path= '/home/shiyanlou/files/'
@app.route('/')
def index():
    course = {}
    n = 1
    filenames = os.listdir(path)
    for filename in filenames:
        filepath = path + filename
        with open (filepath,'r') as file:
            naiyou = json.loads(file.read())
            course[n] = naiyou.pop('title')
            n+=1
    print(course)
    return render_template('index.html',course=course)

@app.route('/files/<filename>')
def file(filename):
    if os.path.exists(path +filename +'.json'):
        with open (path + filename + '.json', 'r') as file:
            naiyou = json.loads(file.read())
        return render_template('file.html',naiyou=naiyou)
    else:
        abort(404)

@app.errorhandler(404)
def haha(error):
    return render_template('404.html'), 404

