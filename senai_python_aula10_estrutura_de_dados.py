# -*- coding: utf-8 -*-
"""senai_python_aula10_Estrutura_De_DADOS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HCKQctEdhS2GPtxuFOuA8IL7NHO4WbVz

## Bubble Sort
"""

def bubble_sort(lista):
  n = len(lista)
  for i in range(n):
    for j in range(0, n-i-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
        print(f"Troca: {lista}")
    print(f"Passada {i+1}: {lista}")
  return lista

lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_exemplo}")
print(f"\nOrdenando...\n")
lista_ordenada = bubble_sort(lista_exemplo)
print(f"\nLista ordenada: {lista_ordenada}")

"""## Insert Sort"""

def insert_sort(lista):
  for i in range(1, len(lista)):
    chave = lista[i]
    j = i-1
    while j >= 0 and chave < lista[j]:
      lista[j+1] = lista[j]
      j -= 1
      print(f"Movimentacao: {lista}")
    lista[j+1] = chave
    print(f"Insercao {i}: {lista}")
  return lista

lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_exemplo}")
print(f"\nOrdenando...\n")
lista_ordenada = insert_sort(lista_exemplo)
print(f"\nLista ordenada: {lista_ordenada}")

"""## Select Sort"""

def select_sort(lista):
  for i in range(len(lista)):
    min = i
    for j in range(i+1, len(lista)):
      if lista[min] > lista[j]:
        min = j
    lista[i], lista[min] = lista[min], lista[i]
    print(f"Troca {i+1}: {lista}")
  return lista

lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_exemplo}")
print(f"\nOrdenando...\n")
lista_ordenada = select_sort(lista_exemplo)
print(f"\nLista ordenada: {lista_ordenada}")

"""## Merge Sort"""

def merge_sort(lista):
  if len(lista) > 1:
    meio = len(lista)//2
    esquerda = lista[:meio]
    direita = lista[meio:]
    merge_sort(esquerda)
    merge_sort(direita)
    i = j = k = 0
  while i < len(esquerda) and j < len(direita):
    if esquerda[i] < direita[j]:
      lista[k] = esquerda[i]
      i += 1
    else:
      lista[k] = direita[j]
      j += 1
    k += 1

    while i < len(esquerda):
      lista[k] = esquerda[i]
      i += 1
      k += 1

    while j < len(direita):
      lista[k] = direita[j]
      j += 1
      k += 1
  return lista

lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_exemplo}")
print(f"\nOrdenando...\n")
lista_ordenada = select_sort(lista_exemplo)
print(f"\nLista ordenada: {lista_ordenada}")