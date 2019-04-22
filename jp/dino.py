import requests

def dinosaurs():
    response = requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')
    return response

def detailDinosaur(name):
    name = name.lower()
    response = requests.get('https://medusa.delahayeyourself.info/api/dinosaurs/%s' % name)
    return response
