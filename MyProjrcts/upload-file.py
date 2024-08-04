import os.path

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')
app.config['UPLOAD_PATH'] = 'static/images'


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload',methods=['POST'])
def ind():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
    return "done"


if __name__ == '__main__':
    app.run(debug=True)
