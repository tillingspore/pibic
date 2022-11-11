import networkx as nx
import matplotlib.pylab as plt


"""
rede de pequeno mundo
modelo watts-strogatz

n :numero de nós
m :quantidade de conexões por nó
p :ordem e aleatoriedade



"""

g = nx.watts_strogatz_graph(n=30,k=30,p=.000001)


pos = nx.circular_layout(g)

plt.figure(figsize=(12,12))
nx.draw_networkx(g,pos)

plt.show()