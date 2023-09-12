from flask import Flask
from flask import request
from flask import render_template
import random

correct = random.randint(1,100)
count=0
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    global correct
    global count
    msg = ''
    print(count)
    if count<7:
        count+=1
        text1 = request.form['text1']
        text1 = int(text1)

        if text1 < correct:
            msg = 'Your number is too low'
            return render_template("index.html", msg=msg)
        elif text1 > correct:
            msg = 'Your number is too high'
            return render_template("index.html", msg=msg)
        else:
            if text1 == correct:
                msg = 'Good work! You got the number in '+ str(count)+ ' guesses'
                count = 0
                correct = random.randint(1,100)
                return render_template("index.html", msg=msg)
    else:
        num = 'Nope. The number I was thinking of was ' + str(correct)
        correct = random.randint(1,20)
        msg = ''
        count=0
        return render_template("index.html", num=num)

if __name__ == '__main__':
    app.run()