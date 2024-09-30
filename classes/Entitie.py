class Entitie:
    def __init__(self, nome, level, vida_maxima, dano_base, defesa_base):
        self.nome = nome
        self.level = level
        self.vida_maxima = vida_maxima
        self._vida = vida_maxima
        self.dano_base = dano_base
        self.defesa_base = defesa_base
        self.defesa_bonus = 5
        self.exp = 0
        self.proximo_level = 100
        self.usos_especial = self.level + 2
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, value):
        self._vida = value
        return self._vida

    def atacar(self , bonus = 0):
        return self.dano_base + bonus
    
    def especial(self , bonus = 0):
        if self.usos_especial > 0:
            self.usos_especial -= 1
            return self.dano_base + bonus

    def defender(self):
        self.defesa_bonus += 5
    
    def descansar(self):
        if(self._vida + 10 > self.vida_maxima):
            return
        else:
            Entitie.vida += 10
    
    def ganhar_exp(self, exp):
        self.exp += exp
        if self.exp >= self.proximo_level:
            self.subir_de_nivel()   


    def subir_de_nivel(self):
        self.level += 1
        self.vida_maxima += 20
        self.vida = self.vida_maxima
        self.dano_base += 5
        self.defesa_base += 2
        self.exp = 0
        self.proximo_level = self.proximo_level * 1.5

    def exibir_detalhes(self):
        print(f"+{'-'*40}+")
        print(f"| {'DETALHES':^38} |")
        print(f"+{'-'*40}+")
        print(f"| {'Nome:':<15} {self.nome:<22} |")
        print(f"| {'Nível:':<15} {self.level:<22} |")
        print(f"| {'Vida:':<15} {self.vida}/{self.vida_maxima:<18} |")
        print(f"| {'Dano base:':<15} {self.dano_base:<22} |")
        print(f"| {'Defesa base:':<15} {self.defesa_base:<22} |")
        print(f"| {'Defesa bonus:':<15} {self.defesa_bonus:<22} |")
        print(f"| {'Experiência:':<15} {int(self.exp):<3}/{int(self.proximo_level):<18} |")
        print(f"+{'-'*40}+\n")

