from controller.user_controller import CinemaController

class CinemaView:
    def tela(self):
        c = CinemaController()
        f = input("Filme: ")
        s = input("Sala: ")
        h = input("Hora: ")
        print(c.cadastrar(f, s, h))