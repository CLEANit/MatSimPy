---
title: Graph Functions
layout: default
filename: Graph.md
excerpt: Documentation on the NetworkX graph functions of this project.
nav_order: 3
nav_exclude: false
search_exclude: false
---

### graph.py    -->    Graph methods

**Func init_graph_from_atm** <br> Initializes an unconnected, undirected graph from a provided ASE atoms object.

**Func c_subgraph_finder** <br> Takes a graph and returns every connected subgraph it has. Adapted from resource [here](https://stackoverflow.com/questions/54440779/how-to-find-all-connected-subgraph-of-a-graph-in-networkx)

**Func graph_visual** <br> Produces a labelled matplotlib visualization of a nx graph object.

**Func gdegree** <br> Obtains an array counting degrees of nodes present in graph G. Similar but distinct from the G.degree already present in the nx package.
