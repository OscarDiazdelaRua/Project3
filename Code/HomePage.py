from tkinter import *

def homePage():
    home = Tk()
    home.title("MusicZone")
    welcomeLabel = Label(home, text="Welcome to the MusicZone!", font = "Helvetica 16 bold italic")
    prefButton = Button(home, text="Select Preferences", padx=40, pady=20, command=selectPref1)
    algorithm1Button = Button(home, text="Use Algorithm 1", padx=40, pady=20, command=loadingScreen)
    algorithm2Button = Button(home, text="Use Algorithm 2", padx=40, pady=20)
    welcomeLabel.pack()
    prefButton.pack()
    algorithm1Button.pack()
    algorithm2Button.pack()
    home.mainloop()

def selectPref1():
    # Create a new window
    prefWindow = Tk()
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference1 = Label(prefWindow, text="Danceability", font = "Helvetica 16 bold italic")
    preference1.grid(row=0, column=250)
    next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=selectPref2)
    next_button.grid(row=450, column=450)

def selectPref2():
    # Create a new window
    prefWindow = Tk()
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference2 = Label(prefWindow, text="Energy", font = "Helvetica 16 bold italic")
    preference2.grid(row=0, column=250)
    next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=selectPref3)
    next_button.grid(row=450, column=450)

def selectPref3():
    # Create a new window
    prefWindow = Tk()
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference3 = Label(prefWindow, text="Instrumentalness", font = "Helvetica 16 bold italic")
    preference3.grid(row=0, column=250)
    next_button = Button(prefWindow, text="Done!", padx=40, pady=20, command=root)
    next_button.grid(row=450, column=450)

def loadingScreen():
    # Create a new window
    prefWindow = Tk()
    prefWindow.title("Loading")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference4 = Label(prefWindow, text="Loading...", font = "Helvetica 16 bold italic")
    preference4.grid(row=0, column=250)


# Shove it onto the screen
# root = Tk()
# root.title("MusicZone")
# startingLabel =  Label(root, text="Welcome to the MusicZone!", font = "Helvetica 16 bold italic")
# Label(root, text="Welcome to the MusicZone!", font = "Helvetica 16 bold italic")
# startingLabel.pack()
# prefButton = Button(root, text="Select Preferences", padx=40, pady=20, command=selectPref1)
# prefButton.pack()
# button1 = Button(root, text="Use algorithm 1", padx=40, pady=20, command=loadingScreen)
# button1.pack()
# button2 = Button(root, text="Use algorithm 2", padx=40, pady=20, command=loadingScreen)
# button2.pack()

# root.mainloop()