import networkx as nx
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import scrolledtext
import tkinter as tk

random_number = random.randrange(10, 25)
simpleG = nx.gnp_random_graph(random_number, 0.3, 40)
n1 = random.randrange(5, 10)
n2 = random.randrange(5, 10)
n3 = random.randrange(5, 10)

class MainMenu:         #for the functionalities of main screen...
    def __init__(self):
        self.root = tk.Tk()
        self.DisplayMenu()
    def CloseWindow(self):
        self.root.destroy()
    def simple(self):
        plt.figure(figsize=(9, 9))
        nx.draw_networkx(simpleG, node_color='green')
        plt.show()
    def complete(self):
        G = nx.complete_graph(random.randrange(10, 25))
        nx.draw_networkx(G, node_color='green')
        plt.show()
    def bipartite(self):
        G = nx.complete_bipartite_graph(n1, n2)
        bi_nodes = []
        for i in range(0, n1):
            bi_nodes.append(i)
        pos = nx.bipartite_layout(G, bi_nodes)  # Specify the nodes in the first set
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000)
        plt.show()
    def tripartite(self):
        G = nx.Graph()
        nodes1 = ['A', 'B', 'C', 'D']
        nodes2 = [1, 2, 3, 4, 5]
        nodes3 = ['X', 'Y', 'Z']

        G.add_nodes_from(nodes1, bipartite=0)
        G.add_nodes_from(nodes2, bipartite=1)
        G.add_nodes_from(nodes3, bipartite=2)

        edges = [('A', 1), ('A', 4), ('A', 3), ('B', 1),  ('B', 2),  ('B', 5), ('C', 2),
                 ('C', 4), ('D', 1), ('D', 2), ('D', 3), ('D', 4), ('D', 5), ('D', 'Z'),
                 (1, 'X'), (1, 'Z'), (2, 'Y'), (3, 'Y'), (5, 'Z'), (4, 'Z'), (4, 'X')]
        G.add_edges_from(edges)

        #plot the nodes coordinates
        pos = {
            'A': (1, 3), 'B': (2, 3), 'C': (3, 3), 'D': (4, 3),
            1: (1, 2), 2: (2, 2), 3: (3, 2), 4: (4, 2), 5: (5, 2),
            'X': (1, 1),'Y': (2, 1),'Z': (3, 1)
        }

        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000)
        plt.show()
    def havelhakimi(self):
        hakimi()
    def tarjans(self):
        tarjan()
    def DisplayMenu(self):
        self.root.geometry("900x900")
        self.root.title("Main Menu")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        self.root.configure(bg="lavender")
        title_lbl = tk.Label(self.root, text="MT3001 - Graph Theory Project",font=('Franklin Gothic Medium', 25,'bold'))
        title_lbl.config(bg="lavender",fg="Black")
        title_lbl.place(x=210, y=50)
        lbl1 = tk.Label(self.root, text="Click any of the following buttons:", font=('Franklin Gothic Medium', 20))
        lbl1.config(bg="lavender",fg="black")
        lbl1.place(x=100, y=140)

        btn1 = tk.Button(self.root, text="Simple Graph", font=('Century Gothic', 18),command=self.simple, width=15, height=1)
        btn2 = tk.Button(self.root, text="Complete Graph", font=('Century Gothic', 18),command=self.complete, width=15, height=1)
        btn3 = tk.Button(self.root, text="Bipartite Graph", font=('Century Gothic', 18), command=self.bipartite, width=15, height=1)
        btn4 = tk.Button(self.root, text="Tripartite Graph", font=('Century Gothic', 18), command=self.tripartite, width=15, height=1)
        btn5 = tk.Button(self.root, text="Havel Hakimi", font=('Century Gothic', 18), command=self.havelhakimi, width=15, height=1)
        btn6 = tk.Button(self.root, text="Tarjan's Algorithm", font=('Century Gothic', 18), command=self.tarjans, width=15, height=1)
        btn1.place(x=100, y=220)
        btn2.place(x=100, y=290)
        btn3.place(x=100, y=360)
        btn4.place(x=100, y=430)
        btn5.place(x=100, y=500)
        btn6.place(x=100, y=570)
        self.root.mainloop()
