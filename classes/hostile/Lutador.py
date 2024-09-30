from classes.Entitie import Entitie

class Lutador(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=96, dano_base=12, defesa_base=9)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(
            f"Avançando com ferocidade, o vilão {self.nome} desferiu um golpe devastador com seu punho, "
            f"usando o ataque Brutal Smash!"
        )
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 1.5)  # Ataque especial com dano aumentado
        print(
            f"Com uma força impressionante, {self.nome} executa uma série de ataques rápidos, golpeando com os punhos e os pés "
            f"no ataque Pistol!"
        )
        print(f"DANO: {dano}\n")
        return dano

    def receber_dano(self, dano_recebido):
        super().receber_dano(dano_recebido)
        print(
            f"{self.nome} sente a dor, mas um sorriso sarcástico surge em seu rosto; ele se recusa a mostrar fraqueza e "
            f"mantém sua postura desafiadora."
        )

    def defender(self):
        super().defender()
        print(
            f"{self.nome}, com um olhar frio, se prepara para desviar do ataque do oponente, pronto para contra-atacar!"
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
                f"\n{self.nome} faz uma pausa estratégica, recuperando suas forças para continuar lutando.\nVIDA ATUAL: {self.vida}\n"
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
            f"{self.nome} sobe de nível! Ele grita: 'A luta está apenas começando!'\n"
        )
        super().exibir_detalhes()
