from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from equations import *
import time
home = Tk()

# Values start at 0 0 0, function_running is used to integrate the algorithms to the GUI 
values = [0,0,0]
function_running = True


# First slider scale window
def selectPref1():

    # Saves the value of the slider
    def scale1(val):
        values[0] = val
       
    # Centers the window on the screen
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))


    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500+{}+{}".format(x, y))
    prefWindow.configure(bg = "#00FFCA", bd=5, relief="raised", highlightbackground="black", highlightthickness=5)
    prefWindow.resizable(False, False)

    # Creates Labels and Scale Widget

    preference = Label(prefWindow, text="Danceability", font = "Arial 16 bold italic",width = 20, padx=40, bg= "#00FFCA", fg = "black")
    preference.pack()

    explanation = Label(prefWindow, text="How much do you want to dance?", font = "Arial 12 bold italic",width = 20, padx=40, bg= "#00FFCA", fg = "black")
    explanation.pack(pady=(50,0))

    slider = Scale(prefWindow, from_=0, to=1, resolution=0.0001, orient=HORIZONTAL, length=300, width=15, sliderlength=7, showvalue= 0, command=scale1, bg= "#00FFCA", fg = "#0A4D68", activebackground = "#00FFCA", troughcolor = "#0A4D68", highlightbackground = "#0A4D68", highlightthickness = 5)
    slider.pack(pady=(150,0))
    
    zero = Label(prefWindow, text="0", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")
    one = Label(prefWindow, text="1", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")

    zero.pack(padx = (80,0),pady = 0, side = "left", anchor = "nw")
    one.pack(padx =(0,80),pady = 0, side = "right", anchor = "ne")

    next_button = Button(prefWindow, text="Next", padx=40, pady=20, font = "Arial 16 bold italic", command=lambda: selectPref2(prefWindow), bg= "#00FFCA", fg = "black", activebackground = "#00FFCA", highlightbackground = "#0A4D68", highlightthickness = 5)
    next_button.pack(side = "bottom", padx = 0, pady = 20)
    # preference1.grid(row=0, column=250)
    # next_button = Button(prefWindow, text="Next", padx=40, pady=20, command=lambda: selectPref2(prefWindow))
    # next_button.grid(row=450, column=450)


    
# Second slider scale window
def selectPref2(previousWindow):

    # Saves the value of the slider
    def scale2(val):
        values[1] = val

    # Centers the window on the screen
    #   
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))

    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500+{}+{}".format(x, y))
    prefWindow.configure(bg = "#00FFCA", bd=5, relief="raised", highlightbackground="black", highlightthickness=5)
    prefWindow.resizable(False, False)

    # Creates Labels and Scale Widget

    preference = Label(prefWindow, text="Energy", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")
    preference.pack()

    explanation = Label(prefWindow, text="How energetic do you want the song to be?", font = "Arial 12 bold italic",width = 40, padx=40, bg= "#00FFCA", fg = "black")
    explanation.pack(pady=(50,0))


    slider = Scale(prefWindow, from_=0, to=1, resolution=0.0001, orient=HORIZONTAL, length=300, width=15, sliderlength=7, showvalue= 0, command=scale2, bg= "#00FFCA", fg = "#0A4D68", activebackground = "#00FFCA", troughcolor = "#0A4D68", highlightbackground = "#0A4D68", highlightthickness = 5)
    slider.pack(pady=(150,0))
    
    zero = Label(prefWindow, text="0", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")
    one = Label(prefWindow, text="1", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")

    zero.pack(padx = (80,0),pady = 0, side = "left", anchor = "nw")
    one.pack(padx =(0,80),pady = 0, side = "right", anchor = "ne")


    next_button = Button(prefWindow, text="Next", padx=40, pady=20, font = "Arial 16 bold italic", command=lambda: selectPref3(prefWindow), bg= "#00FFCA", fg = "black", activebackground = "#00FFCA", highlightbackground = "#0A4D68", highlightthickness = 5)
    next_button.pack(side = "bottom", padx = 0, pady = 20)
    previousWindow.destroy()

    
    
# Third slider scale window
def selectPref3(previousWindow):

    # Saves the value of the slider
    def scale3(val):
        values[2] = val
       
    # Centers the window on the screen
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))

    # Create a new window
    prefWindow = Toplevel(home)
    prefWindow.title("Preferences")
    prefWindow.geometry("500x500+{}+{}".format(x, y))
    prefWindow.configure(bg = "#00FFCA", bd=5, relief="raised", highlightbackground="black", highlightthickness=5)
    prefWindow.resizable(False, False)

    # Creates Labels and Scale Widget

    preference = Label(prefWindow, text="Instrumentalness", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")
    preference.pack()

    explanation = Label(prefWindow, text="How much do you want the song to be instrumental?", font = "Arial 12 bold italic",width = 40, padx=40, bg= "#00FFCA", fg = "black")
    explanation.pack(pady=(50,0))

    slider = Scale(prefWindow, from_=0, to=1, resolution=0.0001, orient=HORIZONTAL, length=300, width=15, sliderlength=7, showvalue= 0, command=scale3, bg= "#00FFCA", fg = "#0A4D68", activebackground = "#00FFCA", troughcolor = "#0A4D68", highlightbackground = "#0A4D68", highlightthickness = 5)
    slider.pack(pady=(150,0))
    
    zero = Label(prefWindow, text="0", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")
    one = Label(prefWindow, text="1", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")

    zero.pack(padx = (80,0),pady = 0, side = "left", anchor = "nw")
    one.pack(padx =(0,80),pady = 0, side = "right", anchor = "ne")

    next_button = Button(prefWindow, text="Done!", padx=40, pady=20, font = "Arial 16 bold italic", command= prefWindow.destroy, bg= "#00FFCA", fg = "black", activebackground = "#00FFCA", highlightbackground = "#0A4D68", highlightthickness = 5)
    next_button.pack(side = "bottom", padx = 0, pady = 20)
    previousWindow.destroy()


def loadingScreen():

    # Create a new window
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (1000/2))
    y = int((screen_height/2) - (200/2))

    # Outputs message
    prefWindow = Toplevel(home)
    prefWindow.title("Loading, Please wait, this will take some time...")
    prefWindow.geometry("1000x200+{}+{}".format(x, y))

    #NOTE: It was not possible to change much of this screen, so we set the info on the header
    
    # Calls the KcalculationHelper function
    home.after(1, lambda: KcalculationHelper(prefWindow))
    
    # Used for the loading screen
    while function_running:
        home.update_idletasks()
        home.update()
        time.sleep(.00001)
   
    loadingScreen.destroy()


def KcalculationHelper(previousWindow):

    # To center the window
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (1000/2))
    y = int((screen_height/2) - (300/2))


    # Create a new window
    Window = Toplevel(home)
    Window.title("Calculation Complete using KMC")
    Window.geometry("1000x300+{}+{}".format(x, y))
    Window.configure(bg = "#00FFCA", bd=5, relief="raised", highlightbackground="black", highlightthickness=5)
    Window.resizable(False, False)

    # Create a Label Widget
    preference = Label(Window, text="Output", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")
    preference.pack()
    temp = KMeans(float(values[0]), float(values[1]), float(values[2]))
    
    # Get the artist names and eliminate unneeded characters
    artist1 = str(temp.iloc[0][2])
    artist2 = str(temp.iloc[1][2])
    artist3 = str(temp.iloc[2][2])
    artist4 = str(temp.iloc[3][2])
    artist5 = str(temp.iloc[4][2])

    artist1 = artist1.replace("[", "").replace("]", "").replace("'", "")
    artist2 = artist2.replace("[", "").replace("]", "").replace("'", "")
    artist3 = artist3.replace("[", "").replace("]", "").replace("'", "")
    artist4 = artist4.replace("[", "").replace("]", "").replace("'", "")
    artist5 = artist5.replace("[", "").replace("]", "").replace("'", "")

    #Output the top 5 songs

    output0 = Label(Window, text= "1. " +temp.iloc[0][1] + " -- by " + (artist1[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output0.pack()
    output1 = Label(Window, text= "2. " +temp.iloc[1][1] + " -- by " + (artist2[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output1.pack()
    output2 = Label(Window, text= "3. " +temp.iloc[2][1] + " -- by " + (artist3[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output2.pack()
    output3 = Label(Window, text= "4. " +temp.iloc[3][1] + " -- by " + (artist4[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output3.pack()
    output4 = Label(Window, text= "5. " +temp.iloc[4][1] + " -- by " + (artist5[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output4.pack()

    # Create a Button Widget to close

    next_button = Button(Window, text="Close", padx=20, pady=10, font = "Arial 12 bold italic", command= Window.destroy, bg= "#00FFCA", fg = "black", activebackground = "#00FFCA", highlightbackground = "#0A4D68", highlightthickness = 5)
    next_button.pack(side = "bottom", anchor = "se", padx = 20, pady = 20)
    function_running = False
    previousWindow.destroy()

def loadingScreen2():


    # Create a new window
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (500/2))
    y = int((screen_height/2) - (500/2))
    prefWindow = Toplevel(home)
    prefWindow.title("Loading...")
    prefWindow.geometry("500x500+{}+{}".format(x, y))
    # Create a Label Widget
    preference4 = Label(prefWindow, text="Loading...", font = "Arial 16 bold italic")
    preference4.grid(row=0, column=250)
    
    # Same as for loadingScreen1
    
    home.after(1, lambda: DcalculationHelper(prefWindow))
    
    while function_running:
        home.update_idletasks()
        home.update()
        time.sleep(.00001)
   
    loadingScreen2.destroy()

def DcalculationHelper(previousWindow):

    # To center the window
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (1000/2))
    y = int((screen_height/2) - (300/2))

    # Create a new window
    Window = Toplevel(home)
    Window.title("Calculation Complete using Distance")
    Window.geometry("1000x300+{}+{}".format(x, y))
    Window.configure(bg = "#00FFCA", bd=5, relief="raised", highlightbackground="black", highlightthickness=5)
    Window.resizable(False, False)

    # Create a Label Widget
    preference = Label(Window, text="Output", font = "Arial 16 bold italic", bg= "#00FFCA", fg = "black")
    preference.pack()
    temp = findClosestSongs(float(values[0]), float(values[1]), float(values[2]))
   
    # Get the artist names and eliminate unneeded characters
    artist1 = str(temp.iloc[0][2])
    artist2 = str(temp.iloc[1][2])
    artist3 = str(temp.iloc[2][2])
    artist4 = str(temp.iloc[3][2])
    artist5 = str(temp.iloc[4][2])

    artist1 = artist1.replace("[", "").replace("]", "").replace("'", "")
    artist2 = artist2.replace("[", "").replace("]", "").replace("'", "")
    artist3 = artist3.replace("[", "").replace("]", "").replace("'", "")
    artist4 = artist4.replace("[", "").replace("]", "").replace("'", "")
    artist5 = artist5.replace("[", "").replace("]", "").replace("'", "")


    #Output the top 5 songs
    output0 = Label(Window, text= "1. " +temp.iloc[0][1] + " -- by " + (artist1[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output0.pack()
    output1 = Label(Window, text= "2. " +temp.iloc[1][1] + " -- by " + (artist2[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output1.pack()
    output2 = Label(Window, text= "3. " +temp.iloc[2][1] + " -- by " + (artist3[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output2.pack()
    output3 = Label(Window, text= "4. " +temp.iloc[3][1] + " -- by " + (artist4[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output3.pack()
    output4 = Label(Window, text= "5. " +temp.iloc[4][1] + " -- by " + (artist5[:40]) + "...", font = "Arial 12 bold italic", bg= "#00FFCA", fg = "black")
    output4.pack()

    # Create a Button Widget to close
    
    next_button = Button(Window, text="Close", padx=20, pady=10,font = "Arial 12 bold italic", command= Window.destroy, bg= "#00FFCA", fg = "black", activebackground = "#00FFCA", highlightbackground = "#0A4D68", highlightthickness = 5)
    next_button.pack(side = "bottom", anchor = "se", padx = 20, pady = 20)
    function_running = False
    previousWindow.destroy()


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


