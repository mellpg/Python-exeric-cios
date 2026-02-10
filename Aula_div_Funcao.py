# Módulo e imperativo estruturado

# Código estruturado (tudo em um arquivo)

# programa.py

def tempo_trav(largura, vb):
    return largura / vb

def distancia_correnteza(vc, t):
    return vc * t

print("=== TRAVESSIA DO RIO ===")

largura = float(input("Digite a largura do rio: ").replace(',', '.'))
vb = float(input("Digite a velocidade do barco: ").replace(',', '.'))
vc = float(input("Digite a velocidade da correnteza: ").replace(',', '.'))

t = tempo_trav(largura, vb)
d = distancia_correnteza(vc, t)

print(f"O barco foi arrastado {d:.2f} metros.")


# Modular

'''

Estrutura dos arquivos
projeto/
│
├── fisica.py
└── main.py

fisica.py → módulo (regras, cálculos)
# fisica.py

def tempo_trav(largura, vb):
    return largura / vb

def distancia_correnteza(vc, t):
    return vc * t

main.py → programa principal
# main.py

from fisica import tempo_trav, distancia_correnteza

print("=== TRAVESSIA DO RIO ===")

largura = float(input("Digite a largura do rio: ").replace(',', '.'))
vb = float(input("Digite a velocidade do barco: ").replace(',', '.'))
vc = float(input("Digite a velocidade da correnteza: ").replace(',', '.'))

t = tempo_trav(largura, vb)
d = distancia_correnteza(vc, t)

print(f"O barco foi arrastado {d:.2f} metros.")


# Decomposição de funções

Exemplo:

A área da coroa circular (anel)
2 círculos de raios r1 e r2 (r1> r2 e pi = 3.14

Se tivesse um problema, teríamos que testar cada un
Divisão de funções

1) Divisão de funções (por que isso existe)

Dividir funções significa separar responsabilidades.

Em vez de uma função grande que faz tudo, você cria:

funções menores

cada uma com uma única tarefa

que podem ser reutilizadas por outras funções

Vantagens práticas:

código mais legível

menos repetição

manutenção mais fácil

menos erro

Isso é padrão em qualquer código profissional.

2) O que é escopo (scope)

Escopo define onde uma variável existe e pode ser usada.

Em Python, existem principalmente:

Escopo local → dentro da função

Escopo global → fora das funções

Escopo local

Parâmetros e variáveis criadas dentro da função

Só existem dentro dela

Outras funções não enxergam

Isso vale mesmo que o nome seja igual em outra função.

3) Funções podem ser usadas várias vezes

Quando você faz:

def soma(a, b):
    return a + b


Essa função:

é definida uma única vez

pode ser chamada quantas vezes quiser

por qualquer outra função

Se você definir duas funções com o mesmo nome, o Python:

descarta a primeira

mantém apenas a última definição

Exemplo real:

def teste():
    print("primeira")

def teste():
    print("segunda")

teste()


Saída:

segunda


4) Parâmetros têm escopo local

Isso é muito importante.

Mesmo que duas funções usem o mesmo nome de parâmetro, elas não compartilham nada.

