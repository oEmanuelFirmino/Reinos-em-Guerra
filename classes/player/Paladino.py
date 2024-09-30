from classes.Entitie import Entitie

class Paladino(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=100, dano_base=15, defesa_base=12)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"O {self.nome} levanta sua espada reluzente e grita: 'Em nome da justiça!'"
            f" Ele avança com determinação, cortando o ar com sua lâmina."
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 2.5)
        print(
            f"O {self.nome} invoca a luz divina e brada: 'Sinta o poder da justiça!'"
            f" Uma onda de energia sagrada irrompe, atingindo seus inimigos."
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"O {self.nome} ergue seu escudo brilhante, clamando: 'Nada pode passar!'"
            f" A luz de sua armadura brilha, protegendo-o de ataques."
        )
        print(f"DEFESA BASE: {self.defesa_base}")
        print(f"DEFESA BÔNUS: {self.defesa_bonus}\n")

    def descansar(self):
        if self.vida == self.vida_maxima:
            print(
                f"{self.nome} não precisa descansar.\n"
            )
        else:
            if self.vida + 8 > self.vida_maxima:
                self.vida = self.vida_maxima
            else:
                self.vida += 8
            print(
                f"\nO {self.nome} se ajoelha em oração, buscando a bênção da luz."
                f" Com cada respiração, ele recupera suas forças.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e sente a luz dentro de si crescer!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! Ele ergue a espada para o céu e grita:"
            f" 'Eu sou a luz que brilha na escuridão!'\n"
        )
        super().exibir_detalhes()
