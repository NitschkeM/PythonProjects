import tkinter as tk
# tk._test()


# Subclassing Tkinter's main window widget - Tk.
# --> Window inherits from tk.Tk --> Window is child of tk.Tk
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")

        label = tk.Label(self, text="Hello World!")
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)


if __name__ == "__main__":
    window = Window()
    window.mainloop()


# Declaring variable in C#
# int myInt;
# Assgning value to the variable in C#
# myInt = 3;
# Initializing variable in C#:      Initializing Variable as: Declaring Variable & Assigning Value to Variable?
# int myInt = 3




####################################################################################
# def functionName(arg, param):
#     if functionWasCalled():
#         return 'thisCodeRuns'
#     else:
#         return 'thisCodeDoesNotRun'

# def functionWasCalled():
#     return True

# print(functionName('arg', 'param'))
####################################################################################