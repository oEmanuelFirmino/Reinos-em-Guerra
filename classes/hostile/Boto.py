from classes.Entitie import Entitie

class Boto(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=75, dano_base=10, defesa_base=8)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"Com um sorriso enigmático, o {self.nome} desliza" 
            f" pelas águas escuras e murmura: 'A correnteza do rio leva todos,"
            f" inclusive você... Prepare-se para afundar em meus domínios!"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 1.8)
        print(
            f"O {self.nome} sorri maliciosamente e murmura: 'As águas do rio"
            f" nunca falham'. Em um instante, uma onda gigantesca se ergue e desaba"
            f" sobre você."
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"Com um movimento ágil, o {self.nome} se transforma em névoa"
            f" sobre as águas, sussurrando: 'Aqui, ninguém me toca'. As correntes"
            f" ao redor se tornam um escudo"
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
                f"\nO {self.nome} submerge lentamente nas águas calmas, desaparecendo"
                f" em um silêncio profundo. 'No rio, até o tempo para', ele murmura,"
                f" enquanto recupera suas forças nas profundezas.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e parece estar ainda mais galanteador!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! Renascendo das profundezas, sorri: 'O"
            f" rio me fortaleceu. Agora, sou imbatível!'!\n"
        )
        super().exibir_detalhes()
