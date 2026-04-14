# Starter Code for Python Data Structures Assignment

# Task 1: Trabalhando com Listas e Dicionários

# Lista de alunos
alunos = []

# Dicionário para notas: chave = nome do aluno, valor = lista de notas
notas = {}

# Exemplo: Adicionar um aluno
# alunos.append("João")
# notas["João"] = [8.5, 9.0, 7.5]

# Função para calcular média
def calcular_media(notas_aluno):
    if notas_aluno:
        return sum(notas_aluno) / len(notas_aluno)
    return 0

# Task 2: Usando Sets e Tuplas

# Set para remover duplicatas
numeros = [1, 2, 2, 3, 4, 4, 5]
numeros_unicos = set(numeros)

# Tuplas para pontos
ponto1 = (0, 0)
ponto2 = (3, 4)

# Função para calcular distância
import math
def distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Exemplo de uso
# print("Números únicos:", numeros_unicos)
# print("Distância:", distancia(ponto1, ponto2))