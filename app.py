# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# from crypt import methods
from distutils.log import debug
from services.pbiembedservice import PbiEmbedService
from utils import Utils
from flask import Flask, render_template, send_from_directory , request,session,redirect,url_for,g,flash
import json
import os

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = '123'

# Load configuration
app.config.from_object('config.BaseConfig')

class User:
    def __init__(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password

users=[]
users.append(User(id=1,username='admin',password='admin'))



@app.route('/',methods = ['POST','GET'])
def login():
    '''Returns a static HTML page'''
    if request.method=='POST':
        uname=request.form['username']
        upass = request.form['password']
        for data in users:
            if data.username==uname and data.password==upass:
                session['userid']=data.id
                g.record=1
                return redirect(url_for('index'))
            else:
                g.record=0
        if g.record!=1:
            flash("Username or Password Mismatch...!!!",'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.before_request
def before_request():
    if 'userid' in session:
        for data in users:
            if data.id==session['userid']:
                g.user=data


@app.route('/index')
def index():
    '''Returns a static HTML page'''
    if not g.user:
        return redirect(url_for('login'))

    return render_template('index.html')

@app.route('/getembedinfo', methods=['GET'])
def get_embed_info():
    '''Returns report embed configuration'''

    config_result = Utils.check_config(app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500

    try:
        embed_info = PbiEmbedService().get_embed_params_for_single_report(app.config['WORKSPACE_ID'], app.config['REPORT_ID'])
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500

@app.route('/favicon.ico', methods=['GET'])
def getfavicon():
    '''Returns path of the favicon to be rendered'''

    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)