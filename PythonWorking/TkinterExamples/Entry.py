from tkinter import *
from Quitter import Quitter

def fetch():
    print('Input => "%s"' % entry.get())                # get text

root = Tk()

entry = Entry(root)
entry.insert(0, 'type words here')                      # set text
entry.pack(side=TOP, fill=X)                            # grow horizontally

entry.focus()                                           # save a click
entry.bind('<Return>', (lambda event: fetch()))         # on enter key
fetchBtn = Button(root, text='Fetch', command=fetch)    # on button
fetchBtn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()



