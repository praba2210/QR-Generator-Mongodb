from flask import Flask, render_template, session, url_for, request, redirect
import pymongo
import pyqrcode
import qrtools
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
QRdb = client["QRGen"] 
students = client.QRGen.students

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def qrgen():
    name = request.form['name']
    college = request.form['college']
    dept = request.form['dept']
    year = request.form['year']
    ph = request.form['no']
    email = request.form['email']
    students.insert({"name":name, "College":college, "Department":dept,"Year":year,"Phone":ph,"Email":email})
    qr = pyqrcode.create(name+","+college+","+dept+","+year+","+ph+","+email) 
    qr.png(file="qrimg.png", scale=6) 
    return render_template('payment.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)