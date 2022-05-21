from tkinter import *
import time, spanishCounterparts

root = Tk()
root.title("Spanish Sitemap to CSV file")
root.geometry("480x700")
#root.configure(bg="#1351d8")

def checkState():
    print("URL: ", devlink.get())



#Input Fields
#Adding the title to the top of the box
devLabel = Label(root, text="Enter The Spanish Sitemap URL Below: ")
devLabel.grid(row=0,column=0,sticky=W,columnspan=2,pady=5)

#devsite input box
devlink = Entry(root, width=50, borderwidth=1)
devlink.grid(row=1,column=0,columnspan=3,padx=5,pady=4)
        


#just a way  to run everything without passing any parameters -  useful for tkinter
def executeScript():
    print("Script Executing")

    #used for error checkin - not needed to for program to function
    #checkState()
    
    url = str(devlink.get())
    spanishCounterparts.spanishSitemap(url)




#Build Button - Executes the 'executeScript' function
build_button = Button(root, text="Run Program", activeforeground='#1351d8', padx=30, pady=10,command=executeScript)
#quit button - exits the program
quit_button = Button(root, text="Exit Program", width=15, height=2, pady=3,command=root.destroy)

build_button.grid(row=10,column=0,columnspan=1)
quit_button.place(relx=0.7,rely=0.92)

#Finally, the mainloop() method puts everything on the display,
#and responds to user input until the program terminates.
root.mainloop()

#TESTING: please comment out when not in use
#https://maxwellford-wpml0522.dev.dealerinspire.com/es/mapa-del-sitio/
