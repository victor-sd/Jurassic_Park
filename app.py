from flask import Flask
from flask import render_template
import json

from jp.dino import dinosaurs,detailDinosaur

app = Flask(__name__)

@app.route('/')
def index():
    d = dinosaurs()
    return render_template('ListeDino.html',d=json.loads(d.text))


@app.route('/dinosaur/<slug>')
def detailDino(slug = None):
    detail = detailDinosaur(slug)
    return render_template('Dino.html',slug=slug,detail=json.loads(detail.text))

