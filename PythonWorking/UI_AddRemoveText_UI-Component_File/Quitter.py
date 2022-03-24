"""
a Quit button that verifies exit requests;
to reuse, attach an instance to other GUIs, and re-pack as desired
"""

# Observed: "re-pack as desired" and self.pack() in __init
#   Q: Does pack() in constructor + pack() where component is imported
#       have any adversial effects? Side-effects?
#       or same behavior as if packed only after import?

from tkinter import *
from tkinter.messagebox import askokcancel

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        quitBtn = Button(self, text='Quit', command=self.quit)
        # quitBtn.pack(side=LEFT, expand=YES, fill=BOTH)    # side=LEFT, but centered? Seems to stay in middle, does LEFT have any effect?
        quitBtn.pack(expand=YES, fill=BOTH)                 # does not seem that way to me, after a quick check (ran program)

    ### Disabled Prompt functionality for: Faster Code->Test Feedback loop
    def quit(self):
        # ans = askokcancel('Verify exit', 'Really quit?')
        # if ans: Frame.quit(self)
        Frame.quit(self)

if __name__ == '__main__': Quitter().mainloop()