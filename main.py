from ui.containers.MyFrame import MyFrame
from models.Graph import Graph


# my_frame = MyFrame(width=800, height=500, bg="red", title="Flow Max")
# my_frame.mainloop()

my_graph = Graph(head_title="S", tail_title="P")
my_graph.initialize_data()

my_graph.get_unvisited_neighbors('A')

print("Hi")