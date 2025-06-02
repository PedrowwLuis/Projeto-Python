import random

print ("Bem vindo ao Jogo da velha")
print ("Você vai jogar contra o computador")
print ("Ganha quem conseguir fazer uma linha, coluna ou diagonal do grid com o mesmo símbolo")
 
print ("Você precisa escolher uma posição no grid para marcar sua jogada, veja o grid:")
print ("_ _ _")
print ("_ _ _")
print ("_ _ _")
print ("escolha um número de 1 a 9 para sua jogada, conforme o grid a seaguir seguir")
print ("1 2 3")
print ("4 5 6")
print ("7 8 9")

def imprime_grid(grid):
 print ("O status do grid é\n")

 for indice in range(len(grid)):
    print(grid[indice], end="  ")
    if indice == 2 or indice == 5 or indice == 8:
        print("")

def verifica_grid(grid):
  
 quantidades_escolhas = 0

grid = ["_"] * 9
  
while True:
 
 escolha = int(input("Qual é a sua escolha"))

 while grid[escolha-1] != "_":
  print("Sua  escolha foi inválida, veja como está o grid")
 imprime_grid(grid)
 escolha = int(input("Qual é a sua escolha"))

 grid[escolha-1] = "X"
 quantidades_escolhas += 1

 vencedor = verifica_grid(grid)
 if vencedor != 0:
   break
 
 if quantidades_escolhas == 9
   break
 
 imprime_grid(grid) 

 escolha_computador = random.randint(1,9) 
 while grid[escolha_computador-1] != "_":
  escolha_computador = random.randint(1,9)    

 grid[escolha_computador-1] = "O"
 vencedor = verifica_grid(grid)
 quantidades_escolhas += 1
 if vencedor != 0:
   break
 imprime_grid(grid) 
 
 if vencedor == 1:
    print("Parabéns, você ganhou!")
 elif vencedor == 2:
   print ("Você perdeu, o computador ganhou!")
 else:
    print("Deu velha, ninguém ganhou, foi empate!")