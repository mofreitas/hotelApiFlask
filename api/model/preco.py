from api import db

class Preco(db.Model):
    __tablename__ = 'preco'

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column("preco", db.Float)
    tipo = db.Column("tipo", db.String(10))
    periodo = db.Column("periodo", db.String(20))
    hotel_id = db.Column("hotel_id", db.Integer, db.ForeignKey('hotel.hotel_id'))

@db.event.listens_for(Preco.__table__, 'after_create')
def criar_precos(*args, **kwargs):
    db.session.add(Preco(preco=110, tipo="Regular", hotel_id=1, periodo="semana"))
    db.session.add(Preco(preco=80, tipo="Reward", hotel_id=1, periodo="semena"))
    db.session.add(Preco(preco=90, tipo="Regular", hotel_id=1, periodo="fim_semana"))
    db.session.add(Preco(preco=80, tipo="Reward", hotel_id=1, periodo="fim_semana"))
    
    db.session.add(Preco(preco=160, tipo="Regular", hotel_id=2, periodo="semana"))
    db.session.add(Preco(preco=110, tipo="Reward", hotel_id=2, periodo="semana"))
    db.session.add(Preco(preco=60, tipo="Regular", hotel_id=2, periodo="fim_semana"))
    db.session.add(Preco(preco=50, tipo="Reward", hotel_id=2, periodo="fim_semana"))

    db.session.add(Preco(preco=220, tipo="Regular", hotel_id=3, periodo="semana"))
    db.session.add(Preco(preco=100, tipo="Reward", hotel_id=3, periodo="semana"))
    db.session.add(Preco(preco=150, tipo="Regular", hotel_id=3, periodo="fim_semana"))
    db.session.add(Preco(preco=40, tipo="Reward", hotel_id=3, periodo="fim_semana"))
    db.session.commit()
