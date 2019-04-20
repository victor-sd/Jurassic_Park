from flask import Flask
from flask import render_template
import json

from jp.dino import dinosaurs

app = Flask(__name__)

@app.route('/')
def index():
    d = dinosaurs()
    return render_template('ListeDino.html',d=json.loads(d.text))

