"""
Generate a graph that would pose a challenge for a constraint satisfaction algorithm
We introduce a few pitfalls to prevent ill formed constraint algorithms from passing
NOTE: CSP graphs are undirected
Pitfalls:
    - Unsatisfiable constraints, how these are handled is important - a > b > c > a
With this in mind we build the following graphs:
    - A graph of A - B - C where the constraints are A > B, B > C, C > A
    - A colouring graph with the following nodes
    -   A - B | A col != B col
    -   A - D | A col != D col
    -   B - C | B col != C col
    -   D - C | D col != C col
    -   C - E | C col != E col
    - Each node in the graph has the domain {red, blue, green}
"""

import graphviz

if __name__ == "__main__":
    dot = graphviz.Graph('constraint_satisfaction')

    with dot.subgraph(name='cluster_infinite') as infinite:
        infinite.attr(rank='min')
        infinite.node('A')
        infinite.node('B')
        infinite.node('C')

        infinite.attr('node', shape='box')
        infinite.node('AB', label='A > B')
        infinite.node('BC', label='B > C')
        infinite.node('CA', label='C > A')

        infinite.edges([
            ('A', 'AB'),
            ('AB', 'B'),
            ('B', 'BC'),
            ('BC', 'C'),
            ('C', 'CA'),
            ('CA', 'A')
        ])
        infinite.attr(label='Unsolvable CSP, domain={1,2,3} for all nodes')

    with dot.subgraph(name='cluster_colouring') as colouring:
        colouring.node('D')
        colouring.node('E')
        colouring.node('F')
        colouring.node('G')
        colouring.node('H')

        colouring.attr('node', shape='box')
        colouring.node('DE', label='D /= E')
        colouring.node('DF', label='D /= F')
        colouring.node('EG', label='E /= G')
        colouring.node('FG', label='F /= G')
        colouring.node('GH', label='G /= H')

        colouring.edges([
            ('D', 'DE'),
            ('D', 'DF'),
            ('DE', 'E'),
            ('DF', 'F'),
            ('E', 'EG'),
            ('EG', 'G'),
            ('F', 'FG'),
            ('FG', 'G'),
            ('G', 'GH'),
            ('GH', 'H')
        ])
        colouring.attr(label='Colouring problem, domain = {red, green, blue} for all nodes')

    dot.render(directory='output_diagrams', view=True)
