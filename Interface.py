from tkinter import *
from tkinter import colorchooser
import Graph_Constructor

# Creates the original TKinter window
root = Tk()
root.title("Interface")
root.geometry("400x200")
root.iconbitmap("Pending.ico")

# Everything that gets drawn onto the interface window happens in this function
# so it can be wiped clean and reset
def Draw():
    # In the eventuality of a reset, the colours and the widgets must be deleted
    # and then reinitialised. For simplicty, the actual interface (in this case
    # the root) is left alone. and everything is drawn on it on a blank Frame
    # that can be easily destroyed (also reseting parameters like the colour array)
    frame = Frame(root)
    frame.pack()
    colours = []

    # In case further funtionality will be added later, the colour choose is
    # blocked off in its own frame
    colour_picker_frame = LabelFrame(frame, text="Pick the colours your graph will use", padx=13, pady=13)
    colour_picker_frame.pack(padx=13, pady=13)

    # Lets the user pick a colour and then displays it and adds it to the array
    def pick():
        n = len(colours)+2
        add_colour = colorchooser.askcolor()[1]
        colours.append(add_colour)
        label = Label(colour_picker_frame, text="                                                      ", bg=add_colour).grid(row=n, column=0)
        label = Label(colour_picker_frame, text="                                                      ", bg=add_colour).grid(row=n, column=1)

    # Delets the frame and reinitialises it, getting rid of any previusly made inputs
    def Reset():
        frame.destroy()
        Draw()

    # The two buttons that add colours or reset the fram, getting rid of the colours
    add_button = Button(colour_picker_frame, text="Add a colour", command=pick).grid(row=0, column=0)
    reset_button = Button(colour_picker_frame, text="Reset colour selection", command=lambda: Reset()).grid(row=0, column=1)

    # A friendly reminder to check before the finalization of the process
    label = Label(frame, text="Don't forget to check your data file!").pack()
    empty = Label(frame, text=None).pack()
    create_button = Button(frame, text="Generate graph", command=lambda: Graph_Constructor.Construct(colours)).pack()

Draw()

root.mainloop()
