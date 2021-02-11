from tkinter import *
from functools import partial # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Tempertature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help", font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("you asked for help")
        Help()
        # get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):

        background = "Orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie: help box)
        self.help_box =Toplevel()

        # set up GUI frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

         # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, b=background, wrap=250)
        self.help_text.grid(colum=0, row=1)

        # Dismiss button (row2)
        self.dismiss_btn =Button(self.help_frame, text="Dismiss", width=10, bg="orange", font="arial 10 bold",
                                 command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self,partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperture Converter")
    something = Converter()
    root.mainloop()
