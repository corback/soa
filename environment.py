import random
import copy

# local imports
import config

e=(n ? curr)



import random
import copy


config = {
    'frac_edges': 0.1,
    'frac_damage': 0.65,
    'factor_reuse': 0.25,
    'policy_id': 'simple',
	'init_num_nodes': len(g.nodes)
}


#TODO: Policy_shortpath
#TODO: Policy_prorich
#TODO: Policy_propoor
#TODO: Policy_proheavy
#TODO: Policy_prolight
#TODO: Policy_proweightrich
#TODO: Policy_proweightpoor
def environment():
    """ actions performed by the environment
        Alzeihmer desease:
        select randomly a certain percentage of edges. 
        The weights of the edges will be reduced
        of a certain percentage
    """
    import math
    edges_copy = copy.copy(g.edges)
    num_edges_selected = int(math.ceil(len(edges_copy) * config['frac_edges'] ))
    selected=random.sample(g.edges,num_edges_selected)
    damaged = set()
    for e in selected: # each of these edges will be assigned a damage
        prev_weight = e.weight
        e.weight = prev_weight * config['frac_damage']
        diff = prev_weight - e.weight
        e.damage = diff # if the edge is too light, destroy it
        if e.weight < 1.0: #del e # FIXME!! careful!!!
		    print e
    damaged.add(e)
    return damaged

def budgetize(damaged):
    """
    generates budgets for the nodes involved in the damaged edges.
	As some weight is removed, a part of this weight is given as a budget to the involved nodes.
	This weight can then be applied to strengtehn other nodes' edges. (this is done by the 'behaviour' func)
	the overall idea: some of the weight is lost, some is 'shifted' to other edges
    """
    for e in damaged: # reset previous budgets. each cycle is a new story!
        e.source.budget = 0
        e.target.budget = 0
    for e in damaged: # a fraction of the edge's removed-weight becomes edges budget
        budget = e.damage * config['factor_reuse']
        e.source.budget += budget 
        e.target.budget += budget

def apply_actions(self,actions):
    for e,increase in actions.items():
        self.budget -= increase
        if self.budget < 0.0:
            raise Exception("programming error: budget can not be < 0.0")
        e.weight += increase

def behaviour(self):
    """
    behavior of the node agent:
    select one (or more?) of its edges to be reinforced,
	according to the node's budget. budget itself is a fraction 
	of the damage inflicted to the nodes' edgess
    """
    actions = policies[config['policy_id']](self)
    apply_actions(self,actions)
		
def wakeup_nodes(damaged):
    """
    wakes up the affected nodes for action. this will call 'behaviour'
    """
    waking_nodes = set()
    for e in damaged:
	waking_nodes.add(e.source)
	waking_nodes.add(e.target)
    for node in waking_nodes:
        node.behavior() # the action is defined there...!!FIXME!!at moment bheaviour is not a method for node


def termination_condition():
    for e in g.edges:
	if len(g.nodes)<config['init_num_nodes']:
		return True
    return False

def snapshot():
    pass #TODO statistics, screenshot, indicators calculations...

def step(): # what happens in each cycle. Main calls happen here.
    damaged = environment()
    budgetize(damaged)
    wakeup_nodes(damaged) # calls their behaviour, which calls the policy (what to do), and finally applies actions
    snapshot()

def cycle(): # the Highest function
    while not termination_condition():
	print termination_condition()
	step()

# TODO initialize custom fields
