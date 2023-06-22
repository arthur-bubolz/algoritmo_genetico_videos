"""
Autor Original: Victor Barros Coch Adaptado de SomaTarget.py
Trabalho - Problema dos Vídeos
Alunos: Arthur Bubolz, Gabriel Martins, Andre Maurell
"""
from matplotlib import pyplot as plt
from genetic2022 import *
from bruteforce import *
import time

#Definindo videos possiveis (duração,likes)
videos = [(8, 160), (15, 476), (8, 190), (5, 349), (13, 69), (10, 276), (11, 158), (13, 123), (5, 151), (5, 466), (7, 411), (6, 78), (7, 385), (2, 433), (11, 359), (13, 383), (13, 304), (11, 479), (9, 215), (10, 454), (3, 77), (9, 226), (10, 346), (8, 145), (11, 287), (4, 470), (13, 317), (10, 222), (12, 417), (12, 105), (4, 245), (9, 112), (13, 356), (3, 157), (7, 42), (8, 189), (3, 176), (3, 218), (13, 463), (12, 443), (11, 204), (9, 404), (14, 279), (15, 304), (15, 350), (10, 126), (10, 432), (13, 358), (5, 498), (6, 439)]

#Numero de intens
n_videos = len(videos)
print("Nro de itens: "+str(n_videos)) #Peso maximo da mochila
tempo_max = 300

#Calcula valor de validacao com brute force
#t0 = time.time()
#best = run_bruteforce(videos, tempo_max)
#t1 = time.time()
#print("Tempo Brute force: "+str(t1-t0))
t0 = time.time()

#Tamanho da populacao
p_count = 100

#Criando a populacao
p = population(p_count , n_videos)

#Numero de geracoes para testar
epochs = 1500

#Salva fitness para referencia
media = media_fitness(p, videos, tempo_max)
best_f = best_fitness(p, videos, tempo_max)
fitness_history = [[media[0]],[media[1]],[best_f[0]],[best_f[1]]] # med fitness|med peso|best fitness|bets peso

for i in range(epochs):
    p = evolve(p, videos , tempo_max)
    media = media_fitness(p, videos, tempo_max)
    best_f = best_fitness(p, videos, tempo_max)
    fitness_history[0].append(media[0])
    fitness_history[1].append(media[1])
    fitness_history[2].append(best_f[0])
    fitness_history[3].append(best_f[1])

t1 = time.time()

#print("Individuo Brute Force: "+str(best[1])+", Valor: "+str(best[0]))

print("Tempo AG: "+str(t1-t0))

print("Individuo AG: "+str(sorted(p, key=lambda p:p[0])[-1])+", Valor: " +str(fitness_history[2][-1]))

fig = plt.figure()
ax = plt.axes()

ax.plot(fitness_history[0])
ax.plot(fitness_history[2])
ax.plot(fitness_history[1])
ax.plot(fitness_history[3])

ax.legend(["Fitness Media", "Melhor Fitness", " Peso Medio (x10)", "Peso do Melhor (x10)"])

ax.grid(True)
plt.show()
