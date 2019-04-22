import requests

def dinosaurs():
    response = requests.get('https://allosaurus.delahayeyourself.info/api/dinosaurs/')
    return response

def detailDinosaur(slug):
    response = requests.get('https://medusa.delahayeyourself.info/api/dinosaurs/%s' % slug)
    return response
