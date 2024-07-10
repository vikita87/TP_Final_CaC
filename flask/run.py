from flask import Flask
from app.views import *
from app.database import *
from flask_cors import CORS

app = Flask(__name__)

# Rutas de API-Rest

app.route('/', methods=['GET'])(index)

app.route('/api/clients/all', methods=['GET'])(get_all_client)

app.route('/api/client/create/', methods=['POST'])(create_client)

init_app(app)

CORS(app)

create_table_clientes()

if __name__ == '__main__':
    app.run(debug=True)