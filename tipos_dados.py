# Tipos numéricos

# Tipo inteiro (int)
# Precisão fixa, ocupam uma palavra de memória
# representado com 32 bits ( de -2**31 a 2**31 - 1)

idade = 10
print(idade)

# Tipo flutuaente (float) : 10.15, -190.00005, 15e-5

altura  = 1.70
print(altura)

# Tipo complexo : (3+2j), (20j)
# Representado com 2 pontos flutuantes
# 1 para a real e outra para imaginária

# Declarando um número complexo: 3 + 4j
z = 3 + 4j
print(z)        # Saída: (3+4j)
print(type(z))  # Saída: <class 'complex'>


# Não há limites

# Testando...
def dobro(x):
    return x * 2
print("Para int:")
print(dobro(4))
print("Para float:")
print(dobro(4.5))
print("Para complexo")
print(dobro(3 + 2j))

def soma(x,y):
    return x + y

print("Para int:")
print(soma(4,100))
print("Para float:")
print(soma(100,1))
print("Para complexo")
print(soma(56,3 + 2j))

