class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict =gdict
    
    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self):
        return self.findEdges()
    
    def findEdges(self):
        edges=[]
        

graph_elements = {
    "a" : ["b","c"],
    "b" : ["a","d"],
    "c" : ["a","d"],
    "d" : ["c","b"],
    "e" : ["d"]
}

g= graph(graph_elements)

print (g.getVertices())