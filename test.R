library("igraph")
print("ok")


net <- graph_from_data_frame(d=links, vertices=nodes, directed=T) 
net