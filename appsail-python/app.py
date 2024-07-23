import sys
sys.path.insert(0, '.venv/lib/python3.9/site-packages')


import os
from flask import Flask, render_template,request, send_from_directory
from main.catalyst import CheckUser
from main.newgraph import NewGraph

app = Flask(__name__)



@app.route("/")
def load_login_html():
    return render_template("login.html")

@app.route("/sales")
def load_sales_html():
    return render_template("sales.html")

@app.route("/api/login",methods=["POST"])
def login():
   user = CheckUser()
   result = user.get_user(request)
   if not result:
       return {
           "status":"failure",
           "message":"Invalid username or password"
       }, 400
   else:
       return {
           "status":"success",
           "data":{
               "status":True
           }
       }, 200

@app.route("/api/generate_report", methods=["POST"])
def gennew_report():
    csv_file = request.files["csv_file"]
    newgraph = NewGraph()
    output_data = newgraph.generate_graph(csv_file)
    return render_template("report.html", data = output_data)

if __name__ == '__main__':
    listen_port = os.getenv('X_ZOHO_CATALYST_LISTEN_PORT')
    app.run(host='0.0.0.0', port = listen_port)