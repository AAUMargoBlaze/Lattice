"""
Generate a graph that would pose a challenge for a path finding algorithm
We introduce a few pitfalls to prevent ill formed search algorithms from passing
Pitfalls:
    - Include a circular low-cost connection to prevent hill climbing algorithms from passing
    - Make the optimised path not so obvious, we want greedy algorithms to give less optimised results
With this in mind we build a graph of the following:
    - A goal node "G"
    - A dead end of A -> B < - > C of costs 1 each
    - An obvious non-optimal path of A -> D -> G with costs 2/6 respectively (totalling to 8)
    - A better path of A -> E -> F -> G with costs 3/2/2 respectively (totalling to 7)
"""

import graphviz

if __name__ == "__main__":
    dot = graphviz.Digraph('pathfinding')

    with dot.subgraph() as rank1:
        rank1.attr(rank='same')
        rank1.node('E')
        rank1.node('F')

    with dot.subgraph() as rank2:
        rank2.attr(rank='same')
        rank2.node('B')
        rank2.node('Start')

    with dot.subgraph() as rank3:
        rank3.attr(rank='same')
        rank3.node('C')
        rank3.node('D')
        rank3.node('Goal')

    dot.edge("Start", "B", label='1')
    dot.edge("B", "C", label='1')
    dot.edge("C", "B", label='1')

    dot.edge("Start", "D", label='2')
    dot.edge("D", "Goal", label='6')

    dot.edge("Start", "E", label='3')
    dot.edge("E", "F", label='2')
    dot.edge("F", "Goal", label='2')

    dot.render(directory='output_diagrams', view=True)
