from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Converter:
    def __init__(self):

        # Formatting varibles
        background_color = "light blue"

        # converter frame
        self.converter_frame = Frame(width=300, height=300,
                                     bg=background_color,
                                     pady=10)

        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Tempperature Converter",
                                        font=("Arial", "16", "bold"),
                                        bg=background_color,
                                        padx=10, pady=10)

        self.temp_heading_label.grid(row=0)

        #export button (Row 1)
        self.export_button = Button(self.converter_frame, text="Export",
                                    font=("Arial", "14"),
                                    padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):

            background = "#a9ef99"      #pale green

            #disable export button
            partner.export_button.config(state=DISABLED)

            #sets up chid window (ie: export and
            self.export_box = Toplevel()

            # 'releaseds' export button
            self.export_box.protocol('WM_DELETE WINDOW',
                                     partial(self.close_export, partner))

            # set up GUI frame
            self.export_frame = Frame(self.export_box, width=300, bg=background)
            self.export_frame.grid()

            # set up export heading (row 0)
            self.how_heading = Label(self.export_frame,
                                     text="Export / Instructions",
                                     font="arial 14 bold, bg=background")
            self.how_heading.grid(row=0)

            #export Instructions (lable, row 1)
            self.export_text = Label(self.export_frame, text="Enter a filename"
                                                            "in the box bellow"
                                                            "and press the save"
                                                            "button to save your"
                                                             "calculation history"
                                                            "to a text file",
                                    justify=LEFT, width=40,
                                     bg=background, wrap=250)
            self.export_text = Label(self.export_frame, text="if the filename"
                                                            "you enter below"
                                                             "already exists"
                                                             "its contents will"
                                                             "be replaced with"
                                                             "your calculation"
                                                             "history",
                                     justify=LEFT, bg="#ffafaf", fg="maroon",
                                     font="Arial 10 italic", wrap=225, padx=10,
                                     pady=10)
            self.export_text.grid(row=2, pady=10)

            # filename enter box (row 3)
            self.filename_entry = Entry(self.export_frame, width=20,
                                        font="Arial 14 bold", justify=CENTER)
            self.filename_entry.grid(row=3, pady=10)

            #save / cancel frame(row 4)
            self.save_cancel_frame = Frame(self.export_frame)
            self.save_cancel_frame.grid(row=5, pady=10)

            #save and cancel Buttons (row 0 of save cancel_frame)

            self.save_button= Button(self.save_cancel_frame, text="save")
            self.save_cancel_frame.grid(row=5, column=0)

            self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                        command=partial(self.close_export, partner))
            self.cancel_button.grid(row=0, column=1)

    def close_export(self,partner):
        #put export button back to normal..
        partner.export_button.config(stae=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
