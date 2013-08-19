# coding: utf8
import sys
import os

from flask import Flask
from flask import render_template
from flask import request
import santnewdata
from datetime import timedelta
from datetime import datetime
from flask import abort, redirect, url_for,flash
from flask import  make_response, Response
from datetime import date
import datetime
from jinja2 import Environment
import jinja2
import MySQLdb
app = Flask(__name__)
app.secret_key ='some_secret'
    
@app.route('/')
def  home():
    items=santnewdata.ind()
    return render_template('default.html',item=items)

@app.route("/home/<name>")
def  foodretail(name=None):
      meno_ind_item=santnewdata.ind()
      meni_method_item=santnewdata.menoInditem(name)
      sub_item=santnewdata.solotionn_name(name)
      return render_template('foodretailpY.html',indItem=meno_ind_item,methoitem=meni_method_item,submeno=sub_item)

@app.route("/home/<name>/<method>")
def  method(name=None,method=None):
      meno_ind_item=santnewdata.ind()
      meni_method_item=santnewdata.menoInditem(name)
      sub_item=santnewdata.solotionn_name(name)
      methodtext=santnewdata.solotion_text(method)
      return render_template('foodretailpM.html',indItem=meno_ind_item,methoitem=meni_method_item,submeno=sub_item,method=methodtext)


@app.route('/prodact')
def prodactlist():
  items=santnewdata.ind()
  prodactlist=santnewdata.prodacts()
  return render_template('prodactlist.html',indItem=items,allprodact=prodactlist)

@app.route('/prodact/<category>')
def prodactlistA(category=None):
  items=santnewdata.ind()
  prodactlist=santnewdata.pro_category(category)
  return render_template('prodactlistD.html',indItem=items,allprodact=prodactlist,cate=category)
@app.route('/prodact/<category>/<name>')
def page(name=None,category=None):
    prodactfle=name
    return render_template('prodactform.html',file=prodactfle,title=name)
@app.route('/contactus')
def contactus():
  return render_template('contact.html')
@app.route('/litformsumite', methods = ['POST' , 'GET'] )
def litformsumite():
  method1=request.form['method']
  category=request.form['ind']
  Name=request.form['name']
  email=request.form['email']
  mobile=request.form['mobile']
  ostan=request.form['ostan']
  sub=request.form['subject']
  text=request.form['masage']
  direct=request.form['direct']
  if Name =='':
    flash('لطفا نام و نام خانوادگی خود را وارد نمائیید')
    return redirect("/home/%s/%s"%(category,method1))

  if mobile =='':
    flash('لطفا شماره تلفن همراه خود  را وارد نمائیید')
    return redirect("/home/%s/%s"%(category,method1))

  
  query="INSERT INTO litform (Name,email,mobile,ostan,sub,text,direct) VALUES ('%s','%s','%s','%s','%s','%s','%s')" %(Name,email,mobile,ostan,sub,text,direct)
  conn=santnewdata.conection()
  nevesht=conn.cursor()
  nevesht.execute(query)
  rows=nevesht.fetchall()
  conn.commit()
  nevesht.close()
  conn.close()
  flash('اطلاعات و متن پیام شما ارصال گردید بسیار سپاسزگزاریم')
  return redirect("/home/%s/%s"%(category,method1))
  
  
  
  


  


