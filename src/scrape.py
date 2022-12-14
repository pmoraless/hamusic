"""
Scrape is the data scraping and visualization tool of Hamusic.
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import config
import networkx as nx
import itertools
import numpy as np
# Import revelant libraries

all_track_data = []
track_danceability = []
track_energy = []
track_key = []
track_loudness = []
track_speechiness = []
track_acousticness = []
track_instrumentalness = []
track_liveness = []
track_valence = []
track_tempo = []
track_timesig = []
track_dur_min = []
all_track_titles = []
# Create revelant lists to hold data
client_credentials_manager = SpotifyClientCredentials(config.CLIENT_ID, config.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# Authenticate
results = sp.playlist_tracks("4NdZwQEEKF3cTKnB30lti1")
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])
# Scrape entire playlist from Spotify
track_uris = [x["track"]["uri"] for x in tracks]
# Pull track URI data from database playlist
for string in track_uris:
    all_track_data.append(sp.audio_features(string[14:]))
# Aggregate all track data
for dictionary in all_track_data:
    track_danceability.append(int(dictionary[0]["danceability"]*100))
    track_energy.append(dictionary[0]["energy"])
    track_key.append(dictionary[0]["key"])
    track_loudness.append(dictionary[0]["loudness"])
    track_speechiness.append(dictionary[0]["speechiness"])
    track_acousticness.append(dictionary[0]["acousticness"])
    track_instrumentalness.append(dictionary[0]["instrumentalness"])
    track_liveness.append(dictionary[0]["liveness"])
    track_valence.append(dictionary[0]["valence"])
    track_tempo.append(int(dictionary[0]["tempo"]))
    track_timesig.append(dictionary[0]["time_signature"])
    track_dur_min.append(int(dictionary[0]["duration_ms"])/60000)
    # Divide by 60,000 to convert ms to min
for track in tracks:
    all_track_titles.append(track["track"]["name"])
    # Find categorical data on songs to aid in ease of data analysis
# Sort all data into lists for numpy
all_track_chars = []
# Create list for compiling
all_track_chars.append(all_track_titles)
all_track_chars.append(track_danceability)
all_track_chars.append(track_energy)
all_track_chars.append(track_key)
all_track_chars.append(track_loudness)
all_track_chars.append(track_speechiness)
all_track_chars.append(track_acousticness)
all_track_chars.append(track_instrumentalness)
all_track_chars.append(track_liveness)
all_track_chars.append(track_valence)
all_track_chars.append(track_tempo)
all_track_chars.append(track_timesig)
all_track_chars.append(track_dur_min)
# Compile all lists together for CSV conversion
df = pd.DataFrame(columns = all_track_chars)
df.to_csv('playlist.csv')

##########################################################
# A collection of functions for track data visualization #
##########################################################

border_ys = []
border_xs = []
CURR_X = -10
for _ in range(0, 44):
    border_ys.append(-14)
    border_xs.append(CURR_X)
    CURR_X += 5
# Create lists for border line in loudness scatterplot

def createEdges(dfRawData):
    """
    Create edges for relevant path
    
    Returns:
        Data frame of all of the graph edges
    """
    allEdgesdf = pd.DataFrame(
        data=list(itertools.combinations(dfRawData.index.tolist(), 2)), 
        columns=['Src', 'Dst'])
    return allEdgesdf

def calcEdges(dfEdges, dfRawData):
    """
    Creates all of the edges in the graph
    
    Returns:
        An indexed data frame of the edges
    """
    calc_dfEdges = dfEdges.copy()
    for i, row in dfEdges.iterrows():
        w = 0
        start = row['Src']
        end = row['Dst']
        dBPM = np.abs(dfRawData.iloc[start]['BPM']-dfRawData.iloc[end]['BPM'])
        dDance = np.abs(dfRawData.iloc[start]['Danceability']-dfRawData.iloc[end]['Danceability'])
        calc_dfEdges.at[i,'dBPM'] = dBPM
        calc_dfEdges.at[i,'dDance'] = dDance
        
        if dBPM <= 25:
            w+=1
        if dDance <=0.5:
            w+=1
        calc_dfEdges.at[i,'weight'] = w
        relevantEdges = calc_dfEdges[calc_dfEdges['weight']>0]
    return relevantEdges

def create_bpm():
    """
    Create a beats per minute hamiltonian graph

    Returns:
        A relevant matplotlib graph
    """
    i_list = list(range(len(all_track_titles)))
    dict1 = list(zip(track_tempo))
    pd1 = pd.DataFrame(dict1, columns=['BPM'], index = i_list)
    dftest = pd1.to_dict('index')
    df_i = list(dftest.keys())
    g1 = nx.Graph()
    g1.add_nodes_from(df_i)
    g1.add_edges_from(itertools.combinations(df_i, 2))

    bpm_label = list(["BPM"] * len(all_track_titles))
    i_list = list(range(len(all_track_titles)))
    nx.set_node_attributes(g1, dftest)

    pos = nx.spring_layout(g1, k = 30)
    nx.draw(g1, with_labels=True, width = 0.2, font_size = 4, font_weight='bold', node_color = 'lightblue', node_size = 500)
    node_labels = nx.get_node_attributes(g1,'BPM')
    nx.draw_networkx_labels(g1, pos, labels = node_labels, font_size = 10, verticalalignment='baseline')
    plt.show()

def create_bpm_dance():
    """
    Create a beats per minute and danceability hamiltonian graph

    Returns:
        A relevant matplotlib graph
    """

    i_list = list(range(len(all_track_titles)))
    dict2 = list(zip(track_tempo, track_danceability))
    pd2 = pd.DataFrame(dict2, columns=['BPM', 'Danceability'], index = i_list)
    dftest = pd2.to_dict('index')
    df_i = list(dftest.keys())

    g2 = nx.Graph()
    g2.add_nodes_from(df_i)
    g2.add_edges_from(itertools.combinations(df_i, 2))
    nx.set_node_attributes(g2, dftest)

    pos = nx.spring_layout(g2, k = 100)
    nx.draw(g2, with_labels=True, width = 0.2, font_size = 4, font_weight='bold', node_color = 'lightblue', node_size = 500)
    nx.draw_networkx_labels(g2, pos,labels = dftest, font_size = 6, verticalalignment='baseline')
    plt.show()

def create_bpm_dance_key():
    """
    Create a beats per minute, danceability, and key hamiltonian graph.

    Returns:
        A relevant matplotlib graph
    """

    i_list = list(range(len(all_track_titles)))
    dict3 = list(zip(track_tempo, track_danceability, track_key))
    pd3 = pd.DataFrame(dict3, columns=['BPM', 'Danceability', 'Key'], index = i_list)
    dftest = pd3.to_dict('index')
    df_i = list(dftest.keys())

    g3 = nx.Graph()
    g3.add_nodes_from(df_i)
    g3.add_edges_from(itertools.combinations(df_i, 2))
    nx.set_node_attributes(g3, dftest)

    pos = nx.spring_layout(g3, k = 100)
    nx.draw(g3, with_labels=True, width = 0.2, font_size = 4, font_weight='bold', node_color = 'lightblue', node_size = 500)
    nx.draw_networkx_labels(g3, pos,labels = dftest, font_size = 6, verticalalignment='baseline')
    plt.show()

def create_edge_graph():
    """
    Generate edges and find metrics for different song characteristics
    
    Returns:
        A relevant Matplotlib graph
    """
    i_list = list(range(len(all_track_titles)))
    dict3 = list(zip(track_tempo, track_danceability, track_key))
    pd3 = pd.DataFrame(dict3, columns=['BPM', 'Danceability', 'Key'], index = i_list)
    dftest = pd3.to_dict('index')

    pdTEST = pd3.copy()
    ex_dfEdges = createEdges(pdTEST)

    dfGraph = calcEdges(ex_dfEdges, pdTEST)

    GG = nx.from_pandas_edgelist(dfGraph, 'Src', 'Dst', ['weight'])

    pos = nx.spring_layout(GG)
    # nx.draw_networkx(G,pos)
    # labels = nx.get_edge_attributes(G,'weight')
    # nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    nx.draw(GG, pos, with_labels=True, font_weight='bold', font_size = 4, node_size = 500)
    # nx.draw_networkx_labels(GG, pos,labels = dftest)
    weight_labels = nx.get_edge_attributes(GG,'weight')
    nx.draw_networkx_edge_labels(GG,pos,edge_labels=weight_labels)
    plt.show()


def create_all_graphs():
    """
    Creates all relevant graphs

    Returns:
        All relevant matplotlib graphs
    """
    return create_bpm(), create_bpm_dance(), create_bpm_dance_key()