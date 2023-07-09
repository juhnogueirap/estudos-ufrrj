# -*- coding: utf-8 -*-
"""BFS8puzzle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RTLC8_uXtb5zz5T2aC8nPduRvBBcu1Ao
"""

from google.colab import drive
drive.mount('/content/drive')

import copy
from collections import deque

tabuleiro = [[0, 8, 7],
             [6, 5, 4],
             [3, 2, 1]]
##node = tabuleiro


dicionario = {
  (0,0): ["Right", "Down"],
  (0,1): ["Right", "Down", "Left"],
  (0,2): ["Left", "Down"],
  (1,0): ["Up", "Right", "Down"],
  (1,1): ["Left", "Up", "Right", "Down"],
  (1,2): ["Up", "Left", "Down"],
  (2,0): ["Up", "Right"],
  (2,1): ["Left", "Up", "Right"],
  (2,2): ["Left", "Up"]}

class Node:

  def __init__(self, node_estado, node_pai, acao, custoCaminho, caminho):


    self.node_estado = node_estado
    self.node_pai = node_pai
    self.acao = acao
    self.custoCaminho = custoCaminho
    self.caminho = [acao]

    if node_pai is not None:
      self.caminho.extend(node_pai.caminho)

def geraEstados(node):
#a partir do nó (matriz) dada, matrizes

  #posicaoZero recebe tupla indicando a posiçao do zero na matriz
  posicaoZero = buscaZero(node)
  movPossiveis = dicionario[posicaoZero]
  #lista de matrizes possiveis
  matrizesPossiveis = []


  for acao in movPossiveis:
    #copia matriz original
    copiaMatriz = copy.deepcopy(node.node_estado)

    ##para cada movimento, altero a matriz
    #as matrizes possiveis sao armazenadas na lista de matrizes possiveis
    if(acao == "Right"):
      novaMatriz = movimentaRight(copiaMatriz, posicaoZero)
      matrizesPossiveis.append((novaMatriz, acao))
      node.caminho.append(acao)
    if(acao == "Down"):
      novaMatriz = movimentaDown(copiaMatriz, posicaoZero)
      matrizesPossiveis.append((novaMatriz, acao))
      node.caminho.append(acao)
    if(acao == "Up"):
      novaMatriz = movimentaUp(copiaMatriz, posicaoZero)
      matrizesPossiveis.append((novaMatriz, acao))
      node.caminho.append(acao)
    if(acao == "Left"):
      novaMatriz = movimentaLeft(copiaMatriz, posicaoZero)
      matrizesPossiveis.append((novaMatriz, acao))
      node.caminho.append(acao)
  return matrizesPossiveis


def buscaZero(node):
#retorna tupla com a posicao do 0 na matriz

  for i in range(len(node.node_estado)):
    for j in range(len(node.node_estado[0])):
      if(node.node_estado[i][j] == 0):
        return i, j

def movimentaRight(matriz, posicaoZero):
  matriz[posicaoZero[0]][posicaoZero[1]], matriz[posicaoZero[0]][posicaoZero[1]+1] = matriz[posicaoZero[0]][posicaoZero[1]+1], matriz[posicaoZero[0]][posicaoZero[1]]
  return matriz

def movimentaLeft(matriz, posicaoZero):
  matriz[posicaoZero[0]][posicaoZero[1]], matriz[posicaoZero[0]][posicaoZero[1]-1] = matriz[posicaoZero[0]][posicaoZero[1]-1], matriz[posicaoZero[0]][posicaoZero[1]]
  return matriz

def movimentaUp(matriz, posicaoZero):
  matriz[posicaoZero[0]][posicaoZero[1]], matriz[posicaoZero[0]-1][posicaoZero[1]] = matriz[posicaoZero[0]-1][posicaoZero[1]], matriz[posicaoZero[0]][posicaoZero[1]]
  return matriz

def movimentaDown(matriz, posicaoZero):
  matriz[posicaoZero[0]][posicaoZero[1]], matriz[posicaoZero[0]+1][posicaoZero[1]] = matriz[posicaoZero[0]+1][posicaoZero[1]], matriz[posicaoZero[0]][posicaoZero[1]]
  return matriz

def transformaMatrizTupla(matriz):
  tupla = tuple(map(tuple, matriz))
  return tupla

def buscaEmLargura(estadoInicial):

  noRaiz = Node(estadoInicial, None, None, 0, [])
  if(testaObjetivo(estadoInicial)):
    return noRaiz
  borda = deque()
  borda.append(noRaiz)
  explorado = set()
  explorado.add(transformaMatrizTupla(noRaiz.node_estado))
  while borda:
    noRaiz = borda.popleft()
    explorado.add(transformaMatrizTupla(noRaiz.node_estado))

    matrizesPossiveis = geraEstados(noRaiz)
    for estados in matrizesPossiveis:
      novoNo = Node(estados[0], noRaiz, estados[1], (noRaiz.custoCaminho + 1), noRaiz.caminho)
      if(transformaMatrizTupla(novoNo.node_estado)) not in explorado:
        if(testaObjetivo(novoNo.node_estado)):
          return novoNo
        borda.append(novoNo)
  return None

def testaObjetivo (matriz):

  matrizGoal = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]

  if len(matriz) != len(matrizGoal) or len(matriz[0]) != len(matrizGoal[0]):
    return False

  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if matriz[i][j] != matrizGoal[i][j]:
        return False

  return True

a = buscaEmLargura([[0, 8, 7],
             [6, 5, 4],
             [3, 2, 1]])
caminho = a.caminho[::-1]
print(a.node_estado)
print(caminho)
print(a.custoCaminho)

!jupyter nbconvert --to pdf /content/drive/MyDrive/ColabNotebooks/BFS8puzzle.ipynb