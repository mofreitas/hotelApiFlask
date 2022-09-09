#coding: utf-8
from flask_restful import Resource, reqparse
from api import ReservaDao
from api import HotelDao
from api import Reserva
from datetime import datetime, timedelta

class ReservaApi(Resource):
    @staticmethod
    def get_dias_from_intervalo(dataInicio: 'datetime', dataFim: 'datetime'):
        lista_datas = []
        data = datetime.fromtimestamp(datetime.timestamp(dataInicio))
        while(data <= dataFim):
            lista_datas.append(data)
            data = data + timedelta(days=1)

        return lista_datas

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('numero_reserva', type=int)
        parser.add_argument('hotel', type=str)
        parser.add_argument('tipo_reserva', type=str)
        parser.add_argument('periodo', type=str)
        args = parser.parse_args()

        periodoInicioStr, periodoFimStr = args["periodo"].split("-")
        periodoInicio = datetime.strptime(periodoInicioStr[0:9], "%d%b%Y")
        periodoFim = datetime.strptime(periodoFimStr[0:9], "%d%b%Y")

        hotel = HotelDao.getHotelByNome(args["hotel"])
        reservas = ReservaDao.consultarReservasByAttributes(numero_reserva=args["numero_reserva"],\
            hotel=hotel, tipo_reserva=args["tipo_reserva"], periodoInicio=periodoInicio, \
            periodoFim = periodoFim)

        return [reserva.get_dict_hotel() for reserva in reservas], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, location='form')
        parser.add_argument('telefone', type=str, location='form')
        parser.add_argument('email', type=str, location='form')
        parser.add_argument('periodo', type=str, location='form')
        parser.add_argument('Hotel', type=str, location='form')
        parser.add_argument('tipo', type=str, location='form')
        parser.add_argument('observacoes', type=str, location='form')
        args = parser.parse_args()

        periodoInicioStr, periodoFimStr = args["periodo"].split("-")
        periodoInicio = datetime.strptime(periodoInicioStr[0:9], "%d%b%Y")
        periodoFim = datetime.strptime(periodoFimStr[0:9], "%d%b%Y")

        hotel = HotelDao.getHotelByNome(args["Hotel"])
        preco = hotel.get_preco_dias(args["tipo"], ReservaApi.get_dias_from_intervalo(periodoInicio, periodoFim))

        reserva = Reserva(nome=args["nome"], telefone=args["telefone"], email=args["email"], \
            hotel=hotel, tipo_reserva=args["tipo"], periodo_inicio = periodoInicio, \
            periodo_fim = periodoFim, observacoes=args["observacoes"], preco=preco)

        ReservaDao.criarReserva(reserva)
        return {"numero_reserva": reserva.numero_reserva}, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('numero_reserva', type=int)
        args = parser.parse_args()

        reserva = ReservaDao.getReservaAtivaByNumero(args["numero_reserva"])

        if(reserva != None):
            ReservaDao.removerReserva(reserva)
            return "Sucesso", 200
        else:
            return "Reserva não encontrada", 404