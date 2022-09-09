from api import db
from datetime import datetime

class Reserva(db.Model):
    __tablename__ = 'reserva'

    numero_reserva = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    tipo_reserva = db.Column(db.String(20))
    observacoes = db.Column(db.Text)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotel.hotel_id"))
    periodo_inicio = db.Column(db.DateTime)
    periodo_fim = db.Column(db.DateTime)
    preco = db.Column(db.Float)
    ativo = db.Column(db.Boolean, default=True)

    hotel = db.relationship("Hotel", uselist=False)

    def get_dict_hotel(self):
        return {"numero_reserva": self.numero_reserva, \
            "nome": self.nome, \
            "telefone": self.telefone, \
            "email": self.email, \
            "periodo": f'{self.periodo_inicio.strftime("%d%b%Y (%a)")}-{self.periodo_fim.strftime("%d%b%Y (%a)")}', \
            "hotel": self.hotel.nome, \
            "tipo": self.tipo_reserva, \
            "preco": self.preco}
