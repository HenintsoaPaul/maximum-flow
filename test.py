from models.NodeLink import NodeLink

graph = {
    'S': set([
        NodeLink('A', capacity=10, flow=7, forward=True),
        NodeLink('D', capacity=20, flow=20, forward=True),
        NodeLink('G', capacity=20, flow=11, forward=True)
    ]),
    'A': set([
        NodeLink('S', capacity=10, flow=7, forward=False),
        NodeLink('B', capacity=5, flow=3, forward=True),
        NodeLink('E', capacity=4, flow=4, forward=True)
    ]),
    'B': set([
        NodeLink('A', capacity=5, flow=3, forward=False),
        NodeLink('C', capacity=4, flow=4, forward=True),
        NodeLink('E', capacity=2, flow=1, forward=False)
    ]),
    'C': set([
        NodeLink('B', capacity=4, flow=4, forward=False),
        NodeLink('E', capacity=9, flow=4, forward=False),
        NodeLink('F', capacity=8, flow=0, forward=True),
        NodeLink('P', capacity=8, flow=8, forward=True)
    ]),
    'F': set([
        NodeLink('P', capacity=30, flow=20, forward=True)
    ])
}