from classes.Entitie import Entitie

class Esqueleto(Entitie):
    def __init__(self, nome):
        super().__init__(nome, level=1, vida_maxima=80, dano_base=8, defesa_base=5)
   
    def atacar(self):
        dano = super().atacar(self.dano_base)
        print(f"{self.nome} avança com um ranger de ossos, desferindo um golpe mortal com suas garras afiadas.")
        print(f"DANO: {dano}")
        return dano

    def especial(self):
        dano = super().especial((self.dano_base + self.level) * 1.8)
        print(f"Com um grito sinistro, {self.nome} invoca uma onda de energia necromântica, "
              f"lançando um ataque aterrorizante que assola o inimigo.")
        print(f"DANO: {dano}\n")
        return dano
    
    def defender(self):
        super().defender()
        print(f"{self.nome} ergue suas costelas e osso de forma defensiva, endurecendo sua postura.(Defesa bonus melhorada!)")
        print(f"DEFESA BASE: {self.defesa_base}")
        print(f"DEFESA BÔNUS: {self.defesa_bonus}\n")
    
    def descansar(self):
        if self.vida == self.vida_maxima:
            print(f"{self.nome} não precisa descansar, seus ossos estão em perfeitas condições.\n")
        else:
            if self.vida + 5 > self.vida_maxima:
                self.vida = self.vida_maxima
            else:
                self.vida += 5
            print(f"\n{self.nome} recupera um pouco de energia ao repousar, seus ossos se tornam um pouco mais firmes.\nVIDA ATUAL: {self.vida}\n")

    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            print(f"{self.nome} ganha {exp} pontos de experiência e seus ossos parecem mais fortes!")
            self.subir_de_nivel()
        else:
            print(f"{self.nome} ganha {exp} pontos de experiência.\nEXPERIÊNCIA ATUAL: {self.exp}\n")
    
    def subir_de_nivel(self):
        super().subir_de_nivel()
        print(f"{self.nome} sobe de nível e suas habilidades necromânticas são aprimoradas!\n")
        super().exibir_detalhes()

