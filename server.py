from flask import Flask, render_template, redirect, request, session, flash

app=Flask(__name__)
app.secret_key='thisisasecret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():

    return render_template('index.html')

@app.route('/ninja/<color>', methods = ['GET'])
def ninja_color(color):
    return render_template('ninja.html',color =color)

    

app.run(debug=True)
