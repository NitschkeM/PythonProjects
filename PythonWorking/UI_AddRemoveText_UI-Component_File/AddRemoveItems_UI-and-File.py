# from TkinterExamples/scrolledlist import ScrolledList
from tkinter import *
from Quitter import Quitter
from ScrolledList import ScrolledList
# from ../TkinterExamples/quitter import Quitter


def setupInputField(root): # Frame/Parent?
    inputField = Entry(root)
    inputField.insert(0, 'type words here')                      # set text
    inputField.pack(side=TOP, fill=X)                            # grow horizontally
    inputField.focus()                                           # save a click
    inputField.bind('<Return>', (lambda event: printInputFieldContent()))         # on enter key
    return inputField

def printInputFieldContent():
    print('Input => "%s"' % inputField.get())                   # get text
    

def setupPrintInputFieldContentBtn():
    btn_printInputFieldContent = Button(root, text='Fetch', command=printInputFieldContent)    # on button
    btn_printInputFieldContent.pack(side=LEFT)

root = Tk()
inputField = setupInputField(root)
setupPrintInputFieldContentBtn()

# ScrolledList(items, root).pack()
items = ["item1", "item2", "item3"]
ScrolledList(items, root)
Quitter(root).pack(side=RIGHT)

root.mainloop()

### From ScrolledList definition
# if __name__ == '__main__':
#     options = (('Lumberjack-%s' % x) for x in range(20)) # or map/lambda, [...]
#     ScrolledList(options).mainloop()