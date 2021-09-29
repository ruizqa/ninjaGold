from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret"


@app.route( "/", methods=['GET'] )
def display():
    if not 'gold' in session:
        session['gold'] = 0
    
    return render_template("index.html")

@app.route( "/process_money", methods=['POST'] )
def process():
    # result = {
    #     'farm': random.randint(10,20)
    #     'cave': random.randint(5,10)
    #     'house': random.randint(2,5)
    #     'casino': random.randint(1,200) -100
    # }
    now = datetime.now()
    if not 'gold' in session:
        return redirect("/")
    elif not 'log' in session:
        session['log'] = " "
    if request.form['which'] == "farm":
        bonus = random.randint(10,20)
        session['gold'] += bonus
    elif request.form['which'] == "cave":
        bonus = random.randint(5,10)
        session['gold'] += bonus
    elif request.form['which'] == "house":
        bonus = random.randint(2,5)
        session['gold'] += bonus
    elif request.form['which'] == "casino":
        bonus = random.randint(1,200) -100
        session['gold'] +=  bonus
    if bonus>0:
        session['log'] += f"<p class='text-success'>Earned {bonus} golds from the {request.form['which']}! ({ now.strftime('%Y/%m/%d %I:%M %p')})</p>"
    elif bonus<0:
        session['log'] += f"<p class='text-danger'> Entered a casino and lost { abs(bonus) } golds... Ouch!  ({ now.strftime('%Y/%m/%d %I:%M %p')})</p>"
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)