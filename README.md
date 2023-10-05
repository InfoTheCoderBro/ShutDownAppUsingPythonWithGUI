# ShutDownAppUsingPythonWithGUI
This Python script is a simple graphical user interface (GUI) application created using the Tkinter library. It provides a user-friendly interface for performing various system shutdown and restart actions on a computer. Here's a description of its main components and functionality:

Application Title: "ShutDown App"

GUI Window: The application opens a window with the following characteristics:

Dimensions: 500x500 pixels
Background Color: Blue
Buttons: The GUI window features four buttons, each with a distinct purpose:

Restart Button: This button allows the user to restart the computer immediately. When clicked, it triggers the restart function, which uses the os.system function to execute the "shutdown /r /t 1" command. This command restarts the computer after a 1-second delay.
Restart Time Button: Clicking this button initiates a delayed restart. It triggers the restart_time function, which executes the "shutdown /r /t 20" command. This command schedules a restart after a 20-second delay.
Log-Out Button: This button is for logging out of the current user session. When clicked, it calls the logout function, which executes the "shutdown -1" command. This command logs out the user without shutting down the computer.
ShutDown Button: Clicking this button initiates an immediate system shutdown. It triggers the shutdown function, which uses the "shutdown /s /t 1" command to shut down the computer after a 1-second delay.
Button Styling: All buttons have consistent styling:

Text Font: Times New Roman, 20-point, bold
Relief Style: Raised
Cursor Type: Plus
Main Loop: The application runs indefinitely using the mainloop() function from Tkinter. This ensures that the GUI remains responsive and can interact with the user.

In summary, this Tkinter-based "ShutDown App" provides an easy-to-use interface for initiating computer restarts, delayed restarts, user logouts, and system shutdowns. Users can select the desired action by clicking the corresponding button, making it a convenient tool for managing system power options.