from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def user(name):
    return render_template('chart1.html')

if __name__ == "__main__":
    app.run()




