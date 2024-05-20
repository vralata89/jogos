import random

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, outro):
        dano = self.ataque - outro.defesa
        if dano > 0:
            outro.vida -= dano
        return dano

    def esta_vivo(self):
        return self.vida > 0

class Jogador(Personagem):
    def __init__(self, nome, classe):
        if classe == "Guerreiro":
            super().__init__(nome, 100, 20, 10)
        elif classe == "Mago":
            super().__init__(nome, 70, 30, 5)
        elif classe == "Arqueiro":
            super().__init__(nome, 80, 25, 7)
        self.experiencia = 0

    def ganhar_experiencia(self, quantidade):
        self.experiencia += quantidade

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa, experiencia):
        super().__init__(nome, vida, ataque, defesa)
        self.experiencia = experiencia
