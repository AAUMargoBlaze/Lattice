"""
Generate a graph representing the most basic graph structures possible
This includes:
    - A labeled graph of relationship A  -> B
    - A labeled graph of relationship A <-> B
    - A labeled graph of A and B without a relationship
For the purposes of keeping things compact, we represent all of this as:
A -> B <-> C, D
"""

import graphviz

if __name__ == "__main__":
    dot = graphviz.Digraph('basics')

    with dot.subgraph() as rank1:
        rank1.attr(rank='same')
        rank1.node('A', 'Position A')
        rank1.node('D', 'Position D')

    with dot.subgraph() as rank2:
        rank2.attr(rank='same')
        rank2.node('B', 'Position B')
        rank2.node('C', 'Position C')

    dot.edges(['AB', 'BC', 'CB'])

    dot.render(directory='output_diagrams', view=True)
