from datetime import datetime
from flask import Flask, render_template,request
from . import app

@app.route("/") 
def index():
    return '<a href="/calc">calc</a>'

@app.route("/calc", methods=['GET'] )
def calc_get():
    return '''<form method="POST" action="/calc">
        <input name="a">
        <br>
        <input name="b">
        <br>
        <label for="cars">Choose a operation</label>
        <br>
        <select name="operations" id="operations">
          <option value="addition">Addition</option>
          <option value="subtraction">Subtraction</option>
          <option value="multiplication">Multiplication</option>
          <option value="division">Division</option>
        </select>
        <input type="submit" value="Compute">
        </form>'''


@app.route("/calc", methods=['POST'] )
def calc_post():
    a = request.form.get('a', '0')
    b = request.form.get('b', '0')
    c = request.form.get('operations')
    
    if c == 'addition':
     result = float(a) + float(b)
    elif c == 'subtraction':
     result = float(a) - float(b)
    elif c == 'multiplication':
     result = float(a) * float(b)
    elif c == 'multiplication':
     result = float(a) / float(b)
    return '<h2>' & str(result) & '</h2>'

