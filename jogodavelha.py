import random

# Mensagens iniciais explicando o funcionamento do jogo
print ("Bem vindo ao Jogo da velha!")
print ("Você vai jogar contra o computador")
print ("Ganha quem conseguir fazer uma linha, coluna ou diagonal do grid com o mesmo símbolo")

# Mostra ao jogador o exemplo de grid e posições 
print ("Você precisa escolher uma posição no grid para marcar sua jogada, veja o grid: ")
print ("_ _ _")
print ("_ _ _")
print ("_ _ _")
print ("escolha um número de 1 a 9 para sua jogada, conforme o grid a seguir ")
print ("1 2 3")
print ("4 5 6")
print ("7 8 9")

# Função que imprime o grid atual do jogo
def imprime_grid(grid):
 print ("O status do grid é\n")

 for indice in range(len(grid)):
    print(grid[indice], end="  ")
    if indice == 2 or indice == 5 or indice == 8:
        print("")

# Função que verifica se houve vitória
def verifica_grid(grid, jogador):

  #Verificação de vitoria horizontal
  if grid[0] == jogador and grid[1] == jogador and grid[2] == jogador:
    if jogador == "X":
      return 1 
    else:
      return 2 
  if grid[3] == jogador and grid[4] == jogador and grid[5] == jogador:
      if jogador == "X":
        return 1 
      else:
        return 2   
  if grid[6] == jogador and grid[7] == jogador and grid[8] == jogador:
     if jogador == "X":
        return 1
     else:
       return 2
     
    #Verificação de vitoria horizontal
  if grid[0] == jogador and grid[3] == jogador and grid[6] == jogador:
     if jogador == "X":
      return 1
     else:
       return 2    
  if grid[1] == jogador and grid[4] == jogador and grid[7] == jogador:
     if jogador == "X":
      return 1
     else:
       return 2   
  if grid[2] == jogador and grid[5] == jogador and grid[8] == jogador:
     if jogador == "X":
      return 1
     else:
       return 2
  
  #Verificação de vitoria diagonal
  if grid[0] == jogador and grid[4] == jogador and grid[8] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2
  if grid[2] == jogador and grid[4] == jogador and grid[6] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2
    
  return 0

while True:  # Loop do jogo completo
    quantidades_escolhas = 0
    grid = ["_"] * 9

# Loop da partida até alguém ganhar ou dar empate
    while True:
        while True:#Entrada do Jogador com Validação
            try:
                escolha = int(input("Qual é a sua escolha (1 a 9): "))
                if escolha < 1 or escolha > 9:
                    print("Escolha inválida! Digite um número entre 1 e 9.")
                    continue
                if grid[escolha - 1] != "_":
                    print("Essa posição já está ocupada. Veja o grid:")
                    imprime_grid(grid)
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números inteiros de 1 a 9.")

  #Atualização de Grid com as Jogadas do Jogador
        grid[escolha - 1] = "X"
        quantidades_escolhas += 1

    # Verifica se o jogador venceu
        vencedor = verifica_grid(grid, "X")
        if vencedor != 0:
            break
        if quantidades_escolhas == 9:#Verifica se foi Velha
            break

        imprime_grid(grid)

    # Jogada do computador
        escolha_computador = random.randint(1, 9)
        while grid[escolha_computador - 1] != "_":
            escolha_computador = random.randint(1, 9)

        grid[escolha_computador - 1] = "O"
        quantidades_escolhas += 1

    # Verifica se o computador venceu
        vencedor = verifica_grid(grid, "O")
        if vencedor != 0:
            break

        imprime_grid(grid)

    # Mostra o resultado final
    if vencedor == 1:
        print("O resultado: Você ganhou!")
    elif vencedor == 2:
        print("O resultado: O computador ganhou!")
    else:
        print("O resultado: Deu velha! Empate!")

    imprime_grid(grid)

    # Pergunta se quer continuar
    continuar = input("Deseja continuar jogando? (S/N): ").strip().upper()
    if continuar != "S":
        print("Obrigado por jogar! Até a próxima!")
        break