import numpy as np
from flask import Flask, redirect, url_for, request, render_template
import pickle

app = Flask(__name__)
# model=pickle.load(open('models/model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contactus.html')
def contactus():
    return render_template('contactus.html')

@app.route('/help.html')
def help():
    return render_template('help.html')

@app.route('/main.html')
def main():
    return render_template('main.html')



if __name__ == '__main__':
    app.run(debug=True)
