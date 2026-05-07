from Repository.usuario_repository import CinemaRepository

class CinemaService:
    def __init__(self):
        self.repo = CinemaRepository()

    def agendar(self, f, s, h):
        if self.repo.sala_ocupada(s, h):
            return "Erro: Sala ocupada!"
        
        self.repo.salvar(f, s, h)
        return "Sessão agendada!"