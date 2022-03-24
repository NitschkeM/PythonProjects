# from tkinter import Label
# import tkinter
from tkinter import *

Label(None, text='Hellow GUI world3!').pack(expand=YES, fill=BOTH) # Stays in the middle
mainloop()

### First argument is the parent widget / container object
# None means: Attach new Label to the default top-level window of this program.
# helloLabel1 = Label(None, text='Hellow GUI world!')     


### Parent widget: Tk, represents the main('root') window of the program
# root = Tk()
# root.title = 'NewRootTitle'
# helloLabel2 = Label(root, text='Hellow GUI world2!')   


### Packs (arranges) the new Label instances into their parent widget(s?)
# Who is the parent widget? What is its name? Where does it come from?
# helloLabel1.pack()
# helloLabel2.pack()

### Bring up the window and start the tkinter event loop
# helloLabel1.mainloop()

# Can think of it like this:
# def mainloop():
#   while the main window has not been closed:
#       if an event has occurred:
#           run the associated event handler function

