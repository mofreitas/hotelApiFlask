from api import db
from datetime import date

class Hotel(db.Model):
    __tablename__ = 'hotel'

    hotel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    classificacao = db.Column(db.Integer)
    preco = db.relationship('Preco')

    def get_preco_dia(self, tipo, dia: 'date'):
        weekday = "semana" if dia.weekday() < 5 else "fim_semana"
        for p in self.preco:
            if p.tipo == tipo and weekday == p.periodo:
                return p.preco

    def get_preco_dias(self, tipo, dias: 'list[date]'):
        total = 0
        for dia in dias:
            total += self.get_preco_dia(tipo, dia)

        return total
    
    
@db.event.listens_for(Hotel.__table__, 'after_create')
def criar_hoteis(*args, **kwargs):
    db.session.add(Hotel(nome='Lakewood', classificacao=3))
    db.session.add(Hotel(nome='Bridgewood', classificacao=4))
    db.session.add(Hotel(nome='Ridgewood', classificacao=5))
    db.session.commit()
