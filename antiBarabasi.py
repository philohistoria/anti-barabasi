import itertools
import random
import math
import networkx as nx
from networkx.generators.classic import empty_graph, path_graph, complete_graph

from collections import defaultdict
def prob_subset(G,m):
    result = set()
    choices = [(x,1.0/G.degree(x)) for x in G.nodes()]
    total = sum(w for c,w in choices)

    upto = 0
    while len(result)<m:
        for c,w in choices:
            if upto+w >total:
                result.add(c)
            upto += w

    return list(result)


def anti_barabasi(n,m):
    G = complete_graph(m)
    #target nodes for new nodes
    targets = list(range(m))
    new = m#initialize = m
    while new < n:
        G.add_edges_from(zip([new]*m,targets))#add m edge together
        targets = prob_subset(G,m)
        new += 1
    return G


    
def main():
    g = anti_barabasi(20,5)
    print g.nodes()
    print g.edges()    
if __name__ == '__main__':
        main()