from classes.Entitie import Entitie

class Goblin(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=60, dano_base=8, defesa_base=6)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"O {self.nome} salta em direção ao seu inimigo com um sorriso maligno,"
            f" gritando: 'Paguem o que devem, ou vou roubar tudo que têm!'"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 1.5)
        print(
            f"O {self.nome} provoca o inimigo e faz um movimento rápido,"
            f" usando um truque para atacar de surpresa: 'Nunca subestime um goblin!'"
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"O {self.nome} se esconde atrás de uma rocha, dizendo:"
            f" 'Você nunca vai me pegar! Sou mais astuto do que parece!'"
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
                f"\nO {self.nome} se esconde em um canto escuro, recuperando suas forças,"
                f" enquanto conta suas riquezas furtadas.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e ri, dizendo:"
                f" 'Estou ficando cada vez mais poderoso!'"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! Ele levanta suas mãos e grita:"
            f" 'Sou o mestre dos tesouros! Ninguém pode me deter!'\n"
        )
        super().exibir_detalhes()
