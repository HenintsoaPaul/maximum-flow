from ui.containers.MyFrame import MyFrame
from models.Graph import Graph


my_frame = MyFrame(width=800, height=500, bg="white", title="Flow Max")
my_frame.mainloop()

# my_graph = Graph(head_title="S", tail_title="P")
# my_graph.initialize_data()
# print(f"Current flow: {my_graph.get_curr_flow()}")

# flow_states = my_graph.get_flow_states(node_title='S', flow_states=[])
# my_graph.increment_graph(flow_states)
# print(f"Current flow: {my_graph.get_curr_flow()}")

# print('Hmmm')