import networkx as nx
import matplotlib.pyplot as plt
import random
#from tkinter import scrolledtext
import tkinter as tk

random_number = random.randrange(10, 25)
simpleG = nx.gnp_random_graph(random_number, 0.3, 40)
n1 = random.randrange(5, 10)
n2 = random.randrange(5, 10)
n3 = random.randrange(5, 10)

def Generate_Points():                      #Function to generate random points
    points.append(Point(-2, 12))
    points.append(Point(3, 11))
    points.append(Point(1, 7))
    points.append(Point(-3, 5))
    points.append(Point(-5, 9))
    points.append(Point(8, 12))
    points.append(Point(12, 11))
    points.append(Point(7, 7))
    points.append(Point(9, 17))
    points.append(Point(3, 16))
    points.append(Point(5, 20))
    points.append(Point(14, 15))
    points.append(Point(20, 14))
    points.append(Point(17, 10))
    points.append(Point(14, 5))
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def left_most(points) -> int:                 #function for finding leftmost point
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn

def Add_Line(p1, p2, c, color):
    if p2.x>p1.x and p2.y>p1.y:
        return c.create_line(p1.x+10, p1.y+10, p2.x-15, p2.y-10, fill=color, arrow=tk.LAST)
    elif p2.x>p1.x and p2.y<p1.y:
        return c.create_line(p1.x + 5, p1.y-20, p2.x - 10, p2.y+10, fill=color, arrow=tk.LAST)
    elif p2.x<p1.x and p2.y>p1.y:
        return c.create_line(p1.x - 10, p1.y+10, p2.x + 10, p2.y-20, fill=color, arrow=tk.LAST)
    elif p2.x==p1.x and p2.y==p1.y:
        r=30
        c.create_line(p1.x-10, p1.y -23, p2.x-4, p2.y -15, fill=color, arrow=tk.LAST)
        return c.create_arc(p1.x - r-r, p1.y - r, p1.x, p1.y + r, start=40,extent=300, style=tk.ARC, outline=color, width=1)
    else:
        return c.create_line(p1.x - 10, p1.y -15, p2.x + 10, p2.y + 5, fill=color, arrow=tk.LAST)
