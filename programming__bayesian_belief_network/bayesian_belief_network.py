from node_class import *
from bbn_functions import *


"""
start with example nodes and give probabilities
it can add more nodes and modify probabilities
"""
if __name__ == "__main__":
    # initial nodes
    e = Node("exercise", [])
    d = Node("diet", [])
    h = Node("heart_disease", [e, d])
    c = Node("chest_pain", [h])
    b = Node("blood_pressure", [h])
    nodes = {'exercise': e, 'diet':d, 'heart disease':h, 'chest pain': c, 'blood pressure':b}
    target = nodes['heart disease']
    # initial probabilities
    e.prob = [0.25, 0.75]
    d.prob = [0.7, 0.3]
    h.prob = [0.25, 0.45, 0.55, 0.75, 0.75, 0.55, 0.45, 0.25]
    c.prob = [0.8, 0.01, 0.2, 0.99]
    b.prob = [0.85, 0.2, 0.15, 0.8]

    print("\n*** Bayesian Belif Network ***")
    while True:
        print('*'*30)
        print("Menu\n1. Calculate Probablity\n2. Add a Node\
                   \n3. Show Nodes\n4. Quit")
        menu = int(input("Enter: "))

        if menu == 1:
            cond_input(target, nodes)
            prob_yes_no = prob_calculator(target, nodes)
            print_prob(prob_yes_no)
        elif menu == 2:
            add_node(target, nodes)
        elif menu == 3:
            show_nodes(nodes)
        elif menu == 4:
            print("End the program")
            break
        else:
            print("Input a correct menu")
