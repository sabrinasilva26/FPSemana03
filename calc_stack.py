from collections import deque


numeros_str = input()


numeros = [int(x) for x in numeros_str.split()]


pilha = deque(numeros)


print(pilha)



while pilha:
  numero = pilha.pop()
  print(numero ** 2)