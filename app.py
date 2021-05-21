from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Srqq98aa@localhost/debinco'
else:
    app.debug = False
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://ohtejgtdgvlmwd:15013d2fb0ec2513023518d5b87e495eebe6bb8ced597980e789892849129e3f@ec2-3-223-72-172.compute-1.amazonaws.com:5432/davopa4qfajuas'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#
# class Feedback(db.Model):
#     __tablename__ = 'feedback'
#     id = db.Column(db.Integer, primary_key=True)
#     Name = db.Column(db.String(200), unique=True)
#     Phone_Number = db.Column(db.String(20))
#     Email = db.Column(db.String(200))
#     rating = db.Column(db.Integer)
#     comments = db.Column(db.Text())
#
#     def __init__(self, Name, Phone_Number , Email, rating, comments):
#         self.Name = Name
#         self.Phone_Number = Phone_Number
#         self.Email = Email
#         self.rating = rating
#         self.comments = comments
#

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        Name = request.form['Name']
        Phone_Number = request.form['Phone_Number']
        Email = request.form['Email']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer,dealer,rating,comments)
        # print(customer,dealer,rating,comments)
        if Name == '' or Phone_Number == '':
            return render_template('index.html', message="Please enter required feilds")
        else:
            send_mail(Name, Phone_Number, Email, rating, comments)
            return render_template('success.html')

        return render_template('index.html', message="You have already Submitted")


if __name__ == '__main__':
    app.run()
