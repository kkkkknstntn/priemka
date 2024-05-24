import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from math import log

def make_complete_graph(n):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(all_pairs(nodes))
    return G

def all_pairs(nodes):
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i > j:
                yield u, v

def random_pairs(nodes, p):
    for edge in all_pairs(nodes):
        if flip(p):
            yield edge

def flip(p):
    return np.random.random() < p

def make_random_graph(n, p):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(random_pairs(nodes, p))
    return G

def _random_subset(repeated_nodes, k):
    targets = set()
    while len(targets) < k:
        x = np.random.choice(repeated_nodes)
        targets.add(x)
    return targets

def barabasi_albert_graph(n, k):
      G = nx.complete_graph(k)
      targets = list(range(k))
      repeated_nodes = []
      for source in range(k, n):
        G.add_edges_from(zip([source]*k, targets))
        repeated_nodes.extend(targets)
        repeated_nodes.extend([source] * k)
        targets = _random_subset(repeated_nodes, k)
      return G

def bollobas_riordan_graph(n,k):
    ba1=barabasi_albert_graph(n*k,1)
    G= nx.empty_graph(n)
    for i in ba1.edges():
        if (i[0]//k != i[1]//k):
         G.add_edge(i[0]//k,i[1]//k)
    return G

def degrees(G,n):
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    return degree_sequence

def sum_degrees(G,n):
    arr = [0] * n
    for i in range(n):
        for j in G.neighbors(i):
            arr[i]+=G.degree(j)
    return arr

n =10
er = make_random_graph(n,0.3)
ba=barabasi_albert_graph(n,10)
bl=bollobas_riordan_graph(n,10)

nx.draw_circular(er,
      node_color="red",
      node_size=1000,
      with_labels=True)
plt.show()
"""
nx.draw_circular(ba,
      node_color="blue",
      node_size=1000,
      with_labels=True)
plt.show()


nx.draw_circular(bl,
      node_color="yellow",
      node_size=1000,
      with_labels=True)
plt.show()
"""
er_deg_uniq=np.unique(degrees(er, n), return_counts=True)
ba_deg_uniq=np.unique(degrees(ba, n), return_counts=True)
bl_deg_uniq=np.unique(degrees(bl, n), return_counts=True)

er_sum_deg=sum_degrees(er,n)
ba_sum_deg=sum_degrees(ba,n)
bl_sum_deg=sum_degrees(bl,n)

er_deg=[er.degree(i) for i in range(n)]
ba_deg=[ba.degree(i) for i in range(n)]
bl_deg=[bl.degree(i) for i in range(n)]

plt.figure()
plt.grid(True)
plt.xlabel(r'$d_i$')
plt.ylabel(r'$s_i$')
plt.title("Зависимость суммы степеней соседей от степени вершины")
plt.scatter(er_deg,er_sum_deg,s=1,label='Эрдеша-Реньи')
plt.scatter(ba_deg,ba_sum_deg,s=1,label='Барабаши-Альберт')
plt.scatter(bl_deg,bl_sum_deg,s=1,label='Боллобаша-Риордана')
plt.legend()
plt.show()

plt.figure()
plt.grid(True)
plt.xlabel(r'$d_i$')
plt.ylabel(r'$a_i$')
plt.title("Зависимость среднец суммы степеней соседей  от степени вершины")
plt.scatter(er_deg,[er_sum_deg[i]/er_deg[i] for i in range(n)],s=1,label='Эрдеша-Реньи')
plt.scatter(ba_deg,[ba_sum_deg[i]/ba_deg[i] for i in range(n)],s=1,label='Барабаши-Альберт')
plt.scatter(bl_deg,[bl_sum_deg[i]/bl_deg[i] for i in range(n)],s=1,label='Боллобаша-Риордана')
plt.legend()
plt.show()

plt.figure()
plt.grid(True)
plt.title("Зависимость индекса дружбы от степени вершины")
plt.xlabel(r'$d_i$')
plt.ylabel(r'$b_i$')
plt.scatter(er_deg,[er_sum_deg[i]/er_deg[i]/er_deg[i] for i in range(n)],s=1,label='Эрдеша-Реньи')
plt.scatter(ba_deg,[ba_sum_deg[i]/ba_deg[i]/ba_deg[i] for i in range(n)],s=1,label='Барабаши-Альберт')
plt.scatter(bl_deg,[bl_sum_deg[i]/bl_deg[i]/bl_deg[i] for i in range(n)],s=1,label='Боллобаша-Риордана')
plt.legend()
plt.show()

plt.figure()
plt.grid(True)
plt.title("Распределение степеней вершин")
plt.xlabel(r'$d_i$')
plt.plot(*er_deg_uniq, 'b-',label='Эрдеша-Реньи')
plt.plot(*ba_deg_uniq, 'r-',label='Барабаши-Альберт')
plt.plot(*bl_deg_uniq, 'g-',label='Боллобаша-Риордана')
plt.legend()
plt.show()

plt.figure()
plt.grid(True)
plt.title("Распределение степеней вершин")
plt.xlabel(r'$log(d_i)$')
print([log(i) for i in er_deg_uniq[0]])
plt.plot([log(i) for i in er_deg_uniq[0]], [log(i) for i in er_deg_uniq[1]],label='Эрдеша-Реньи')
plt.plot([log(i) for i in ba_deg_uniq[0]], [log(i) for i in ba_deg_uniq[1]],label='Барабаши-Альберт')
plt.plot([log(i) for i in bl_deg_uniq[0]], [log(i) for i in bl_deg_uniq[1]],label='Боллобаша-Риордана')
plt.legend()
plt.show()



