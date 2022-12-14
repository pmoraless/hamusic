import networkx as nx
import numpy as np

import itertools
from collections import defaultdict

import random
import matplotlib.pyplot as plt
import pandas as pd


def adjList(graph):
    """
    Finds the adjacency list from the graph.
    """

    adjList = [[] for _ in range(graph.number_of_nodes())]
    for (src, dest) in graph.edges():
        adjList[src].append(dest)
        adjList[dest].append(src)
    return adjList

def hampath(graph, v, visited, path, c):
    """
    Find all hamiltonian paths from a starting vertex.
    """

    n = graph.number_of_nodes()
    
    if len(path) == n:
        c.extend(path)
        return
    
    adj_list = adjList(graph)
    
    for w in adj_list[v]:
        if not visited[w]:
            visited[w] = True
            path.append(w)

            hampath(graph, w, visited, path, c)

            visited[w] = False
            path.pop()

def find_all_paths(graph):
    """
    Finds all hamiltonian paths for starting from all possible vertices.
    """

    n = graph.number_of_nodes()
    allpaths = []
    for startV in range(n):
        path = [startV]
        c = []
        visited = [False] * n
        visited[startV] = True
        
        hampath(graph, startV, visited, path, c)
        final = [c[i * n:(i + 1) * n] for i in range((len(c) + n - 1) // n )]
        allpaths.append(final)
        allpathsflat = [item for sublist in allpaths for item in sublist]
    return allpathsflat

def find_hampath(graph):
    """
    Finds all hamiltonian paths. 

    Note: A fully connected graph should be n!
    """
    all_paths = find_hampath(graph)

    #show first 30 paths
    all_paths[:30]

    #print number of paths
    print(len(all_paths))

def parse_path(graph):

    """
    Parses through hamiltonian paths and takes the BPM difference between consecutive songs.

    Returns: Small (<=20) BPM differences, nil otherwise.
    """
    all_paths = find_all_paths(graph)
    good_path = []
    for path in all_paths:
        path_bpm = [graph.nodes[i]['BPM'] for i in path]
        bpm_diff = abs(np.diff(path_bpm))
        if all(i <=20 for i in bpm_diff)==True:
            good_path.append(path)
            print(path, path_bpm)

def parse_two_paths(graph):
    """
    parse through paths

    for this, took the difference of 
    1. bpm between consecutive songs and summed them
    2. danceability b/w songs and summed them
    3. scaled/add weights to both attributes
    4. sum total
    5. sort weight sum, want the LOWEST

    """
    all_paths = find_all_paths(graph)
    good_path = {}
    for path in all_paths[:20]:
        path_bpm = [graph.nodes[i]['BPM'] for i in path]
        path_dance = [graph.nodes[i]['Danceability'] for i in path]
        bpm_diff = abs(np.diff(path_bpm))
        dance_diff = 100*abs(np.diff(path_dance))
        print(bpm_diff, dance_diff)
        path_rating = sum(bpm_diff) + sum(dance_diff)
        good_path[str(path)]= path_rating

    sort_good_path = sorted(good_path.items(), key=lambda x:x[1])
    return sort_good_path

def two_attributes(attribute1, attribute2):
    """
    Provides data for two song attributes.

    Returns: Dictionary of dictionary data frame.
    """
    i_list = list(range(len(all_track_titles)))
    dict1 = list(zip(attribute1, attribute2))
    pd1 = pd.DataFrame(dict1, columns=[attribute1, attribute2], index = i_list)
    df = pd1.to_dict('index')
    return df
