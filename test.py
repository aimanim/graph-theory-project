import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")

        # Create a button to open a new window
        self.btn_open_window = tk.Button(master, text="Open New Window", command=self.open_new_window)
        self.btn_open_window.pack(pady=20)

    def open_new_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("New Window")

        # Add widgets or perform actions in the new window
        label = tk.Label(new_window, text="This is a new window.")
        label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
