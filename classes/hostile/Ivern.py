from classes.Entitie import Entitie

class Ivern(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=80, dano_base=12, defesa_base=10)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"O {self.nome} ergue seu bastão de madeira e diz: 'A natureza se ergue em meu nome!'"
            f" Ele conjura raízes do solo, atingindo seu inimigo com um ataque poderoso."
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 2.0)
        print(
            f"O {self.nome} convoca a essência da floresta, gritando: 'A força da natureza!"
            f" Cresçam, minhas raízes!' Uma explosão de energia verde atinge seus inimigos."
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"O {self.nome} se envolve em um manto de folhas e flores, exclamando:"
            f" 'A natureza me protege!' Suas defesas aumentam enquanto ele se camufla."
        )
        print(f"DEFESA BASE: {self.defesa_base}")
        print(f"DEFESA BÔNUS: {self.defesa_bonus}\n")

    def descansar(self):
        if self.vida == self.vida_maxima:
            print(
                f"{self.nome} não precisa descansar.\n"
            )
        else:
            if self.vida + 6 > self.vida_maxima:
                self.vida = self.vida_maxima
            else:
                self.vida += 6
            print(
                f"\nO {self.nome} se senta sob uma árvore antiga, respirando a energia da floresta."
                f" 'A natureza me rejuvenesce', ele murmura enquanto recupera suas forças.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e sente a energia da floresta fluir!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! Ele ergue suas raízes para o céu e diz:"
            f" 'Eu sou o guardião da floresta e estou mais forte do que nunca!'\n"
        )
        super().exibir_detalhes()
