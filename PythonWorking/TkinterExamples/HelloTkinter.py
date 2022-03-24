import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.printHiBtn = tk.Button(self)
        self.printHiBtn["text"] = "Hello World\n(click me)"
        self.printHiBtn["command"] = self.print_hi
        self.printHiBtn.pack(side="top")

        self.quitBtn = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quitBtn.pack(side="bottom")

    def print_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()