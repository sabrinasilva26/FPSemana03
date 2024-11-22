from collections import deque


palavras = input()

fila = palavras.split() 
fila1= deque()

for letra in fila:
  fila1.appendleft(letra) #acrescenta no sentido oposto



print(fila1)
for palavra in fila:

  if 'o' in palavra.lower():
    print(palavra)
    
