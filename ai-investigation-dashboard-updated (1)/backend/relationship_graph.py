
def build_graph(messages):

edges={}

for m in messages:
    sender=m["sender"]

    if sender not in edges:
        edges[sender]=0

    edges[sender]+=1

return edges
