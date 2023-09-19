class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}'

class Filme (Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao}min - Likes: {self._likes}'

class Serie (Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.temporadas} temporadas - Likes: {self._likes}'
    
class Playlist:
    def __init__ (self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__ (self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas
    
    def __len__(self):
        return len(self._programas)