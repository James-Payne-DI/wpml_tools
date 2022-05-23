from tkinter import *
from fileCreator import createCSV
import time, spanishCounterparts

root = Tk()
root.title("Spanish Sitemap to CSV file")
root.iconbitmap(r'straw-hats.ico')
root.geometry("480x500")
#root.configure(bg="#1351d8")

def checkState():
    print("URL: ", devlink.get())



#Input Fields
#Adding the title to the top of the box
devLabel = Label(root, text="Enter The Spanish Sitemap URL Below: ")
devLabel.grid(row=0,column=0,sticky=W,columnspan=2,pady=5)

#devsite input box
devlink = Entry(root, width=50, borderwidth=1)
devlink.grid(row=1,column=0,columnspan=3,padx=5,pady=3)

nameLabel = Label(root, text="Enter The name of the dealership Below: ")
nameLabel.grid(row=2,column=0,sticky=W,columnspan=2,pady=5)

#Dealership Name input box
nameString = Entry(root, width=50, borderwidth=1)
nameString.grid(row=4,column=0,columnspan=3,padx=5,pady=3)

pathLabel = Label(root, text="Enter filepath you want this to save to: ")
pathLabel.grid(row=5,column=0,sticky=W,columnspan=2,pady=(5,2))

#devsite input box
pathString = Entry(root, width=50, borderwidth=1)
pathString.grid(row=6,column=0,columnspan=3,padx=5,pady=2)

pathLabel2 = Label(root, text="^Example: '/Users/jimmypayne/Documents'")
pathLabel2.grid(row=7,column=0,sticky=W,columnspan=2,pady=(1,5))


global statusLabel   
statusLabel = Label(root, text="Click 'Run Program' to begin...")
statusLabel.grid(row=9,column=0,sticky=W,columnspan=2,padx=5,pady=(35,5))


#just a way  to run everything without passing any parameters -  useful for tkinter
def executeScript():
    print("Script Executing")
    url = str(devlink.get())
    dealer = str(nameString.get())
    path = str(pathString.get())
    if url:
        statusLabel.config(text="Running...")
        #update idle tasks
        root.update_idletasks()
        time.sleep(1.5)
        translationList = spanishCounterparts.spanishSitemap(url)

        time.sleep(0.75)
        createCSV(path,dealer,translationList)
        statusLabel.config(text="Program Complete")
    else:
        statusLabel.config(text="Please enter a URL in the input field and try again.")
    
    



#Build Button - Executes the 'executeScript' function
build_button = Button(root, text="Run Program", activeforeground='#1351d8', padx=30, pady=10,command=executeScript)
#quit button - exits the program
quit_button = Button(root, text="Exit Program", width=15, height=2, pady=3,command=root.destroy)

build_button.grid(row=10,column=0,sticky=W,columnspan=1,padx=5)
quit_button.place(relx=0.7,rely=0.92)

#Finally, the mainloop() method puts everything on the display,
#and responds to user input until the program terminates.
root.mainloop()

#TESTING: please comment out when not in use
#https://maxwellford-wpml0522.dev.dealerinspire.com/es/mapa-del-sitio/
