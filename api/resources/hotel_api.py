#coding: utf-8
from flask_restful import Resource, reqparse
from datetime import datetime
from api import HotelDao

class HotelApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("q", type=str)
        args = parser.parse_args()

        hoteis = HotelDao.getAllHoteis()

        consulta = args["q"]
        tipo, datas = consulta.split(":")
        datas_list = list(map(lambda data_str: datetime.strptime(data_str.strip()[0:9], "%d%b%Y"), datas.split(",")))
        tipo = tipo.strip()

        melhor_hotel = hoteis[0]
        preco_minimo = melhor_hotel.get_preco_dias(tipo, datas_list)

        for hotel in hoteis[1:]:
            preco = hotel.get_preco_dias(tipo, datas_list)
            if preco < preco_minimo or (preco == preco_minimo and hotel.classificacao > melhor_hotel.classificacao):
                preco_minimo = preco
                melhor_hotel = hotel

        return {"cheapest" : melhor_hotel.nome}