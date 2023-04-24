from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from equations import *
import time
home = Tk()

values = [0,0,0]
function_running = True
# def homePage():
    

#     home.resizable(False, False)
#     window_width = 700
#     window_height = 550



#     screen_width = home.winfo_screenwidth()
#     screen_height = home.winfo_screenheight()

#     x = int((screen_width/2) - (window_width/2))
#     y = int((screen_height/2) - (window_height/2))

#     home.title("MusicZone")
#     home.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
#     welcomeLabel = Label(home, text="Welcome to the MusicZone!", font = "Consolas 16 bold italic")
#     prefButton = Button(home, text="Select Preferences", font = "Consolas 12", width = 20, padx=40, pady=30, command=selectPref1)
#     algorithm1Button = Button(home, text="Use Algorithm 1", font = "Consolas 12",width = 20, padx=40, pady=30, command=loadingScreen)
#     algorithm2Button = Button(home, text="Use Algorithm 2", font = "Consolas 12",width = 20, padx=40, pady=30)
#     exitButton = Button(home, text="Exit", font = "Consolas 12",width = 17, pady=20, command=home.destroy)
#     questionButton = Button(home, text="?", font = "Consolas 12",width = 7, pady=20, command=displayImage)

#     print(values)
    
#     welcomeLabel.pack()
#     prefButton.pack(pady = 10)
#     algorithm1Button.pack(pady = 25)
#     algorithm2Button.pack(pady = 10)
#     exitButton.pack(padx = (215,0),pady = 15, side= "left")
#     questionButton.pack(padx =(0,215),pady = 15,side= "right")
    
#     home.mainloop()



def selectPref1():

    def scale1(val):
        values[0] = val
        print(values[0])

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))


    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500+{}+{}".format(x, y))
    # Create a Label Widget
    preference = Label(prefWindow, text="Danceability", font = "Consolas 16 bold italic",width = 20, padx=40)
    preference.pack()

    slider = Scale(prefWindow, from_=0, to=1, resolution=0.0001, orient=HORIZONTAL, length=300, width=15, sliderlength=5, showvalue= 0, command=scale1)
    slider.pack(pady=(200,0))
    
    value = slider.get()

    next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=lambda: selectPref2(prefWindow))
    next_button.pack(side = "bottom", anchor = "se", padx = 20, pady = 20)
    # preference1.grid(row=0, column=250)
    # next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=lambda: selectPref2(prefWindow))
    # next_button.grid(row=450, column=450)


    

def selectPref2(previousWindow):


    def scale2(val):
        values[1] = val
        print(values[1])

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))

    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500+{}+{}".format(x, y))
    # Create a Label Widget
    preference = Label(prefWindow, text="Energy", font = "Consolas 16 bold italic")
    preference.pack()


    slider = Scale(prefWindow, from_=0, to=1, resolution=0.0001, orient=HORIZONTAL, length=300, width=15, sliderlength=5, showvalue= 0, command=scale2)
    slider.pack(pady=(200,0))
    
    


    next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=lambda: selectPref3(prefWindow))
    inst_val = next_button.pack(side = "bottom", anchor = "se", padx = 20, pady = 20)
    previousWindow.destroy()

    
    

def selectPref3(previousWindow):

    def scale3(val):
        values[2] = val
        print(values[2])

    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))

    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500+{}+{}".format(x, y))
    # Create a Label Widget
    preference = Label(prefWindow, text="Instrumentalness", font = "Consolas 16 bold italic")
    preference.pack()

    slider = Scale(prefWindow, from_=0, to=1, resolution=0.0001, orient=HORIZONTAL, length=300, width=15, sliderlength=5, showvalue= 0, command=scale3)
    slider.pack(pady=(200,0))
    
    



    next_button = Button(prefWindow, text="Done!", padx=40, pady=20, command= prefWindow.destroy)
    next_button.pack(side = "bottom", anchor = "se", padx = 20, pady = 20)
    previousWindow.destroy()


def loadingScreen():
    # Create a new window
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))
    prefWindow = Toplevel(home)
    prefWindow.title("Loading...")
    prefWindow.geometry("500x500+{}+{}".format(x, y))
    # Create a Label Widget
    preference4 = Label(prefWindow, text="Loading...", font = "Consolas 16 bold italic")
    preference4.grid(row=0, column=250)
    # TODO: Currently, loading screen does not have anything in frame, only tag. fix if see fit
    
    # start the progress bar animation
    
    home.after(1, lambda: calculationHelper(prefWindow))
    
    while function_running:
        home.update_idletasks()
        home.update()
        time.sleep(.00001)
   
    loadingScreen.destroy()


def displayImage():
    # Create a new window
    
    window_width = 500
    window_height = 500
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    prefWindow = Toplevel(home)

    prefWindow.resizable(False, False)

    prefWindow.title("Example")
    prefWindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    img = Image.open("Data/Algovisualcomparison.PNG")
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    label = Label(prefWindow, image=img)
    label.image = img  # Keep a reference to the image to prevent garbage collection
    label.pack()

def calculationHelper(previousWindow):
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))

    # Create a new window
    Window = Toplevel(home)
    Window.title("Calculation Complete")
    Window.geometry("500x500+{}+{}".format(x, y))
    # Create a Label Widget
    preference = Label(Window, text="Output", font = "Consolas 16 bold italic")
    preference.pack()
    temp = KMeans(float(values[0]), float(values[1]), float(values[2]))
    print(temp)
    # TODO: Place output in frame here 
    next_button = Button(Window, text="Close", padx=40, pady=20, command= Window.destroy)
    next_button.pack(side = "bottom", anchor = "se", padx = 20, pady = 20)
    function_running = False
    previousWindow.destroy()
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
    # preference4 = Label(prefWindow, text="Loading...", font = "Consolas 16 bold italic")
    # preference4.grid(row=0, column=250)

# homePage()

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