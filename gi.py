"""
abstraction for access to graph ('g'). So that the specific implementation is somewhat isolated
and that we don't have to handle complicated type conversions in our code.
"""
from config import g
import random

def nodes():
    """
    returns the graph's nodes
    """
    return [ node 
             for node 
             in g().nodes 
             if node is not None 
    ]

def edges():
    """
    returns the graph's edges
    """
    return [ e 
            for e 
            in g().edges 
            if e is not None 
            and hasattr(e,'source')
            and hasattr(e,'target')
    ]

def alive_edges():
    """
    return a list of edges that have not been killed
    """
    return [ e for e in edges() if e.weight != 0 ]

def num_edges():
    """
    returns the how many edges are there
    """
    return len(edges())
    
def neighbors(node):
    """
    returns the neighbors of a node
    """
    ret = []
    for n in node.neighbors:
        if n is not None:
            ret.append(n)
    return ret
    
def random_neighbor(node):
    """
    returns a randomly selected node from
    the node's neighborhood
    """
    tmp = neighbors(node)
    random.shuffle(tmp)

    for n2 in tmp:
        # checking that an edge is actually there
        if has_edge(n2,node):
            return n2

    raise Exception("no neighbor found!")

def random_edges(how_many,only_alive=False): # FIXME: more elegant than parametrized?? Boh!
    """ 
    returns some edges, randomly selected
    """
    how_many = min(how_many,num_edges())

    pool = None
    if only_alive:
        pool = alive_edges()
    else:
        pool = edges()

    ret=random.sample(pool,how_many)
    return ret

def kill_edge(e):
    print "killing edge "+str(e)+" -- "+str(e.getEdge())
    g().underlyingGraph.readUnlockAll()
    set_weight(e, 0.0)

def add_weight(e,increase):
    set_weight(e,get_weight(e) + increase)

def set_weight(e,weight):
    e.getEdge().getEdgeData().setWeight(weight)

def get_weight(e):
    return e.weight

def mult_weight(e, factor):
    set_weight(e, get_weight(e) * factor)
 
def has_edge(n1,n2):
    e = (n1 ? n2).pop() # take the edge linking 'node' to 'n'
    return False if e is None else True

def get_edge(n1,n2):
    e = (n1 ? n2).pop() # take the edge linking 'node' to 'n'
    if e is None:
        raise Exception("gi.get_edge("+str(n1)+","+str(n2)+") did not find the edge")
    return e

