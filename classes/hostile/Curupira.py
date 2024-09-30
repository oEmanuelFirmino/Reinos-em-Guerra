from classes.Entitie import Entitie

class Curupira(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=100, dano_base=12, defesa_base=10)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"O {self.nome} grita ferozmente, seus cabelos vermelhos brilhando,"
            f" e ataca com um golpe poderoso de suas garras, gritando: 'Ninguém toca"
            f" nas minhas florestas!'"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 2.5)
        print(
            f"O {self.nome} dá um salto impressionante e desaparece,"
            f" deixando apenas uma ilusão para confundir seu inimigo."
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"Com um movimento ágil, o {self.nome} se camufla entre as árvores,"
            f" sussurrando: 'A floresta é meu lar. Aqui, você não me toca!'"
        )
        print(f"DEFESA BASE: {self.defesa_base}")
        print(f"DEFESA BÔNUS: {self.defesa_bonus}\n")

    def descansar(self):
        if self.vida == self.vida_maxima:
            print(
                f"{self.nome} não precisa descansar.\n"
            )
        else:
            if self.vida + 10 > self.vida_maxima:
                self.vida = self.vida_maxima
            else:
                self.vida += 10
            print(
                f"\nO {self.nome} se deita sob a sombra das árvores, recuperando"
                f" suas forças com a energia da floresta.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e diz: 'Estou apenas aquecendo!'"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! Ele ergue os braços, exclamando:"
            f" 'A floresta me dá poder!'\n"
        )
        super().exibir_detalhes()
