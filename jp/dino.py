import requests

def dinosaurs():
    response = requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')
    return response
