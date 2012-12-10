def simple(node):
    """
    chooses a random edge and returns the action that
    represents an increase of its weight, according to the budget.
	returns a request for increasing the weight of 
	edge e in the amount of the total budget
    """
    n = random.shuffle(node.neighborhood)[0] 
    e = (node ? n).pop() # take the edge linking 'node' to 'n'
    return {e: node.budget}

def get(name):
    #TODO FIXME