from classes.Entitie import Entitie

class Boitata(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=80, dano_base=12, defesa_base=10)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"O {self.nome} avança com força, suas patas batendo no chão,"
            f" e berra: 'Sinto a batida do meu coração, e isso é o suficiente para derrubar você!'"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 2)
        print(
            f"O {self.nome} faz uma dança mágica, girando e se transformando,"
            f" enquanto grita: 'Prepare-se para a explosão do Boi Tatu!'"
        )
        print(f"DANO: {dano}\n")
        return dano

    def defender(self):
        super().defender()
        print(
            f"O {self.nome} se posiciona firme, usando sua força para absorver o ataque,"
            f" e ressoa: 'Nada pode me derrubar quando a música toca!'"
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
                f"\nO {self.nome} se deita sob a luz da lua, encantado pelas estrelas,"
                f" e murmura: 'Cada descanso é uma nova dança'.\nVIDA ATUAL: {self.vida}\n"
            )

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(
                f"{self.nome} ganha {exp} pontos de experiência e começa a tocar uma melodia,"
                f" refletindo sobre suas conquistas!"
            )
            self.subir_de_nivel()
        else:
            print(
                f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n"
            )

    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(
            f"{self.nome} sobe de nível! Ele ergue a cabeça e grita:"
            f" 'Cada batida da minha dança é um passo para a vitória!'\n"
        )
        super().exibir_detalhes()
