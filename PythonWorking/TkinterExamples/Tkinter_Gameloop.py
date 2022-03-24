import tkinter as tk

# All X in tkinter are widgets, X = Classes?
# 
whatKindOfWidgetIsThis = tk.Tk()

label = tk.Label(text="Hellow").pack()

whatKindOfWidgetIsThis.mainloop()

print(5)

# Timer / Loop that changes the position of an object each time it runs?
#   If we just update by 1 each time the loop runs.
#   Then how often updates occur will depend on the comupter / hardware.
#       How often the processor executes instructions?
#       How much Processing Time on the Processor the program is allocated.

# Code that executes at specific time intervals?
#   Clock / Timer ?
#   Depends on: Idea of Time, Keeping track of Time - how long since last execution + how long until next execution.


# Connecting implementation to some Timer code?
#   Such that updates depends on time, e.g. updates per seconds, 
#   instead of processor, e.g. faster updates because processor is fast.

# In Tkinter: 
#   Is it possible to update the position of a square without creating a new thread of execution / a new process?
#   Is it possible to execute a for loop while the mainloop is running?
#       I dont think so:
#           I think if we added a statement underneath the mainloop() call
#           then that statement would not execute until the mainloop was exited/stopped/halted/interrupted/canceled.



# Resources:
#   Memory
#           Allocation of Memory?
#   Processing Time
#           Allocation of Processing Time?


#   Resource Name
#       Allocation of Resource
#       Distribution of Resource
#       Shared Resources
#           Who are the resources shared with?
#           Who shares the resources?