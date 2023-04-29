# This project is made by Oscar Diaz de la Rua, Sebastian Valdes, and Enrique Montanez

# PROJECT 3 - ARTIST RECOMMENDATION USING CLUSTERING

#Runs main.py
from equations import *
from HomePage import *
import pandas as pd



if __name__ == '__main__':
    
    # Sets the main window that will be used for the program

    home.resizable(False, False)
    window_width = 700
    window_height = 550

    # Background texture

    image = PhotoImage(file="Data/Background.PNG")
    label = Label(home, image=image)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Centers the window on the screen
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    #  Configures the main window
    home.title("MusicZone")
    home.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    home.configure(bg = "#00FFCA", bd=5, relief="raised", highlightbackground="black", highlightthickness=5)

    # Sets up label, buttons, and the commands to be carried out

    welcomeLabel = Label(home, text="Welcome to the MusicZone!", font = "Arial 16 bold italic", bg = "#00FFCA", fg = "black", pady=20)
    prefButton = Button(home, text="--> Select Preferences First! <--", font = "Arial 12 bold italic", width = 20, padx=40, pady=30, command=selectPref1, bg = "#00FFCA", fg = "black", activebackground= "#0A4D68")
    algorithm1Button = Button(home, text="Use Algorithm 1", font = "Arial 12 bold italic",width = 20, padx=40, pady=30, command=loadingScreen, bg = "#00FFCA", fg = "black", activebackground= "#0A4D68")
    algorithm2Button = Button(home, text="Use Algorithm 2", font = "Arial 12 bold italic",width = 20, padx=40, pady=30, command=loadingScreen2, bg = "#00FFCA", fg = "black", activebackground= "#0A4D68")
    exitButton = Button(home, text="Exit", font = "Arial 12 bold italic",width = 17, pady=20, command=home.destroy, bg = "#00FFCA", fg = "black", activebackground= "#0A4D68")
    questionButton = Button(home, text="?", font = "Arial 12 bold italic",width = 7, pady=20, command=displayImage, bg = "#00FFCA", fg = "black", activebackground= "#0A4D68")
    
    # Packs(AKA sends to print) all the widgets
    welcomeLabel.pack()
    prefButton.pack(pady = 10)
    algorithm1Button.pack(pady = 25)
    algorithm2Button.pack(pady = 10)
    exitButton.pack(padx = (195,0),pady = 15, side= "left")
    questionButton.pack(padx =(0,195),pady = 15,side= "right")
    
    # Completes the main tkinter loop
    
    home.mainloop()




