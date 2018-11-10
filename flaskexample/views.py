from flask import render_template
from flaskexample import app
# from sqlalchemy import create_engine
# from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from flask import request


@app.route('/')
@app.route('/index')

def view_method():
#     with open('flaskexample/question', 'rb') as inusrfile:
    aotable = pd.read_csv("flaskexample/companies.csv")
    dropdown_list = list(aotable['title'])
#         dropdown_list = sorted(list(aotable['title']))
    return render_template('index.html', title='Home', dropdown_list=dropdown_list)
    
    

@app.route('/topics', methods=['GET', 'POST'])
def topics():
  aotable = pd.read_csv("flaskexample/question.csv")
  dropdown_list = list(aotable['title'])
  # dropdown_list = sorted(list(aotable['title']))

  company_name = request.form.get('inputform')
  all_topics = pd.read_csv("flaskexample/companies.csv")

  topics=all_topics.loc[all_topics['title'] == company_name]
  trans_top=topics.loc[:, ['Topic1','Topic2', 'Topic3','Topic4','Topic5', 'Topic6','Topic7', 'Topic8']].transpose()
  trans_top.columns=['Topics']
  result=trans_top
  return render_template("topics.html", result = result, dropdown_list=dropdown_list)
  

@app.route('/questions', methods=['GET', 'POST'])
def questions():
#   aotable = pd.read_csv("flaskexample/question.csv")
#   dropdown_list = sorted(list(aotable['title']))
  topic = request.form.get('inputform')
  question = pd.read_csv("flaskexample/question.csv")
  question=question.loc[question['title'] == topic]
  trans_ques=question.loc[:, ['Q1','Q2', 'Q3','Q4', 'Q5']].transpose()
  trans_ques.columns=['Questions']
  result=trans_ques
  return render_template("questions.html", result = result)
# 
# 
# @app.route('/output', methods=['GET', 'POST'])
# def output():
#   topic = request.form.get('inputform')
#   question = pd.read_csv("flaskexample/question.csv")
#   question=question.loc[question['title'] == 'Array']
#   trans_ques=question.loc[:, ['Q1','Q2', 'Q3']].transpose()
#   trans_ques.columns=['Questions']
#   result=trans_ques
#   return render_template("output.html", result = result)