import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np   
import community as community_louvain


df = pd.read_csv('Componente.csv')
Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)
degrees = [val for (node, val) in G.degree()]
print("El minimo grado es:", min(degrees))
print("El maximo grado es:", max(degrees))
print("El grado promedio:", sum(degrees)/len(degrees))

#lista = []
#for i in range(len(degrees)):
#    lista.append(i+1)
    
                                                         
#plt.bar(lista,degrees)
#plt.show()
print("La distancia promedio entre los nodos",nx.average_shortest_path_length(G))
print("El diametro de la red es de:", nx.diameter(G))
print("La transitividad es de", nx.transitivity(G))


#centralidad = nx.betweenness_centrality(G)
#c = []
#for key1 in centralidad:
#    c.append(centralidad[key1])

#pagerank= nx.pagerank(G)
#p = []
#for key2 in pagerank:
#    p.append(pagerank[key2])

#plt.xlabel("PageRank")
#plt.ylabel("Centralidad")
#plt.plot(p, c, 'o', color='black')
#plt.show()

#plt.xlabel("PageRank")
#plt.ylabel("Grados")
#plt.plot(p, degrees, 'o', color='black')
#plt.show()

#plt.xlabel("Centralidad")
#plt.ylabel("Grados")
#plt.plot(c, degrees, 'o', color='black')
#plt.show()

print("Core",nx.algorithms.core.k_core(G))
print("Shell",nx.algorithms.core.k_shell(G))
print("Asortatividad de la red",nx.degree_assortativity_coefficient(G))

#############
G1=nx.random_degree_sequence_graph(degrees)
G2=nx.random_degree_sequence_graph(degrees)
G3=nx.random_degree_sequence_graph(degrees)
G4=nx.random_degree_sequence_graph(degrees)
G5=nx.random_degree_sequence_graph(degrees)
G6=nx.random_degree_sequence_graph(degrees)
G7=nx.random_degree_sequence_graph(degrees)
G8=nx.random_degree_sequence_graph(degrees)
G9=nx.random_degree_sequence_graph(degrees)
G10=nx.random_degree_sequence_graph(degrees)


print("La transitividad de G1 es de", nx.transitivity(G1))
print("Core G1",nx.algorithms.core.k_core(G1))

print("La transitividad de G2 es de", nx.transitivity(G2))
print("Core G2",nx.algorithms.core.k_core(G2))

print("La transitividad de G2 es de", nx.transitivity(G3))
print("Core G2",nx.algorithms.core.k_core(G3))

print("La transitividad de G2 es de", nx.transitivity(G4))
print("Core G2",nx.algorithms.core.k_core(G4))

print("La transitividad de G2 es de", nx.transitivity(G5))
print("Core G2",nx.algorithms.core.k_core(G5))

print("La transitividad de G2 es de", nx.transitivity(G6))
print("Core G2",nx.algorithms.core.k_core(G6))

print("La transitividad de G2 es de", nx.transitivity(G7))
print("Core G2",nx.algorithms.core.k_core(G7))

print("La transitividad de G2 es de", nx.transitivity(G8))
print("Core G2",nx.algorithms.core.k_core(G8))

print("La transitividad de G2 es de", nx.transitivity(G9))
print("Core G2",nx.algorithms.core.k_core(G9))

print("La transitividad de G2 es de", nx.transitivity(G10))
print("Core G2",nx.algorithms.core.k_core(G10))
