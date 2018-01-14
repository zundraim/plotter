#imports
import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



#fonts
LARGE_FONT=("Verdana", 12)

def qf():
    print("it works")

class Plotter(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Graph2d, Graph3d): #All pages have to be added to this list, otherwise navigation will nog be possible
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont): #cont is short for container

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="This is gonna show graphs", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2d = tk.Button(self, text="2d graph",
                            command=lambda: controller.show_frame(Graph2d))
        button2d.pack()

        button3d = tk.Button(self, text="3d graph",
                            command=lambda: controller.show_frame(Graph3d))
        button3d.pack()


class Graph2d(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Here will be 2d plots", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        homeButton = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        homeButton.pack()


        #adding the graph
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,-3,8,9,3,5])

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        


class Graph3d(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)

            label = tk.Label(self, text="Here will be 3d plots", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            homeButton = tk.Button(self, text="Back to home",
                                command=lambda: controller.show_frame(StartPage))
            homeButton.pack()


app = Plotter()
app.mainloop()
