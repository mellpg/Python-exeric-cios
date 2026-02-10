'''

5) Exemplo em Python
Duas funções, uma chamando a outra
Objetivo:

Uma função calcula a média

Outra função decide se o aluno passou

Cada função tem seu próprio escopo



'''

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


def verificar_aprovacao(nota1, nota2):
    media = calcular_media(nota1, nota2)

    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Uso da função (fora dela)

resultado = verificar_aprovacao(8, 6)
print(resultado)

'''

6) O que está acontecendo de verdade

nota1 e nota2 em calcular_media
→ só existem dentro dessa função

nota1 e nota2 em verificar_aprovacao
→ são outros parâmetros, outro escopo

Mesmo nome ≠ mesma variável.

verificar_aprovacao chama calcular_media

calcular_media faz o cálculo e retorna

verificar_aprovacao usa o valor retornado

Isso é divisão correta de funções.

7) Regra prática para você memorizar

Função não vê variáveis internas de outra

Parâmetros são sempre locais

Mesmo nome em funções diferentes não conflita

Uma função pode chamar outra sem problema

Nunca defina duas funções com o mesmo nome

'''

# Maneira organizada
def pi():
    # Função apenas para definir Pi constante
    return 3.14


print(pi())


def quadrado(x):
    # Função apenas para retornar o quadrado de um número
    return x**2

print(quadrado(8))

def areac(R):
    # Função apenas para calcular a área de um círculo
    # Dado raio R
    # Pi vezes raio ao quadrado
    return pi() * quadrado(R)


print(areac(6))

'''
def coroa(r1,r2):

    Forma mais rigorosa:
    impede resultados inválidos
    deixa o erro explícito
    é o padrão em código sério
    if r1 < r2:
        # raise: Palavra-chave usada para forçar uma exceção (erro) a ocorrer.
        # ValueError(...): É o tipo de exceção que indica
        # que o valor não faz sentido para operação!
        raise ValueError("r1 deve ser maior ou igual a r2")
    else
    return areac(r1) - areac(r2)
'''
# Forma menos rigorosa
# R1 PRECISA ser maior que R2
# Em vez de um if e else
# Podemos apenas corrijir a entrada dessa forma...

def coroa(r1, r2):
    if r2 > r1:
        # Vai trocar os valores
        # r1 vai passar a ter o maior valor
        # e o r2 vai passar a ter o menor
        r1, r2 = r2, r1

    return areac(r1) - areac(r2)


print(coroa(6,3))



# Função para calcular área do quadrado
# dado o comprimento de um de seus lados

def area_quadrado(x):
    return x**2

# Volume de uma pirâmide quadrangular
# Dados:
# V: volume da pirâmide (medida tridimensional)
# 1/3 , volume é um terço do volume do prisma
# de mesma base e altura
# h: Altura da pirâmide
# l: comprimento do lado do quadrado

# Fórmula: v = (1/3) * x**2 * h
'''

def v_piram(h: int, x: int) -> int:
    v = (1/3) * area_quadrado(x) * h
    return v

lado = int (input("Digite o comprimento do lado do quadrado:"))
altura = int (input("Digite a altura da pirâmide:"))
volume = v_piram(altura,lado)
print(f"O volume é: {volume:.0f}")

'''

'''

# Cálculo com imposto
# imposto = pb * 0.15
# preço final + imposto



def imposto(pb: float) -> float:
    return pb * 0.15
    

def pf(pb: float) -> float:
    # Vai chamar o pb do imposto
    # e somar com o imposto
    # Exemplo: pf recebe o valor(pb = 30)
    # Você chama o imposto(pb)
    # Imposto é calculado
    # retorna 200 + 30 = 230
    return pb + imposto(pb)

pFinal = float (input("Digite o preço base: "))
resultado = pf(pFinal)
print(f"O preço final (com imposto) foi de : {resultado:.2f}")



taxa = 0.20

def desconto(p: float, taxa: float) -> float:
    return p * taxa

def preco_final(p: float) -> float:
    # SEMPRE chamar os parãmetro
    # MESMA COISA
    # preco_final vai receber(p)
    # diminuindo p - desconto
    # Não esquecer de ao chamar a função
    # CHAMAR OS PARÂMETROS!!!
    # Retorna o desconto:
    return p - desconto(p,taxa)

p_inicial = float(input("Digite o preço original: "))
p_final = preco_final(p_inicial)
print(f"O preço final (com desconto) foi de : {p_final:.2f}")


'''


    

    



        
   
