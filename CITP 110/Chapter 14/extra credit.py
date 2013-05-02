#=====================================================================
# Program:      Homework Assignment for Extra Credit
# Programmer:   Teresa Potts
# Date:         May 1,2013
# Abstract:     This program calculates your estimated miles per gallon
#              (MPG) based on your gas tank size and how far you will go.
#=====================================================================

import tkinter
import tkinter.messagebox

class MpgCalculatorGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter your gas tank capacity in gallons.")
        self.capacity_entry = tkinter.Entry(self.top_frame,width=5)

        # Pack the frame's widgets.
        self.prompt_label.pack(side="left")
        self.capacity_entry.pack(side="left")


        # Create the widgets for the mid frame.
        self.prompt_label = tkinter.Label(self.mid_frame, text="Enter how many miles you can travel on a full tank.")
        self.miles_entry = tkinter.Entry(self.mid_frame, width=5)

        self.prompt_label.pack(side="left")
        self.miles_entry.pack(side="left")

        self.calc = tkinter.Button(self.bottom_frame, text="Calculate", command=self.mpg)
        self.quit = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the buttons.
        self.calc.pack(side="left")
        self.quit.pack(side="left")

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.

    def mpg(self):
        # Get the value entered by the user into the
        # capacity_entry widget.
        capacity = float(self.capacity_entry.get())
        miles = float(self.miles_entry.get())

        # Calculate the MPG.
        mpg = miles/capacity

        # Display the results in an info dialog box.
        tkinter.messagebox.showinfo("Your MPG is:", mpg)

# Create an instance of the mpgcalculatorGUI class.
mpg_calc = MpgCalculatorGUI()