'''

# Áres do quadrado:

import math

def areaQuadrado(l):
    # Usando a função da biblioteca
    return msth.pow(l,2)

# E a pirâmide calcular?

def piramQ(ab,h):
    # Função que calcula volume de uma pirãmide
    # Dada as arestas ab e altura h
    return (1/3) * areaQuadrado(ab) * h


'''

'''
dado dois angulos B e C , em graus , e a medida AC, do lado oposto
do ãngulo B de um triângulo, defina uma função que utilize a lei dos
senos para calcular os demais lados (AB, BC) do mesmo triângulo
'''
from math import*
def leiDosSenos(B,C,AC):
    """ Função que calcula os demais lados do triângulo
      dados dois Ângulos B e C em graus e um segmento AC"""
    A = 180 - B - C
    AB = sin(radians(C))/ sin(radians(B))* AC
    BC = sin(radians(A)) / sin(radians(B))*AC
    return AB,BC

# sin calcula o seno de um valor
# Para isso ser feito deve estar medido em radianos
# Mas no nosso exemplo está sendo pedido em graus
# O que fazer? Converter graus em radianos com a função
# sin(radians(x))

