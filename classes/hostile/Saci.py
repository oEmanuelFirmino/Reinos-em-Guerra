from classes.Entitie import Entitie

class Saci(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=50, dano_base=8, defesa_base=5)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"Com um riso travesso, o {self.nome} lança uma bola de fumaça,"
            f" gritando: 'Vamos ver se você consegue me pegar!'"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 2.0)
        print(
            f"O {self.nome} dá um salto ágil e desaparece em uma nuvem de"
            f" fumaça, surgindo atrás de você para um ataque surpresa!"
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"Com uma risada, o {self.nome} se esconde em um redemoinho de"
            f" folhas, sussurrando: 'Ninguém pode me tocar enquanto danço!'"
        )
        print(f"DEFESA BASE: {self.defesa_base}")
        print(f"DEFESA BÔNUS: {self.defesa_bonus}\n")

    def descansar(self):
        if self.vida == self.vida_maxima:
            print(
                f"{self.nome} não precisa descansar.\n"
            )
        else:
            if self.vida + 5 > self.vida_maxima:
                self.vida = self.vida_maxima
            else:
                self.vida += 5
            print(
                f"\nO {self.nome} dá um giro e desaparece por um momento,"
                f" recuperando suas forças nas sombras da floresta.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e ri: 'Estou apenas começando!'"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! Em um redemoinho de folhas, ele exclama:"
            f" 'Agora sou ainda mais travesso!'\n"
        )
        super().exibir_detalhes()
