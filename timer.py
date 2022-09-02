# Importing modules
from tkinter import *
from turtle import heading
from playsound import playsound
import time

class Countdown_timer:
    def __init__(self,root):
        # Creating the interface object
        self.root = root    
        self.root.title("My Pomodoro")
        self.root.geometry("400x600")
        self.root.config(bg="#000")
        self.root.resizable(width = False, height = False)
        # Changing the feather icon to an image we want
        self.icon = PhotoImage(file="tomato.png")
        self.root.iconphoto (True, self.icon)
        
        self.heading = Label(root, text = "My Pomodoro", font = "Arial 25 bold", bg = "#000", fg = "#ea3548")
        self.heading.pack(pady = 20)

        # Declaring a variable to pause the countdown time
        self.pause = False
        

        # Current Time Clock
        time_clock_label = Label(self.root, font = ("Arial", 14, "bold"), text = "Current Time:", bg = "#fff")
        time_clock_label.place(x = 90, y = 76)

        # Declaring the variables
        # Setting strings to default value
        # Getting user input
        self.hrs = StringVar()
        self.hrs_entry = Entry(self.root, textvariable = self.hrs, width = 2, font = "Arial 50", bg = "#000", fg = "#fff", bd = 0)
        self.hrs_entry.place( x = 30, y = 160)
        self.hrs.set("00")

        self.mins = StringVar()
        self.mins_entry = Entry(self.root, textvariable = self.mins, width = 2, font = "Arial 50", bg = "#000", fg = "#fff", bd = 0)
        self.mins_entry.place( x = 150, y = 160)
        self.mins.set("00")

        self.sec = StringVar()
        self.sec_entry = Entry(self.root, textvariable = self.sec, width = 2, font = "Arial 50", bg = "#000", fg = "#fff", bd = 0)
        self.sec_entry.place( x = 270, y = 160)
        self.sec.set("00")

        Label(self.root, text = "hours", font = "Arial 12", bg = "#000", fg = "#fff").place ( x = 105, y = 200)

        Label(self.root, text = "min", font = "Arial 12", bg = "#000", fg = "#fff").place ( x = 225, y = 200)

        Label(self.root, text = "sec", font = "Arial 12", bg = "#000", fg = "#fff").place ( x = 345, y = 200)

        # Buttons
        self.button_start = Button(self.root, text = "Start", bg = "#ea3548", bd = 0, fg = "#fff", width = 10, height = 2, font = "arial 10 bold", command = self.start_timer)
        self.button_start.place(x = 255, y = 520)

        self.button_reset = Button(self.root, text = "Reset", bg = "#ea3548", bd = 0, fg = "#fff", width = 10, height = 2, font = "arial 10 bold", command = self.reset_timer)
        self.button_reset.place(x = 152, y = 520)

        self.button_pause = Button(self.root, text = "Pause", bg = "#ea3548", bd = 0, fg = "#fff", width = 10, height = 2, font = "arial 10 bold", command = self.pause_timer)
        self.button_pause.place(x = 50, y = 520)

        self.Image1 = PhotoImage(file = "short_session.png")
        self.button1 = Button(self.root, image = self.Image1, bg = "#000", bd = 0, command = self.short_session)
        self.button1.place( x = 7, y = 300)

        self.Image2 = PhotoImage(file = "long_session.png")
        self.button2 = Button(self.root, image = self.Image2, bg = "#000", bd = 0, command = self.long_session)
        self.button2.place( x = 137, y = 300)

        self.Image3 = PhotoImage(file = "break.png")
        self.button3 = Button(self.root, image = self.Image3, bg = "#000", bd = 0, command = self.break_session)
        self.button3.place( x = 267, y = 300)

    def current_time_clock(self):
        self.current_time = Label(self.root, font = ("Arial", 14, "bold"), text = "", bg = "#fff")
        self.current_time.place(x = 222, y = 76)

        self.day_week_display = Label(self.root, font = ("Arial", 14, "bold"), text = "", bg = "#fff")
        self.day_week_display.place(x = 70, y = 104)

        self.clock_time = time.strftime('%H:%M:%S')
        self.current_time.config(text = self.clock_time)
        self.current_time.after(1000, self.current_time_clock)

        self.day_week = time.strftime('%A, %d %B %Y')
        self.day_week_display.config(text = self.day_week)
    
    def pause_timer(self):
        self.button_reset.config(state = "normal")
        self.pause = True

        total_minutes, total_seconds = divmod(self.time_left, 60)

        total_hours = 0

        if total_minutes > 60:
            total_hours, total_minutes = divmod ( total_minutes, 60)
        
        self.hrs.set("{0:2d}".format(total_hours))
        self.mins.set("{0:2d}".format(total_minutes))
        self.sec.set("{0:2d}".format(total_seconds))

        # Update the interface
        root.update()


    def start_timer(self):
        self.button_reset.config(state = "disabled")
        self.pause = False
        
        try:
            self.time_left = int(self.hrs.get())*3600 + int(self.mins.get())*60 + int(self.sec.get())
        except:
            print("Invalid input")

        while self.time_left > -1:
            total_minutes, total_seconds = divmod(self.time_left, 60)
            total_hours = 0
            if total_minutes > 60 :
                total_hours, total_minutes = divmod(total_minutes, 60)

            self.hrs.set("{0:2d}".format(total_hours))
            self.mins.set("{0:2d}".format(total_minutes))
            self.sec.set("{0:2d}".format(total_seconds))

            # Update the interface
            root.update()
            time.sleep(1)

            if self.time_left == 0:
                playsound("Smooth alarm.mp3")
                self.sec.set("00")
                self.mins.set("00")
                self.hrs.set("00")
            
            self.time_left -= 1

            if self.pause == True:
                break
    

    def reset_timer(self):
        self.hrs.set("00")
        self.mins.set("00")
        self.sec.set("00")
    
   
    def short_session(self):
        self.hrs.set("00")
        self.mins.set("20")
        self.sec.set("00")

    def long_session(self):
        self.hrs.set("00")
        self.mins.set("50")
        self.sec.set("00")

    def break_session(self):
        self.hrs.set("00")
        self.mins.set("15")
        self.sec.set("00")


if __name__ == "__main__":
    root = Tk()
    # Creating a CountDown class object
    final_timer = Countdown_timer(root)
    final_timer.current_time_clock()
    root.mainloop()
