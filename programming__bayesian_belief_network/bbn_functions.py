import itertools
from node_class import *


"""
input conditions from users (ex. exercise=Y, diet=N, ...)
probability table in order of Y or N product (ex. YYY, YYN, ..., NNY, NNN)
"""
def cond_input(target, nodes):
    print("\nInput 'Y' or 'N' for conditions")
    for key, node in nodes.items():
        if node == target:
            pass # no need to input Y or N for the target
        else:
            cond = input(node.name + ": ")
            cond = ''.join(['0' if x == 'Y' else '1' for x in cond])
            node.cond = cond # binary (ex. 001, 010, 111, ...)


"""
calculate the comprehensive probability for conditions given
"""
def prob_calculator(target, nodes):
    prob_yes_no = []
    for value in ['0', '1']:
        target.cond = value
        prob_ans = 1.0 # initial probability for multiply
        for key, node in nodes.items():
            p_cond = ""
            p_cond = ''.join([p_cond.join(p.cond) for p in node.parent])
            if p_cond == '': # root nodes
                pass
            else: # at least having one parent
                cond = int(node.cond + p_cond, 2) # binary to positional index
                prob_ans = prob_ans * node.prob[cond]
        # yes = 0.xxx, no = 0.xxx
        prob_yes_no.append(prob_ans)

    return prob_yes_no


"""
print probabilities in raw and percent
"""
def print_prob(probs):
    probs = [round(elem, 3) for elem in probs]
    print("\nRaw Probability: ", probs)
    probs = [round(elem/sum(probs), 3)*100 for elem in probs]
    print("Heart Disease: Yes {}% vs. No {}%\n".format(probs[0], probs[1]))


"""
add a new node either a parent or a child to the target
"""
def add_node(target, nodes):
    name = input("\nEnter the node name: ")
    loc = int(input("Enter 1. Parent  2. Child"))
    if loc == 1: # above target
        nodes[name] = Node(name, [])
        yn = ["".join(c) for c in itertools.product("YN", repeat=1)]
    elif loc == 2: # below target
        nodes[name] = Node(name, [target]) # parent = 'heart disease'
        yn = ["".join(c) for c in itertools.product("YN", repeat=2)]
    else:
        print("Wrong menu selected")

    parents = ''.join([p.name for p in nodes[name].parent])
    # user input for the probabilities when target = Yes
    for value in yn[0:len(yn)//2]:
        prob = float(input('(' + nodes[name].name + ', ' + parents + ')'\
                               + ' = ' + value + ': '))
        nodes[name].prob.append(prob)
    # calculate probabilities when target = No
    for i in range(0, len(yn)//2):
        prob = 1 - nodes[name].prob[i]
        nodes[name].prob.append(prob)


"""
print all the nodes includting target with parents
"""
def show_nodes(nodes):
    print("Node Name\tParents")
    for key, node in nodes.items():
        parents = [p.name for p in node.parent]
        parents = '' if len(parents) == 0 else parents
        print(key, "\t", parents)
