from flask import Flask, render_template,request
app = Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('Project.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods = ['POST'])

def login():
    a = request.form["accommodation"]
    b = request.form["arrival_month"]
    c = request.form["arrival_year"]
    d = request.form["arrival_date"]
    e = request.form["meal_option"]
    f = request.form["deposit_type"]
    g = request.form["booking_type"]
    h = request.form["week_night_stay"]
    i = request.form["weekend_night_stay"]
    j = request.form["adults"]
    k = request.form["children"]
    l = request.form["babies"]
    m = request.form["repeated_guest"]
    n = request.form["parking_spaces"]
    o = request.form["special_requests"]
    
    t= [[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h),float(i),float(j),float(k),float(l),float(m),float(n),float(o)]]
    prediction = model.predict(t)
    print(prediction[0])
    
    if (prediction[0] == 0):
        output = "No waiting period for given booking"
    elif (prediction[0] == 1):
        output = "Waiting period upto a week"
    elif (prediction[0] == 2):
        output = "Waiting period upto a month"
    elif (prediction[0] == 3):
        output = "Waiting period of more than a month"
    return render_template("index.html",y = ""+output)

if __name__=='__main__' :
    app.run()