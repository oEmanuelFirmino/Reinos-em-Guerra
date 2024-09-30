from classes.Entitie import Entitie

class Rei(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=100, dano_base=14, defesa_base=11)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"Com um sorriso irônico, {self.nome} avança e desferiu um golpe rápido, dizendo: "
            f"'Espero que você esteja preparado para o meu ataque Jet Gatling!'"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 1.6)  # Ataque especial com dano aumentado
        print(
            f"Usando sua agilidade, {self.nome} executa uma série de movimentos acrobáticos, lançando o ataque Gigant Fuusen, "
            f"enquanto provoca: 'Isso deve doer... ou não.'"
        )
        print(f"DANO: {dano}\n")
        return dano

    def receber_dano(self, dano_recebido):
        super().receber_dano(dano_recebido)
        print(
            f"{self.nome} se inclina dramaticamente, com uma expressão exagerada: 'Uau, que emocionante! O que vem a seguir, uma massagem?'"
        )

    def defender(self):
        super().defender()
        print(
            f"Com um olhar desdenhoso, {self.nome} se esquiva com um movimento elegante e diz: 'Ah, por favor, isso foi tão previsível!'"
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
                f"\n{self.nome} repousa em seu trono, recuperando suas forças com a confiança de um verdadeiro rei.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e se torna ainda mais formidável!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! 'Meu reino será invencível!', ele proclama com grande pompa!\n"
        )
        super().exibir_detalhes()
