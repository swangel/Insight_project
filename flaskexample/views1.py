from flask import render_template
from flaskexample import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from flask import request

# Python code to connect to Postgres
# You may need to modify this based on your OS, 
# as detailed in the postgres dev setup materials.
user = 'anqi' #add your Postgres username here      
host = 'localhost'
dbname = 'birth_db'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

@app.route('/')
@app.route('/index')

def view_method():
#     with open('flaskexample/question', 'rb') as inusrfile:
    aotable = pd.read_csv("flaskexample/question.csv")

    dropdown_list = sorted(list(aotable['title']))
    return render_template('index.html', title='Home', dropdown_list=dropdown_list)




# @app.route('/db')
# def birth_page():
#     sql_query = """                                                             
#                 SELECT * FROM birth_data_table WHERE delivery_method='Cesarean'\
# ;                                                                               
#                 """
#     query_results = pd.read_sql_query(sql_query,con)
#     births = ""
#     print(query_results[:10])
#     for i in range(0,10):
#         births += query_results.iloc[i]['birth_month']
#         births += "<br>"
#     return births
# 
# @app.route('/db_fancy')
# def cesareans_page_fancy():
#     sql_query = """
#                SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean';
#                 """
#     query_results=pd.read_sql_query(sql_query,con)
#     births = []
#     for i in range(0,query_results.shape[0]):
#         births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
#     return render_template('cesareans.html',births=births)
# 
# @app.route('/input')
# def cesareans_input():
#     return render_template("input.html")


@app.route('/output', methods=['GET', 'POST'])
def output():
  #pull 'birth_month' from input field and store it
  topic = request.args.get('inputform')
  question = pd.read_csv("flaskexample/question.csv")

#   result= question[question['title']==topic]
  result= topic

    #just select the Cesareans  from the birth dtabase for the month that the user inputs
#   query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
#   print(query)
#   query_results=pd.read_sql_query(query,con)
#   print(query_results)
#   births = []
#   for i in range(0,query_results.shape[0]):
#       births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
#       the_result = ''

  return render_template("output.html", result = result)
