# Leitura dos valores de entrada
a, b = map(int, input().split())

# Condicional para verificar se os valores são iguais
if a == b:
    print(a)  # Ou print(b), ambos são iguais
else:
    print(max(a, b))  # Se diferentes, imprime o maior
