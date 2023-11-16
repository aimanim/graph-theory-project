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
    def trajans(self):
        trajan()
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
        btn6 = tk.Button(self.root, text="Trajan's Algorithm", font=('Century Gothic', 18), command=self.trajans, width=15, height=1)
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
class trajan:
    def __init__(self):
        self.root = tk.Tk()
        self.display()
    def CloseWindow(self):
        self.root.destroy()
    def display(self):
        self.root.geometry("900x900")
        self.root.title("Trajan's Algorithm")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        self.root.configure(bg="lavender")
        title_lbl = tk.Label(self.root, text="MT3001 - Graph Theory Project",font=('Franklin Gothic Medium', 25, 'bold'))
        title_lbl.config(bg="lavender", fg="Black")
        title_lbl.place(x=210, y=50)
        self.root.mainloop()
MainMenu()