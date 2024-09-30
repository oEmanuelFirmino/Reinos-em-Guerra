from menus import selecionar_personagem_menu, selecionar_inimigo_menu,menu_batalha

def main():
    personagem = selecionar_personagem_menu()
    
    while personagem.vida > 0:
        inimigo = selecionar_inimigo_menu()
        
        menu_batalha(personagem, inimigo)
        
        if personagem.vida > 0:
            print("Parabéns, você venceu a batalha!")
        else:
            print("Você foi derrotado. Fim de jogo.")
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()