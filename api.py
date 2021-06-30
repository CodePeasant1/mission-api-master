from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:Onion23scion@localhost/mission-database.cofx4za1bb1a.us-east-1.rds.amazonaws.com'
app.config['SQLALCHAMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.route('/')
def root_page():
    return "Mission API"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
