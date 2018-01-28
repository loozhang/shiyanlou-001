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
def
