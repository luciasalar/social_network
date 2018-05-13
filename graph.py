import csv
import networkx as nx
from operator import itemgetter
import community #This is

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
nx.shortest_path(G, 'A', 'D', weight='weight')



with open('quakers_nodelist.csv', 'r') as nodecsv: # Open the file                       
    nodereader = csv.reader(nodecsv) # Read the csv  
    # Retrieve the data (using Python list comprhension and list slicing to remove the header row, see footnote 3)
    nodes = [n for n in nodereader][1:]                     

    node_names = [n[0] for n in nodes] # Get a list of only the node names                                       

with open('quakers_edgelist.csv', 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv     
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data


G = nx.Graph()

G.add_nodes_from(node_names)
G.add_edges_from(edges)

print(nx.info(G))

#create empty dict as nodes
hist_sig_dict = {}
gender_dict = {}
birth_dict = {}
death_dict = {}
id_dict = {}

#set the dict as nodes
for node in nodes: # Loop through the list, one row at a time
    hist_sig_dict[node[0]] = node[1]
    gender_dict[node[0]] = node[2]
    birth_dict[node[0]] = node[3]
    death_dict[node[0]] = node[4]
    id_dict[node[0]] = node[5]


#add attributes to node
nx.set_node_attributes(G, values = hist_sig_dict, name= 'historical_significance')
nx.set_node_attributes(G, values= gender_dict, name= 'gender')
nx.set_node_attributes(G, values= birth_dict, name='birth_year')
nx.set_node_attributes(G, values= death_dict, name='death_year')
nx.set_node_attributes(G, values= id_dict, name='sdfb_id')


for n in G.nodes(): # Loop through every node, in our data "n" will be the name of the person
    print(n, G.node[n]['birth_year']) # Access every node by its name, and then by the attribute "birth_year"














