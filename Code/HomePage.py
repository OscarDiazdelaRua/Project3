from tkinter import *
from PIL import Image, ImageTk
home = Tk()

def homePage():
    

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
    prefWindow1 = Toplevel(home)
    prefWindow1.title("Preferences")
    prefWindow1.geometry("500x500")
    # Create a Label Widget
    preference1 = Label(prefWindow1, text="Danceability", font = "Modern 16 bold italic")
    preference1.grid(row=0, column=250)
    next_button = Button(prefWindow1, text="Next", padx=40, pady=20, command=lambda: selectPref2(prefWindow1))
    next_button.grid(row=450, column=450)
    

def selectPref2(prefWindow1):
    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference2 = Label(prefWindow, text="Energy", font = "Modern 16 bold italic")
    preference2.grid(row=0, column=250)
    next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=lambda: selectPref3(prefWindow))
    next_button.grid(row=450, column=450)
    prefWindow1.destroy()
    
    

def selectPref3(temp):
    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference3 = Label(prefWindow, text="Instrumentalness", font = "Modern 16 bold italic")
    preference3.grid(row=0, column=250)
    next_button = Button(prefWindow, text="Done!", padx=40, pady=20, command= prefWindow.destroy)
    next_button.grid(row=450, column=450)
    temp.destroy()

def loadingScreen():
    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Loading")
    prefWindow.geometry("500x500")
    # Create a Label Widget
    preference4 = Label(prefWindow, text="Loading...", font = "Modern 16 bold italic")
    preference4.grid(row=0, column=250)

def displayImage():
    # Create a new window

    window_width = 500
    window_height = 500
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    prefWindow = Toplevel(home)

    prefWindow.title("Example")
    prefWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    img = Image.open("Data/Algovisualcomparison.PNG")
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    label = Label(prefWindow, image=img)
    label.image = img  # Keep a reference to the image to prevent garbage collection
    label.pack()

    # prefWindow = Toplevel()

    # prefWindow.title("Example")
    # prefWindow.geometry("500x500")
    # img = Image.open("Data/Algovisualcomparison.PNG")
    # img = img.resize((500, 500), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img)
    
    # panel = Label(prefWindow, image = img)

    # panel.pack(side = "bottom", fill = "both", expand = "yes")


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