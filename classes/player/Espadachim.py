from classes.Entitie import Entitie

class Espadachim(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=96, dano_base=12, defesa_base=10)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"Avançando, o espadachim {self.nome} puxa a sua katana e usa seu ataque Sanzen Sekai!"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 2.0)  # Ataque especial com dano aumentado
        print(
            f"Incrivelmente, {self.nome} segura uma katana com a boca e duas com as mãos e usa seu ataque Santoryu Ougi!"
        )
        print(f"DANO: {dano}\n")
        return dano

    def receber_dano(self, dano_recebido):
        super().receber_dano(dano_recebido)
        print(
            f"{self.nome} demonstra uma resistência impressionante, ignorando a dor e mantendo-se focado na batalha!"
        )

    def defender(self):
        super().defender()
        print(
            f"{self.nome}, determinado na batalha, se preparou para o ataque do inimigo!"
        )
        print(f"DEFESA BASE: {self.defesa_base}")
        print(f"DEFESA BÔNUS: {self.defesa_bonus}\n")

    def descansar(self):
        if self.vida == self.vida_maxima:
            print(f"{self.nome} não precisa descansar.\n")
        else:
            if self.vida + 5 > self.vida_maxima:
                self.vida = self.vida_maxima
            else:
                self.vida += 5
            print(
                f"\n{self.nome} repousa por um momento, recuperando suas forças para a próxima batalha.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e se torna ainda mais habilidoso com sua katana!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! 'Minha lâmina se tornará ainda mais afiada!' ele exclamou com determinação!\n"
        )
        super().exibir_detalhes()
