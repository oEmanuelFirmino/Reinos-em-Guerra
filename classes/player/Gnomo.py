from classes.Entitie import Entitie

class Gnomo(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=100, dano_base=15, defesa_base=5)

    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(f"{self.nome} avança com um grito selvagem, desce seu machado com força esmagadora, "
              f"causando um golpe profundo no inimigo.")
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial(round((self.dano_base + self.level) * 1.8))
        print(f"Tomado por uma fúria implacável, {self.nome} ruge como uma fera indomável, "
              f"canalizando toda a sua força em um ataque devastador!")
        print(f"DANO: {dano}")
        print(f"USOS RESTANTES DO ESPECIAL:{self.usos_especial}\n")
        return dano
    
    def receber_dano(self, dano):
        aux = self.vida_maxima
        super().vida(dano)
        print(f"{self.nome} balança suas espessas costelas para bloquear o ataque, absorvendo parte do impacto.")
        print(f"DANO RECEBIDO: {aux - super().vida()}")
        print(f"VIDA RESTANTE: {super().vida}\n")
   
    def defender(self):
        super().defender()
        print(f"{self.nome} ergue seu escudo com firmeza e se prepara para o impacto.(Defesa bonus melhorada!)")
        print(f"DEFESA BASE: {self.defesa_base}")
        print(f"DEFESA BÔNUS: {self.defesa_bonus}\n")
   
    def descansar(self):
        if self.vida == self.vida_maxima:
            print(f"{self.nome} já está em plena forma e não precisa descansar.\n")
        else:
            if self.vida + 10 > self.vida_maxima:
                self.vida = self.vida_maxima
            else:
                self.vida += 10
            print(f"\n{self.nome} recupera suas forças e sente sua energia renovada.\nVIDA ATUAL: {self.vida}\n")

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(f"{self.nome} ganha {exp} pontos de experiência e sente sua força aumentar!")
            self.subir_de_nivel()
        else:
            print(f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n")
    
    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(f"{self.nome} subiu de nível e está mais forte do que nunca!\n")
        super().exibir_detalhes()

    
