# Argumentos Default

# Argumento default é um valor que a função usa sozinha se você não passar nada.

def mostrar_numero(numero=10):
    print(numero)

# Vai mostrar o número:

mostrar_numero()

# Sem default (Obrigatório Passar)

def soma(a, b):
    print(a + b)

soma(2, 3)   # funciona
# soma(2)      # ERRO


# CUIDADOS

'''

Quando você chama uma função
o python liga os valores aos parâmetros pela ordem

def func(a, b):
    print(a, b)

func(5, 7)
O Python entende:

a = 5

b = 7

Isso é simples porque todos são obrigatórios.

Agora entra o argumento default

Veja esta definição:

def func(a, b=10):
    print(a, b)


Aqui:

a → obrigatório

b → opcional (tem valor padrão 10)

Chamadas possíveis
func(5)      # a = 5, b = 10
func(5, 20)  # a = 5, b = 20


Até aqui, tudo consistente.

Aqui entra o problema...

def func(a=10, b):
    print(a, b)

Pergunta:
👉 Se eu chamar func(5), o que é 5?

ossibilidades:

a = 5 e b fica sem valor?

a usa 10 e b = 5?

O Python não consegue decidir.

Por isso, ele nem deixa você definir a função.

Erro real do Python:

SyntaxError: non-default argument follows default argument

Se um parâmetro é opcional, todos que vêm depois dele também precisam ser opcionais.

Por isso:

def func(a, b=10):   # OK
    pass


Mas:

def func(a=10, b):   # NÃO
    pass

Regra final para você guardar

Obrigatórios → primeiro

Opcionais (default) → depois

O problema não é a posição “depois” no código, é o tipo do parâmetro

Primeiro: o que é “obrigatório” e “opcional”
Obrigatório

→ não tem valor padrão

a
b

Opcional (default)

→ tem valor padrão

b=10

Agora olhe para este exemplo (o que DEU CERTO)
def func(a, b=10):
    pass


a → obrigatório

b=10 → opcional

Ordem:

obrigatório → opcional

Agora o exemplo que NÃO pode
def func(a=10, b):
    pass


a=10 → opcional

b → obrigatório

Forma correta de pensar

👉 O Python precisa primeiro lidar com os parâmetros obrigatórios.
👉 Só depois ele aceita parâmetros opcionais (default).

Ou seja:

obrigatórios → primeiro
opcionais (default) → depois

'''

def saudacao(nome = "Mel"):
    print("Oi!", nome)

saudacao()
saudacao("Joaquim")

'''
Por que não usei return?

Porque essa função só exibe algo na tela.
Ela não precisa devolver nenhum valor para quem chamou.

def saudacao(nome="Mel"):
    print("Oi,", nome)


Essa função:

executa uma ação (mostrar texto)

termina

retorna implicitamente None

Isso é comportamento padrão do Python.

Quando return é necessário

Você usa return quando:

o valor precisa ser usado depois

outra função depende desse resultado

você vai guardar o resultado em uma variável

'''

def saudacao2(nome):
    return "Oi! " + nome

nome_User = input("Digite seu nome:")
mensagem = saudacao2(nome_User)
print(mensagem)
print("\n")

# Função que retorna dado dois inteiros x e y retorna x**y
def dados(x: int, y: int) -> int:
    return x**y

valor = dados(4,5)
print(valor)

# Isso aqui é um argumento default
# Se não fornecer o segundo parâmetro
# automaticamente a fução vai considerar 2
# Devem ser sempre os úçtimos
def potencia(x, y = 2):
    return x**y

valor2 = potencia(3,2)
print(valor2)



