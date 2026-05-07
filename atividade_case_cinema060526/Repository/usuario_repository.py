import sqlite3

class CinemaRepository:
    def __init__(self):
        self.con = sqlite3.connect('cinema.db')
        self.con.execute('CREATE TABLE IF NOT EXISTS sessoes (filme, sala, hora)')

    def sala_ocupada(self, sala, hora):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM sessoes WHERE sala=? AND hora=?", (sala, hora))
        return cur.fetchone()

    def salvar(self, f, s, h):
        self.con.execute("INSERT INTO sessoes VALUES (?,?,?)", (f, s, h))
        self.con.commit()