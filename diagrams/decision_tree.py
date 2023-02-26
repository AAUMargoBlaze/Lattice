"""
Generate a graph representing a very simple decision tree
Here we use a simple example found in:
https://towardsai.net/p/programming/decision-trees-explained-with-a-practical-example-fe47872d3b53
"""

import graphviz

if __name__ == "__main__":
    dot = graphviz.Digraph('decision_tree')
    dot.attr('node', shape='box')

    with dot.subgraph() as rank1:
        rank1.attr(rank='same')
        rank1.node('A', 'Has Feathers?')

    with dot.subgraph() as rank2:
        rank2.attr(rank='same')
        rank2.node('B', 'Can Fly?')
        rank2.node('C', 'Has Finns?')

    with dot.subgraph() as rank3:
        rank3.attr(rank='same')
        rank3.node('D', 'Hawk')
        rank3.node('E', 'Penguin')
        rank3.node('F', 'Dolphin')
        rank3.node('G', 'Bear')

    dot.edge('A', 'B', label='True')
    dot.edge('A', 'C', label='False')

    dot.edge('B', 'D', label='True')
    dot.edge('B', 'E', label='False')

    dot.edge('C', 'F', label='True')
    dot.edge('C', 'G', label='False')

    dot.render(directory='output_diagrams', view=True)
