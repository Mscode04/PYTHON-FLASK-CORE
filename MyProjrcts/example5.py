from flask import Flask, render_template


app = Flask(__name__, template_folder='template')
@app.route('/<int:num>')
def index(num):
    return render_template('index.html',n1=num)

if __name__ == '__main__':
    app.run(debug=True)