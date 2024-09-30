from classes.Entitie import Entitie

class TiaDaMerenda(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=90, dano_base=8, defesa_base=12)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"A {self.nome} lança um prato de comida como se fosse uma arma, gritando:"
            f" 'Nada como uma refeição para te fazer cair na real!'"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 1.5)
        print(
            f"A {self.nome} faz uma oração silenciosa e, de repente, um banquete mágico surge!"
            f" 'Prepare-se para um ataque de sabores!' Ela utiliza o banquete para recuperar vida."
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"A {self.nome} ergue um enorme avental, dizendo: 'Aqui, ninguém passa fome!'"
            f" Ela se protege, aumentando sua defesa com o poder da comida caseira."
        )
        print(f"DEFESA BASE: {self.defesa_base}")
        print(f"DEFESA BÔNUS: {self.defesa_bonus}\n")

    def descansar(self):
        if self.vida == self.vida_maxima:
            print(
                f"{self.nome} não precisa descansar.\n"
            )
        else:
            if self.vida + 7 > self.vida_maxima:
                self.vida = self.vida_maxima
            else:
                self.vida += 7
            print(
                f"\nA {self.nome} senta-se em uma mesa cheia de delícias, respirando o aroma"
                f" da comida fresca. 'Um lanche sempre rejuvenesce', ela diz enquanto recupera"
                f" suas energias.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e fica ainda mais determinada a alimentar a todos!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! 'Mais um prato e estou pronta para qualquer desafio!'"
            f" ela exclamou enquanto se prepara para a batalha!\n"
        )
        super().exibir_detalhes()
