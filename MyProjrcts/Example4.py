#App routing
#a function connected to an app

import flask
from flask import Flask

app = Flask(__name__)



@app.route('/')
def page():
    return "Hello Dear Mohammed Shaheen KP"


@app.route('/contact')
def home1():
    return "Hello Dear Mohammed Shaheen KP THIS IS contact"


@app.route('/about')
def about1():
    return "Hello Dear Mohammed Shaheen KP this is ABOUT "
app.add_url_rule("/Home","home",page)

if __name__ == "__main__":
    app.run(debug=True)
