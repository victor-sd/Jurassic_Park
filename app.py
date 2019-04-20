from flask import Flask
from flask import render_template

from jp.dino import dinosaurs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

