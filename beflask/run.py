# from beflask import app

from flask import Flask
from beth.controller import Register_Blueprints

app = Flask(__name__)



if __name__ == '__main__':
    Register_Blueprints(app)
    # app.run(host='0.0.0.0', port='100', debug=True)
    app.run(debug=True)
