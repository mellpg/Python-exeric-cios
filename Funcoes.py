def dobro(x): 
    return x*2

resultado = dobro(60)
print(resultado)

## Sintaxe
## def nome_da_funcao(parametros)
## return valor de retorno


# Função de sucessor
def sucessor(y):
    return y + 1

# Entrando com dados
# Prestar atenção em seu tipo
print("Função de Sucessor:")
num = int (input("Digite um número:"))

# Chamando a função:

resultado2 = sucessor(num)
print("O sucessor de: ", num, "é:",resultado2)

def multi(m,t):
    return m*t
print("Função de multiplicação:")
num2 = int(input("Digite um número:"))
num3 = int(input("Digite outro número:"))
resultado3 = multi(num2,num3)
print("O resultado da multiplicação é:", resultado3)



def modulo(z,v):
    return z%v
print("Função de módulo:")
num6 = int(input("Digite um número:"))
num7 = int(input("Digite outro número:"))
resultado4 = modulo(num6,num7)
print("O módulo é :", resultado4)



def div(s,g):
    return s/g
print("Função de divisão:")
num9 = int(input("Digite um número:"))
num12 = int(input("Digite outro número:"))
resultado5 = div(num9,num12)

if num9 < num12:
    print(" ERRO: dividendo é menor que o divisor.")
    print(" Digite novamente:")
else:
    print(" O resultado da divisão é:", resultado5)


def funcao_primeiro_grau(a,b,x):
    return (a*x) + b

print("Função primeiro grau:")
angular = int(input("Digite o coeficiente angular (a):"))
absissa = int(input("Digite a absissa (x):"))
if absissa < 0:
    print("A reta vai descer!")
else:
    print("A reta não vai descer!")
linear = int(input("Digite o coeficiente linear (b):"))
funcao = funcao_primeiro_grau(angular,absissa,linear)
print("A ordenada é: " , funcao)




