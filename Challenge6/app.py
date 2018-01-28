#!/usr/bin/env python3
#-*-coding:utf-8-*-
from flask import Flask,render_template
import json
import os

app=flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

@app.route('/')
def index():
	filelist=os.listdir('../files/')
	return render_template('index.html',filelist=filelist)

@app.route('/files/<filename>')
def file(filename):
	if filename=='helloshiyanlou':
		with open('../files/helloshiyanlou.json','r') as file:
			shiyanlou=json.loads(file.read())
		return render_template('file.html',shiyanlou=shiyanlou)
	elif filename=='helloworld':
		with open('../files/helloworld.json','r') as file:
			shiyanlou=json.loads(file.read())
		return render_template('file.html',shiyanlou=shiyanlou)
	else:
		return render_template('404.html'),404

if __name__=='__main__':
	app.run()	
