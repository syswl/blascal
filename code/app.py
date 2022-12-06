from flask import Flask
from flask import request
from flask import send_from_directory
import itertools, random, re, ast
import os

app = Flask(__name__)


class Blascal():
    def __init__(self, condition='1'):

    def insert(self):

    def properties(self):
        return '<br><br>'.join(self.response)

    def example(self):
        return self.properties()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET', 'POST'])
def index():
    a = request.args.get('relation', '')
    notEdge = True if a or b or c or d else ''
    if notEdge:
        notEdge = ''
        try:
            a = ast.literal_eval(a)
        except:
            a = None
        f = request.args.get('feedback', '')
    return (
            '''
            <!DOCTYPE html>

            <head>
            <meta charset="utf-8"/>
            <meta name="viewport" content="width=device-width, user-scalable=yes"/>
            <link rel="icon" href="/favicon.ico" type="image/x-icon">
            <link href="http://fonts.googleapis.com/css?family=Open%20Sans" rel="stylesheet" type="text/css">
            <style>
            body{font-family:'Open Sans'; padding: 0 0 1em 0}
     
        </div>
        '''
    )


if __name__ == "__main__":
    app.run()
