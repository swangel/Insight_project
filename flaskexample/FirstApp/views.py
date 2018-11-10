from flask import render_template
from flaskexample import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from flask import request


@app.route('/')
@app.route('/index')

def view_method():
#     with open('flaskexample/question', 'rb') as inusrfile:
    aotable = pd.read_csv("flaskexample/question.csv")
    dropdown_list = sorted(list(aotable['title']))
    return render_template('index.html', title='Home', dropdown_list=dropdown_list)



@app.route('/output', methods=['GET', 'POST'])
# @app.route('/output',methods=['GET'])
def output():
  topic = request.form.get('inputform')
  question = pd.read_csv("flaskexample/question.csv")
#   result=question.loc[question['title'] == topic].values.tolist()
#   result=result[1]
#   result= question[(question['title']==topic)]
#   result= topic
#   print(topic)
  question=question.loc[question['title'] == 'Array']
  trans_ques=question.loc[:, ['Q1','Q2', 'Q3']].transpose()
  trans_ques.columns=['Questions']
  result=trans_ques
  return render_template("output.html", result = result)
