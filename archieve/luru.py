# -*- coding=UTF-8 -*-
import globalvars
import mysql.connector

def get():
  template = globalvars.jinja_env.get_template('template/luru.html')
  return template.render()

def post():
  template = globalvars.jinja_env.get_template('template/luru.html')
  return template.render()