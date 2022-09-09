from api import Reserva
from api import db

class ReservaDao():
    @staticmethod
    def criarReserva(reserva: 'Reserva'):
        db.session.add(reserva)
        db.session.commit()

    @staticmethod
    def consultarReservas():
        return Reserva.query.filter_by(ativo=True).all()

    @staticmethod
    def consultarReservasByAttributes(numero_reserva, hotel, periodoInicio, periodoFim, tipo_reserva):
        return Reserva.query.filter_by(numero_reserva=numero_reserva, hotel=hotel, \
            periodo_inicio=periodoInicio, periodo_fim=periodoFim, tipo_reserva=tipo_reserva).all()


    @staticmethod
    def removerReserva(reserva):
        reserva.ativo = False
        db.session.commit()

    @staticmethod
    def getReservaAtivaByNumero(numero_reserva):
        return Reserva.query.filter_by(numero_reserva=numero_reserva, ativo=True).first()