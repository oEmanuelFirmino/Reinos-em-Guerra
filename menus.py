import os
from classes.hostile import Esqueleto, Saci, Boto, Goblin, Curupira, Ivern, Lutador, Rei
from classes.player import Barbaro, Gnomo, Boitata, Paladino, TiaDaLimpeza, TiaDaMerenda, Espadachim, Atirador
import random
from ascii import reinos_em_guerra_ascii_art

def selecionar_personagem_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        reinos_em_guerra_ascii_art() 
        nome = input("Nome do personagem: ")
        print(f"+{'-'*30}+")
        print(f"| {'Selecione uma classe':^28} |")
        print(f"+{'-'*30}+")
        print(f"| {'1. Barbaro':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'2. Gnomo':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'3. Boitatá':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'4. Paladino':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'5. Tia da Limpeza':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'6. Tia da Merenda':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'7. Atirador':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'8. Espadachim':<28} |")
        print(f"+{'-'*30}+")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            return Barbaro(nome)
        if opcao == "2":
            return Gnomo(nome)
        if opcao == "3":
            return Boitata(nome)
        if opcao == "4":
            return Paladino(nome)
        if opcao == "5":
            return TiaDaLimpeza(nome)
        if opcao == "6":
            return TiaDaMerenda(nome)
        if opcao == "7":
            return Atirador(nome)
        if opcao == "8":
            return Espadachim(nome)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

def selecionar_inimigo_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print(f"+{'-'*30}+")
        print(f"| {'Selecione um inimigo':^28} |")
        print(f"+{'-'*30}+")
        print(f"| {'1. Esqueleto':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'2. Saci':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'3. Boto Cor de Rosa':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'4. Goblin':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'5. Curupira':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'6. Ivern':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'7. Lutador':<28} |")
        print(f"+{'-'*30}+")
        print(f"| {'8. Rei':<28} |")
        print(f"+{'-'*30}+")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            return Esqueleto("Puro Osso")
        if opcao == "2":
            return Saci("Saci Pererê")
        if opcao == "3":
            return Boto("Boto Cor De Rosa")
        if opcao == "4":
            return Goblin("Goblin")
        if opcao == "5":
            return Curupira("Curupira")
        if opcao == "6":
            return Ivern("Ivern")
        if opcao == "7":
            return Lutador("Ivern")
        if opcao == "8":
            return Rei("Ivern")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


def menu_batalha(personagem, inimigo):
    while personagem.vida > 0 and inimigo.vida > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print(f"+{'-'*37}+")
            print(f"| {'Selecione sua ação:':^35} |")
            print(f"+{'-'*37}+")
            print(f"{personagem.nome} {f'Vida: {personagem.vida}':^35}")
            print(f"{inimigo.nome} {f'Vida: {inimigo.vida}':^35}")
            print(f"+{'-'*37}+")
            print(f"| {'1. Atacar - Golpear o inimigo':<35} |")
            print(f"| {'2. Defender - Melhorar a defesa':<35} |")
            print(f"| {'3. Descansar - Recuperar vida':<35} |")

            if personagem.usos_especial > 0:
                print(f"| {'4. Usar especial - Usar magia':<35} |")
            print(f"| {'5. Exibir detalhes':<35} |")
            print(f"+{'-'*37}+")
            escolha = input("Selecione sua ação: ")

            if escolha == "1":
                dano = personagem.atacar()
                inimigo.vida -= dano
                break 
            elif escolha == "2":
                personagem.defender()
                break
            elif escolha == "3":
                personagem.descansar()
                break
            elif escolha == "4":
                if personagem.usos_especial > 0:
                    dano = personagem.especial()
                    inimigo.vida -= dano
                    break
                os.system('cls' if os.name == 'nt' else 'clear')
            elif escolha == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                personagem.exibir_detalhes()
            else:
                print("Escolha inválida, tente novamente...")
                os.system('cls' if os.name == 'nt' else 'clear')

        if inimigo.vida <= 0:
            print(f"\n{inimigo.nome} foi derrotado!\n")
            personagem.defesa_bonus = 5
            personagem.usos_especial = personagem.level + 2
            personagem.ganhar_exp(10+inimigo.level) 
            break

        acao_inimigo = random.choice(["atacar", "defender", "descansar"])
        
        print(f"\nAção do inimigo:")
        if acao_inimigo == "atacar":
            dano = inimigo.atacar()  
            personagem.vida -= dano
        elif acao_inimigo == "defender":
            inimigo.defender()
        elif acao_inimigo == "descansar":
            inimigo.descansar()

        if personagem.vida <= 0:
            print(f"\n{personagem.nome} foi derrotado!")
            break
        
        print(f"\n Vida de {personagem.nome} após ações: {personagem.vida}")
        print(f"\n Vida de {inimigo.nome} após ações: {inimigo.vida}")
        input("\nPressione Enter para continuar...")
