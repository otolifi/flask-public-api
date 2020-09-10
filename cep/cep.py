from flask import Blueprint, render_template
import requests as req

bp_cep = Blueprint('cep', __name__, template_folder='templates', url_prefix='/cep')


@bp_cep.route('/<cep>')
def index(cep):
    url = f"http://viacep.com.br/ws/{cep}/json"
    data = req.get(url).json()
    return render_template('index.html', data=data)
