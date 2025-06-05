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

# Variável que conta quantas jogadas foram feitas    
quantidades_escolhas = 0

# Cria o grid inicial com 9 posições vazias
grid = ["_"] * 9

# Início do loop principal do jogo  
while True:

 # Loop que valida a jogada do jogador  
  while True:
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

# Marca a jogada do jogador no grid
  grid[escolha - 1] = "X"
  quantidades_escolhas += 1

 # Verifica se o jogador ganhou
  vencedor = verifica_grid(grid,"X")

  if vencedor != 0:
    break
# Se todas as posições forem preenchidas e ninguém ganhou, é empate
  if quantidades_escolhas == 9:
    break

  imprime_grid(grid) # Mostra o grid após a jogada do jogador

# Jogada do computador (escolhe posição aleatória livre)
  escolha_computador = random.randint(1,9)
  while grid[escolha_computador-1] != "_":
    escolha_computador = random.randint(1,9)

 # Marca a jogada do computador no grid
  grid[escolha_computador - 1] = "O"
  quantidades_escolhas += 1

# Verifica se o computador ganhou
  vencedor = verifica_grid(grid,"O")
  if vencedor != 0:
    break

  imprime_grid(grid) # Mostra o grid após a jogada do computador

# Mensagem final com resultado 
if vencedor == 1:
    print("Parabéns, você ganhou!")
elif vencedor == 2:
   print ("Você perdeu, o computador ganhou!")
else:
    print("Deu velha, ninguém ganhou, foi empate!")

imprime_grid(grid)# Mostra o resultado final do Grid