# BELOW WE IMPORT THE MODULES NEEEDED
from tkinter import *
from tkinter import ttk
import os
import time
import numpy as np
import cv2
import pyautogui
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image

# from tkinter.filedialog import asksaveasfile

# MAIN WINDOWN DECLARED AND SET
mainWindow = Tk()
mainWindow.geometry('800x600')
mainWindow['background']='#856ff8'
# mainWindow.resizable(False, False)


# -------------WIDGETS---------------------------

# HEADER
header=ttk.Label(mainWindow,font=("Arial", 30), width='50',text='TAKE A SHOT',anchor='center')
header.pack(pady=20)

left_frame=ttk.LabelFrame(mainWindow, width=300, height=300, text='What to do?')
left_frame.pack(side=LEFT, padx=20)
left_frame.pack_propagate(0)


# ---------------------------- FUNCTION PORTION -----------------------------------------

# TAKE A SCREENSHOT
def getScrot():
    try:
        if entryBtn.get().isnumeric():
            entryValue=entryBtn.get()
            time.sleep(int(entryValue))
            entryBtn.delete(0, "end")
            print("screenshot taken Sir")
            screenShot=pyautogui.screenshot()
            print(screenShot)
            saveFile=fd.asksaveasfile(initialdir="/home/Programación/PythonPortfolio/screen_recorder",
                                    mode='wb',
                                    defaultextension='.png',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("Python file", ".py"),
                                        ("All files", ".*")
                                    ])
            screenShot.save(saveFile)
        else:
            messagebox.showwarning("Not a number", "Enter a number")
    except:
        print("Error ocurred man")



# START RECORDING
def startRec():
    videoTitleValue=videoTitle.get()
    if(not videoTitleValue.isnumeric()):
        messagebox.showwarning("Video title missing","It is not a number")
        return
    print(videoTitleValue)
    saveFile=fd.asksaveasfile(initialdir="/home/Programación/PythonPortfolio/screen_recorder",
                            mode='wb',
                            defaultextension='.avi',
                            filetypes=[
                                ("Text file", ".txt"),
                                ("Python file", ".py"),
                                ("All files", ".*")
                            ])
    screen_size=tuple(pyautogui.size())
    codec=cv2.VideoWriter_fourcc(*"XVID")
    fps=8.0
    print("Start recording...")
    out=cv2.VideoWriter("{}.avi".format(saveFile.name),codec, fps, (screen_size))
    record_seconds=int(videoTitleValue)
    for i in range(int(record_seconds*fps)):
        img=pyautogui.screenshot()
        frame=np.array(img)
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()
    out.release()
    print("Done recording")

def retrieveImg():
    picFile=fd.askopenfilename(initialdir='home/Programación/PythonPortfolio/screen_recorder')
    img=Image.open(picFile)
    img.show()

def dissapear(event):
    entryBtn.delete(0,END)






# --------------------------------------- MAINFRAME -----------------------------------------------

# TAKING A PIC PORTION

entryBtn=ttk.Entry(left_frame, width=50)
scrot=ttk.Button(left_frame, text='Take a screenshot',command= getScrot)

choosePicBtn=Button(left_frame, text='Retrieve a pic and show it aside', command=retrieveImg)


# RECORDING PORTION
record=ttk.Button(left_frame, text='Start recording', command=startRec)
videoTitle=ttk.Entry(left_frame)



scrot.pack(pady=10)
# chooseSecs.pack(pady=10, side=RIGHT)
entryBtn.pack(pady=10)
entryBtn.insert(0, "Enter seconds to take screenshot")
entryBtn.bind('<Button>', dissapear)

choosePicBtn.pack(pady=10)


record.pack(pady=10)
videoTitle.pack(pady=10)
videoTitle.insert(0, "Enter footage title")
# CANVAS
canvas=Canvas(width=400, height=500, bg='white')
canvas.pack(anchor=CENTER)





# EXECUTING THE WINDOW

# MAIN WINDOWN EXECUTION
mainWindow.mainloop()
