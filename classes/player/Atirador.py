from classes.Entitie import Entitie

class Atirador(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=80, dano_base=8, defesa_base=7)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"Avançando com precisão, o atirador {self.nome} ergue sua arma e dispara o tiro Eagle Strike!"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 1.5)  # Ataque especial com dano aumentado
        print(
            f"Com uma habilidade impressionante, {self.nome} equilibra uma arma com a mão esquerda e outra com a direita, usando o ataque Double Shot!"
        )
        print(f"DANO: {dano}\n")
        return dano

    def receber_dano(self, dano_recebido):
        super().receber_dano(dano_recebido)
        print(
            f"{self.nome} hesita por um momento, sentindo o impacto, mas se esforça para se manter de pé, lutando contra a dor para continuar a batalha."
        )

    def defender(self):
        super().defender()
        print(
            f"{self.nome}, com determinação, se posiciona estrategicamente para bloquear o ataque inimigo!"
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
                f"\n{self.nome} respira fundo e se concentra, recuperando suas forças para a próxima batalha.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e aprimora suas habilidades de tiro!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! 'Meu alvo está sempre à vista!', ele afirma, confiante!\n"
        )
        super().exibir_detalhes()
