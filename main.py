# Import necessary modules
from tkinter import *
import os

# Define a function to restart the computer immediately
def restart():
    os.system("shutdown /r /t 1")

# Define a function to restart the computer after a delay of 20 seconds
def restart_time():
    os.system("shutdown /r /t 20")

# Define a function to log out the current user
def logout():
    os.system("shutdown -l")

# Define a function to shut down the computer immediately
def shutdown():
    os.system("shutdown /s /t 1")

# Create a Tkinter window
st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

# Create a button for restarting the computer
r_button = Button(st, text="Restart", font=("Time New Roman", 20, "bold"),
                  relief=RAISED, cursor="plus", command=restart)
r_button.place(x=150, y=60, height=50, width=200)

# Create a button for restarting the computer after a delay
rt_button = Button(st, text="Restart Time", font=("Time New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)

# Create a button for logging out the current user
lg_button = Button(st, text="Log-Out", font=("Time New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=270, height=50, width=200)

# Create a button for shutting down the computer
st_button = Button(st, text="ShutDown", font=("Time New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=shutdown)
st_button.place(x=150, y=370, height=50, width=200)

# Start the Tkinter main loop to display the window
st.mainloop()
