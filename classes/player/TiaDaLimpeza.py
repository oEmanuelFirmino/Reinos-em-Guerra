from classes.Entitie import Entitie

class TiaDaLimpeza(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=80, dano_base=9, defesa_base=15)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"A {self.nome} agita sua vassoura e dispara um feitiço de limpeza,"
            f" gritando: 'Prepare-se para a limpeza geral! Ninguém escapa de mim!'"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 1.6)
        print(
            f"A {self.nome} ergue um balde mágico e clama: 'Com o poder da limpeza, eu purifico a sujeira!'"
            f" Uma onda de energia limpa o campo de batalha, causando dano a todos os inimigos."
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"A {self.nome} se agacha e levanta um manto de produtos de limpeza,"
            f" dizendo: 'Aqui, a sujeira não tem vez!' Sua defesa aumenta com o poder da organização."
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
                f"\nA {self.nome} faz uma pausa e organiza seu material de limpeza, sorrindo:"
                f" 'Uma pausa para respirar é sempre bem-vinda.' Ela recupera suas energias.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e se torna ainda mais eficiente na limpeza!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! 'Agora, a limpeza será ainda mais poderosa!'"
            f" ela exclamou enquanto se prepara para a próxima batalha!\n"
        )
        super().exibir_detalhes()