class MainMenu:         #for the functionalities of main screen...
    def __init__(self):
        self.root = tk.Tk()
        Generate_Points()
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
        tarjan(points)
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
        btn1.place(x=120, y=220)
        btn2.place(x=120, y=290)
        btn3.place(x=120, y=360)
        btn4.place(x=120, y=430)
        btn5.place(x=120, y=500)
        btn6.place(x=120, y=570)
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
    Points = []
    updated_points = {}  # Hashmap that maps points to appropriate coordinates on the screen
    def __init__(self, p):
        self.Points = p
        self.circle_radius = 30
        self.start = Point(150, 500)
        self.screenheight = 700
        self.screenwidth = 800
        self.root = tk.Tk()
        self.result_var = tk.BooleanVar(self.root)
        self.simulation_speed = 1000  # Change this so that program runs faster/slower.
        self.root.withdraw()
        self.tarjansalgo()

    def CloseWindow(self):
        self.root.destroy()
    def proceed(self):
        self.result_var.set(True)
    def tarjansalgo(self):
        c = self.InitializeWindow("Tarjan's Algorithm", "Simulation for Tarjan's algorithm")
        colors = ["light goldenrod", "springgreen2", "salmon1", "cornflower blue", "mediumorchid1"]

        def tarjan_scc(graph):
            vertices = len(graph.nodes)
            id = 0
            low_link = [-1] * vertices
            id_array = [-1] * vertices
            stack_member = [False] * vertices
            stack = []
            scc_result = []
            s = 0
            L = []

            def dfs(u):
                nonlocal id
                nonlocal s
                print(f"Visiting vertex {u}, ID: {id}, Low-link: {low_link[u]}")
                low_link[u] = id
                id_array[u] = id
                id += 1
                stack.append(u)
                stack_member[u] = True
                temp = self.updated_points[self.Points[u]]

                c.create_oval(temp.x - self.circle_radius / 2, temp.y - (2 / 3) * self.circle_radius,
                              temp.x + self.circle_radius / 2, temp.y + (1 / 3) * self.circle_radius, fill="pink")
                coordinates = tk.Label(c, text=f"{u}", font=('Century Gothic', 8, 'bold'), bg="pink", fg="black")
                lowlink = tk.Label(c, text=f"{low_link[u]}", font=('Century Gothic', 12, 'bold'), bg="lavender",
                                   fg="black")
                label_window = c.create_window(temp.x, temp.y - 5, window=coordinates)
                label2_window = c.create_window(temp.x + 30, temp.y - 3, window=lowlink)
                self.result_var.set(False)  # To pause the execution for some time
                self.root.after(self.simulation_speed, self.proceed)  # to call proceed() function after some time
                self.root.wait_variable(self.result_var)
                c.pack()
                for v in graph.neighbors(u):
                    if id_array[v] == -1:
                        lid = Add_Line(self.updated_points[self.Points[u]], self.updated_points[self.Points[v]], c,
                                         "red")
                        L.append(lid)
                        dfs(v)
                        low_link[u] = min(low_link[u], low_link[v])
                        print(f"Backtracking. Updated low link value of {u} is {low_link[u]}")
                        c.delete(lid)
                        self.result_var.set(False)  # To pause the execution for some time
                        self.root.after(self.simulation_speed,
                                        self.proceed)  # to call proceed() function after some time
                        self.root.wait_variable(self.result_var)
                        c.pack()
                        L.pop()
                        lowlink = tk.Label(c, text=f"{low_link[u]}", font=('Century Gothic', 12, 'bold'), bg="lavender",
                                           fg="black")
                        label2_window = c.create_window(temp.x + 30, temp.y - 3, window=lowlink)
                    elif stack_member[v]:
                        low_link[u] = min(low_link[u], id_array[v])
                        print(f"No more unvisited neighbours. Updated low link value of {u} is {low_link[u]}")
                        self.result_var.set(False)  # To pause the execution for some time
                        self.root.after(self.simulation_speed,
                                        self.proceed)  # to call proceed() function after some time
                        self.root.wait_variable(self.result_var)
                        lowlink = tk.Label(c, text=f"{low_link[u]}", font=('Century Gothic', 12, 'bold'), bg="lavender",
                                           fg="black")
                        label2_window = c.create_window(temp.x + 30, temp.y - 3, window=lowlink)

                w = -1
                if low_link[u] == id_array[u]:
                    scc = []
                    print(f"ID == lowlink. Found Strongly Connected Component with lowlink {low_link[u]} :")
                    while w != u:
                        w = stack.pop()
                        stack_member[w] = False
                        scc.append(w)
                        temp = self.updated_points[self.Points[w]]
                        c.create_oval(temp.x - self.circle_radius / 2, temp.y - (2 / 3) * self.circle_radius,
                                      temp.x + self.circle_radius / 2, temp.y + (1 / 3) * self.circle_radius,
                                      fill=f"{colors[s]}")
                        coordinates = tk.Label(c, text=f"{w}", font=('Century Gothic', 8, 'bold'), bg=f"{colors[s]}",
                                               fg="black")
                        label_window = c.create_window(temp.x, temp.y - 5, window=coordinates)
                        self.result_var.set(False)  # To pause the execution for some time
                        self.root.after(self.simulation_speed,
                                        self.proceed)  # to call proceed() function after some time
                        self.root.wait_variable(self.result_var)
                    print(scc)
                    scc_result.append(scc)
                    s = s + 1

            for i in range(vertices):
                if id_array[i] == -1:
                    dfs(i)

            return scc_result

        G = nx.DiGraph()
        G.add_edges_from(
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 5), (5, 6), (6, 7), (7, 5), (1, 7), (5, 8), (8, 9)])
        G.add_edges_from([(9, 10), (10, 8), (0, 9), (11, 8), (11, 12), (12, 13), (13, 11), (13, 14), (14, 14)])
        strongly_connected_components = tarjan_scc(G)
        c.pack()
        self.root.mainloop()
    def InitializeWindow(self,title,text):
        self.root.deiconify()
        self.root.geometry(f"{self.screenwidth}x{self.screenheight}")
        self.root.title(title)
        c = tk.Canvas(self.root, width=self.screenwidth, height=self.screenheight, bg="lavender")
        title_label = tk.Label(c, text=text, font=('Century Gothic', 15), bg="lavender",fg="black")
        c.create_window(400, 50, window=title_label, anchor="center")
        self.root.protocol("WM_DELETE_WINDOW", self.CloseWindow)
        exit_btn = tk.Button(c,text="Back",font=("Century Gothic", 12),command=self.CloseWindow)
        c.create_window(100,100,window=exit_btn)
        exit_btn.place(x=650, y=615)
        origin = self.Points[left_most(self.Points)]
        i=0
        for point in self.Points:
            temp = Point(point.x, point.y)
            temp.x = abs(origin.x - temp.x) * 20 + self.start.x
            temp.y = self.start.y - abs(origin.x + temp.y) * 20
            self.updated_points[point] = temp
            c.create_oval(temp.x - self.circle_radius/2, temp.y - (2/3)*self.circle_radius, temp.x + self.circle_radius/2, temp.y + (1/3)*self.circle_radius, fill="skyblue")
            coordinates = tk.Label(c, text=f"{i}", font=('Century Gothic', 8, 'bold'), bg="skyblue", fg="black")
            label_window = c.create_window(temp.x, temp.y - 5, window=coordinates)
            i=i+1
        G = nx.DiGraph()
        G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 5), (5, 6), (6, 7), (7, 5), (1, 7), (5, 8), (8, 9)])
        G.add_edges_from([(9, 10), (10, 8), (0, 9), (11, 8), (11, 12), (12, 13), (13, 11), (13, 14), (14, 14)])
        for edge in G.edges:
            source_node = edge[0]
            target_node = edge[1]
            Add_Line(self.updated_points[self.Points[source_node]], self.updated_points[self.Points[target_node]], c, "black")
        c.pack()
        return c
points = []
MainMenu()