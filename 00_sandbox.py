from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Converter:
    def __init__(self):

        # Formatting varibles
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations
        '''self.all_calc_list =  ['5 degrees C is -17.2 degrees F',
                                '6 degrees C is -16.7 degrees F',
                                '7 degrees C is -16.1 degrees F',
                                '8 degrees C is -15.8 degrees F',
                                '9 degrees C is -15.1 degrees F',
                               ]'''

        self.all_calc_list = []

        # converter frame
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)

        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Tempperature Converter",
                                        font="Arial 19 bold",
                                        bg=background_color,
                                        padx=10, pady=10)

        self.temp_heading_label.grid(row=0)

        # user instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons below...",
                                             font="Arial 10 italic", wrap=290,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), orchid3 | khakil
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To centigrade", font="Arial 10 bold",
                                  bg="khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Answer will appear here")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15,
                                       command=lambda: self.history(self.all_calc_list))
        self.calc_hist_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.calc_hist_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        # print(low)

        error = "#ffafaf"  # Pale pink background for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check amount is a valid number

            # convert from C to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # check and convert to centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) + 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celsius)

            else:
                # input is invalid (too cold)!!
                answer = "Too cold!"
                has_errors = "yes"

            # Display answer
             # print(answer)
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add Answer to list for History
            if answer != "too cold":
                self.all_calc_list.append(answer)
                self.calc_hist_button.config(state=NORMAL)

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

    def history(self, calc_history):
        History(self, calc_history)


    def help(self):
        # print("you asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class History:
    def __init__(self, partner, calc_history):

        background = "#a9ef99"  # Pale green

        # disable history button
        partner.calc_hist_button.config(state=DISABLED)

        # set up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        # set up GUI frame
        self.history_frame = Frame(self.history_box, width=350, bg=background)
        self.history_frame.grid()

        # set up history heading (row 0)
        self.how_heading = Label(self.history_frame,
                                 text="Calculation History",
                                 font="arial 10 bold",
                                 bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent"
                                       " Calculations. please use the "
                                       "export button to create a text "
                                       "file of all your Calculations for "
                                       "This session",
                                  wrap=250,
                                  font="arial 10 italic",
                                  justify=LEFT, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History output goes here ... (row 2)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                               - item - 1] + "\n"
        else:
            for item in calc_history:
                history_string += item + "\n"

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dissmiss Button Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame,
                                    text="Export",
                                    font="Arial 12 bold",
                                    command=partial(self.export, partner))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame,
                                     text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.calc_hist_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, partner):
        get_export = Export(self)

class Export:
    def __init__(self, calc_history, partner):
        background = "#a9ef99"  # pale green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up chid window (ie: export and
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
                                    font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # export Instructions (lable, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename"
                                                        "in the box bellow"
                                                        "and press the save"
                                                        "button to save your"
                                                        "calculation history"
                                                        "to a text file",
                                justify=LEFT, width=40,
                                bg=background, wrap=250)
        self.export_text = Label(self.export_frame, text="if the filename "
                                                        "you enter below "
                                                        "already exists "
                                                        "its contents will "
                                                        "be replaced with "
                                                        "your calculation "
                                                        "history",
                                justify=LEFT, bg="#ffafaf", fg="maroon",
                                font="Arial 10 italic", wrap=225, padx=10,
                                pady=10)
        self.export_text.grid(row=2, pady=10)

        # filename enter box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Lables (initially blank, row 4
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # save / cancel frame(row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # save and cancel Buttons (row 0 of save cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        print("you said to save")

    def close_export(self, partner):
        # put export button back to normal..
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

class Help:
    def __init__(self, partner):
        background = "Orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / instructions",
                                font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                            justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                width=10, bg="orange", font="arial 10 bold",
                                command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
