from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask import Flask

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
  
    with app.app_context():
        db.init_app(app)
        db.create_all()

    api.add_resource(HotelApi, '/api/v1/cheapest/')
    api.add_resource(ReservaApi, '/api/v1/reservas/')
    api.init_app(app)  

    return app

from .model.hotel import Hotel as Hotel
from .model.preco import Preco as Preco
from .model.reserva import Reserva as Reserva

from .dao.hotel_dao import HotelDao as HotelDao
from .dao.reserva_dao import ReservaDao as ReservaDao

from .resources.hotel_api import HotelApi as HotelApi
from .resources.reserva_api import ReservaApi as ReservaApi


