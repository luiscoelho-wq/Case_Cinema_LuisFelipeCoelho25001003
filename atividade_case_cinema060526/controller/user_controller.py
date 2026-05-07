from service.user_service import CinemaService

class CinemaController:
    def __init__(self):
        self.serv = CinemaService()

    def cadastrar(self, f, s, h):
        return self.serv.agendar(f, s, h)