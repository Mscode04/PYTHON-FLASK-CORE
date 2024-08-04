# clint to server

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')
@app.route('/')
def index():
    return render_template('new1.html')
@app.route("/register",methods=["GET"])  #we can use post methon insted of get post not store any history and cant change 
def form():
    name=request.args.get("names")
    num=request.args.get("number")
    mail=request.args.get("email")
    return render_template('register.html',names=name,number=num,email=mail)
if __name__ == '__main__':
    app.run(debug=True)