class hakimi:
    def __init__(self):
        self.root = tk.Tk()
        self.display()
    def CloseWindow(self):
        self.root.destroy()
    def simple(self):
        plt.figure(figsize=(9, 9))
        nx.draw_networkx(simpleG, node_color='green')
        plt.show()
    def display(self):
        self.root.geometry("900x900")
        self.root.title("Havel Hakimi")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        self.root.configure(bg="lavender")
        degrees = list(dict(simpleG.degree()).values())
        degrees.sort(reverse=True)
        initial = ', '.join(map(str, degrees))
        initial = "Degree sequence: "+initial
        final_string = ''
        while degrees[0]!=0:
            num = degrees[0]
            for i in range (1,num+1):
                degrees[i] = degrees[i] - 1
            degrees.pop(0)
            degrees.sort(reverse=True)
            result = ', '.join(map(str, degrees))
            final_string = final_string + "\n" + result
        final_string=initial+final_string+"\n\nGraphical!"
        title_lbl = tk.Label(self.root, text="Performing Havel Hakimi's Theorem", font=('Franklin Gothic Medium', 25, 'bold'))
        title_lbl.config(bg="lavender", fg="Black")
        title_lbl.place(x=50, y=50)
        lbl = tk.Label(self.root, text=final_string,font=('Franklin Gothic Medium', 18), justify='right')
        lbl.config(bg="lavender", fg="Black")
        lbl.place(x=50, y=120)
        btn1 = tk.Button(self.root, text="Graph", font=('Franklin Gothic Medium', 18), command=self.simple, width=10,height=1)
        btn1.place(x=55, y=170)
        self.root.mainloop()
class tarjan:
    def __init__(self):
        self.root = tk.Tk()
        self.display()
    def CloseWindow(self):
        self.root.destroy()

    def tarjan_scc(self, graph):
        vertices = len(graph.nodes)
        id = 0
        low_link = [-1] * vertices
        id_array = [-1] * vertices
        stack_member = [False] * vertices
        stack = []
        scc_result = []

        def dfs(u):
            nonlocal id
            print(f"Visiting vertex {u}, ID: {id}, Low-link: {low_link[u]}")
            low_link[u] = id
            id_array[u] = id
            id += 1
            stack.append(u)
            stack_member[u] = True

            for v in graph.neighbors(u):
                if id_array[v] == -1:
                    dfs(v)
                    low_link[u] = min(low_link[u], low_link[v])
                    print(f"Backtracking. Updated low link value of {u} is {low_link[u]}")
                elif stack_member[v]:
                    low_link[u] = min(low_link[u], id_array[v])
                    print(f"No more unvisited neighbours. Updated low link value of {u} is {low_link[u]}")

            w = -1
            if low_link[u] == id_array[u]:
                scc = []
                print(f"ID == lowlink. Found Strongly Connected Component with lowlink {low_link[u]} :")
                while w != u:
                    w = stack.pop()
                    stack_member[w] = False
                    scc.append(w)
                print(scc)
                scc_result.append(scc)

        for i in range(vertices):
            if id_array[i] == -1:
                dfs(i)

        return scc_result
    def drawgraph(self):
        G = nx.DiGraph()
        G.add_edges_from([(0, 1), (2, 0), (3, 4), (4, 5), (5, 3), (14, 2), (6, 7), (7, 8), (8, 6), (0, 6), (1, 13), (13,14)])
        G.add_edges_from([(9, 10), (10, 11), (11, 9), (11, 12), (12, 12), (1, 3), (9, 8), (1, 5), (5, 8)])
        plt.figure(figsize=(9, 9))
        strongly_connected_components = self.tarjan_scc(G)
        color_map = {}
        for i, component in enumerate(strongly_connected_components):
            color = f'C{i}'  # Use distinct colors for each component
            for node in component:
                color_map[node] = color

        # Draw the graph
        pos = nx.spring_layout(G)  # You can use a different layout algorithm if needed
        nx.draw(G, pos, node_color=[color_map[node] for node in G.nodes], with_labels=True, font_weight='bold')
        plt.show()
    def display(self):
        self.root.geometry("900x900")
        self.root.title("Trajan's Algorithm")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        self.root.configure(bg="lavender")
        title_lbl = tk.Label(self.root, text="Executing Tarjan's Algorithm",font=('Franklin Gothic Medium', 25, 'bold'))
        title_lbl.config(bg="lavender", fg="Black")
        title_lbl.place(x=210, y=50)
        # Create a directed graph
        G = nx.DiGraph()
        G.add_edges_from([(0, 1), (2, 0), (3, 4), (4, 5), (5, 3), (14, 2)])
        G.add_edges_from([(6, 7), (7, 8), (8, 6), (0, 6), (1, 13), (13, 14)])
        G.add_edges_from([(9, 10), (10, 11), (11, 9), (11, 12), (12, 12)])
        G.add_edges_from([(1, 3), (9, 8), (1, 5), (5, 8)])
        # Find strongly connected components
        strongly_connected_components = self.tarjan_scc(G)
        result = "Strongly Connected Components: \n"
        for component in strongly_connected_components:
            result = result + str(component) + "\n"
        lbl = tk.Label(self.root, text=result, font=('Franklin Gothic Medium', 18))
        lbl.config(bg="lavender", fg="Black")
        lbl.place(x=250, y=150)
        btn1 = tk.Button(self.root, text="Graph", font=('Franklin Gothic Medium', 18), command= self.drawgraph, width=10,height=1)
        btn1.place(x=350, y=400)
        self.root.mainloop()
MainMenu()