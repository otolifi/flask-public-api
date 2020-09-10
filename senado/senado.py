from flask import Blueprint, render_template
import requests as req
import json

bp_senado = Blueprint('senado', __name__, template_folder='templates', url_prefix='/senado')


@bp_senado.route('/')
def index():
    url = "http://legis.senado.leg.br/dadosabertos/senador/lista/atual?uf=to"
    header = {"Accept": "application/json"}
    response = req.get(url, headers=header)
    response_json = json.loads(response.content)
    data = response_json["ListaParlamentarEmExercicio"]["Parlamentares"]["Parlamentar"]
    return render_template('index.html', data=data)
