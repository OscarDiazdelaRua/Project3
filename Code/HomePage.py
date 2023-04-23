from tkinter import *

def homePage():
    

    home = Tk()
    home.resizable(False, False)
    window_width = 700
    window_height = 550


    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    home.title("MusicZone")
    home.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    welcomeLabel = Label(home, text="Welcome to the MusicZone!", font = "Modern 16 bold italic")

    prefButton = Button(home, text="Select Preferences", font = "Modern 12 bold italic", width = 20, padx=40, pady=30, command=selectPref1)
    algorithm1Button = Button(home, text="Use Algorithm 1", font = "Modern 12 bold italic",width = 20, padx=40, pady=30, command=loadingScreen)
    algorithm2Button = Button(home, text="Use Algorithm 2", font = "Modern 12 bold italic",width = 20, padx=40, pady=30)
    exitButton = Button(home, text="Exit", font = "Modern 12 bold italic",width = 17, pady=20, command=home.destroy)
    questionButton = Button(home, text="?", font = "Modern 12 bold italic",width = 10, pady=20, command=displayImage)
    welcomeLabel.pack()
    prefButton.pack(pady = 10)
    algorithm1Button.pack(pady = 25)
    algorithm2Button.pack(pady = 10)
    exitButton.pack(padx = (235,0),pady = 15, side= "left")
    questionButton.pack(padx =(0,235),pady = 15,side= "right")
    home.mainloop()

def selectPref1():
    # Create a new window
    prefWindow = Tk()
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference1 = Label(prefWindow, text="Danceability", font = "Modern 16 bold italic")
    preference1.grid(row=0, column=250)
    next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=selectPref2)
    next_button.grid(row=450, column=450)

def selectPref2():
    # Create a new window
    prefWindow = Tk()
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference2 = Label(prefWindow, text="Energy", font = "Modern 16 bold italic")
    preference2.grid(row=0, column=250)
    next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=selectPref3)
    next_button.grid(row=450, column=450)

def selectPref3():
    # Create a new window
    prefWindow = Tk()
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference3 = Label(prefWindow, text="Instrumentalness", font = "Modern 16 bold italic")
    preference3.grid(row=0, column=250)
    next_button = Button(prefWindow, text="Done!", padx=40, pady=20)
    next_button.grid(row=450, column=450)

def loadingScreen():
    # Create a new window
    prefWindow = Tk()
    prefWindow.title("Loading")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference4 = Label(prefWindow, text="Loading...", font = "Modern 16 bold italic")
    preference4.grid(row=0, column=250)

def displayImage():
    # Create a new window

    prefWindow = Tk()

    prefWindow.title("Example")
    prefWindow.geometry("500x500")
    img = Image.open("Data/Algovisualcomparison.PNG")
    panel = Label(prefWindow, image = img)

    panel.pack(side = "bottom", fill = "both", expand = "yes")


    # prefWindow = Tk()
    # prefWindow.title("Example")
    # prefWindow.geometry("500x500")
    # # Create a Label Widget
    # preference4 = Label(prefWindow, text="Loading...", font = "Modern 16 bold italic")
    # preference4.grid(row=0, column=250)

homePage()

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