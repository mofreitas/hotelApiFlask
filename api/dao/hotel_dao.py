from api import Hotel

class HotelDao():
    @staticmethod
    def getAllHoteis():
        return Hotel.query.all()

    @staticmethod
    def getHotelByNome(nomeHotel: str):
        return Hotel.query.filter_by(nome=nomeHotel).first()
        