from pyvis.network import Network
import pandas as pd


''' These are some parameter than we can implement in the interface like shape, color, ...'''
node_shape = 'diamond' #image, circularImage, diamond, dot, star, triangle, triangleDown, square and icon
degree_min = 0
list_of_hidden = []



def degree_filtering(max_degree,nodes,network):
    for nd in nodes:
        node_neighbors = network.neighbors(nd["id"])
        if(len(node_neighbors) < max_degree):
            nd["hidden"] = True
            list_of_hidden.append(nd["id"])


got_net = Network(height="750px", width="65%", bgcolor="#222222", font_color="white")
got_net.toggle_physics(True)
got_net.toggle_drag_nodes(True)
got_net.show_buttons(True)
# set the physics layout of the network
got_net.barnes_hut()
#got_data = pd.read_csv("https://www.macalester.edu/~abeverid/data/stormofswords.csv")
got_data = pd.read_csv("Classeur1.csv")
sources = got_data['Source']
targets = got_data['Target']
#weights = got_data['Weight']

edge_data = zip(sources, targets)#, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    #w = e[2]

    got_net.add_node(src, src, title=src,shape=node_shape,hidden=False)
    got_net.add_node(dst, dst, title=dst,shape=node_shape,hidden=False)
    got_net.add_edge(src, dst, value=1,hidden=False)


degree_filtering(degree_min,got_net.nodes,got_net)
for edg in got_net.edges:
    if edg["from"] in list_of_hidden:
        edg["hidden"] = True
    
    if edg["to"] in list_of_hidden:
        edg["hidden"] = True
        
    
got_net.set_edge_smooth('curvedCW')
neighbor_map = got_net.get_adj_list()



# add neighbor data to node hover data
for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])
    



got_net.show("mon_graph.html")

