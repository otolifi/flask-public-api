from flask import Flask
from cep.cep import bp_cep
from senado.senado import bp_senado


app = Flask(__name__)


app.register_blueprint(bp_cep)
app.register_blueprint(bp_senado)


if __name__ == "__main__":
    app.run()
