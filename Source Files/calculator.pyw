import os
import time
import math
import keyboard
from tkinter import *
from tkvideo import tkvideo
import tkinter.messagebox as mbox

# GET CURRENT WORKING DIRECTORY
cwd = os.path.dirname(os.path.abspath(__file__))

# CALCULATOR FUNCTION
def calculator():

    # MAKE CALCULATOR WINDOW ABOVE LOADING SCREEN
    win = Toplevel(root)

    # REMOVE THE LOADING WINDOW FROM SCREEN
    root.withdraw()

    # CLOSE ROOT WINDOW TOO IF CLACULATOR IS CLOSED
    win.protocol('WM_DELETE_WINDOW', root.destroy)
    
    # CALCULATOR WINDOW PROPERTIES
    win.geometry("350x535")
    win.minsize(350,535)
    win.maxsize(350,535)
    win.title("Calculator")
    win.iconbitmap(f"{cwd}\\icon.ico")
    win.focus_force()
    win.lift()

    # MAKE A VARIABLE FOR SCREEN VALUE
    screenValue = StringVar()
    screenValue.set("")

    # MAKE CALCULATOR SCREEN ENTRY
    screen = Entry(win, textvariable=screenValue, font=("lucida", 32, "bold"), justify=RIGHT, relief=SUNKEN, borderwidth=3, bg="light blue", fg="black")
    screen.pack(fill=X, padx=12, pady=12)

    # MAKE A MENU BAR IN CALCULATOR
    menuBar = Menu(win)

    # METHODS FOR SUB MENU 1
    def ClearAll():
        screenValue.set("")

    def DestroyAll():
        win.destroy()
        root.destroy()

    # ENTER SUB MENUS TO MENUBAR (SUB-MENU 1)
    menu1 = Menu(menuBar, tearoff=0)
    menu1.add_command(label="Clear All", command=ClearAll)
    menu1.add_command(label="Exit", command=DestroyAll)


    # METHODS FOR SUB MENU 2
    checkVar = IntVar()
    
    def AlwaysOnTop():
        if checkVar.get() == 1:
            win.wm_attributes("-topmost", 1)
            win.wm_state("zoomed")
        elif checkVar.get() == 0:
            win.wm_attributes("-topmost", 0)
            win.wm_state("normal")

    def Minimize():
        win.wm_state("iconic")

    # ENTER SUB MENUS TO MENUBAR (SUB-MENU 2)
    menu2 = Menu(menuBar, tearoff=0)
    menu2.add_checkbutton(label="Always on Top", variable=checkVar, onvalue=1, offvalue=0, command=AlwaysOnTop)
    menu2.add_command(label="Minimize", command=Minimize)

    # METHODS FOR SUB MENU 3
    def Version():
        main = Tk()
        main.overrideredirect(1)
        main.withdraw()
        mbox.showinfo("Build Version", "Build Version 1.0.0")
        main.destroy()

    def About():
        main = Tk()
        main.overrideredirect(1)
        main.withdraw()
        mbox.showinfo("About Calculator", "                   Calculator App\n\nMade by: Syed Muhammad Sameer Nasir\nContact No. +923009644099\n")
        main.destroy()
    
    # ENTER SUBMENUS TO MENU (SUB-MENU 3)
    menu3 = Menu(menuBar, tearoff=0)
    menu3.add_command(label="Check Build Version", command=Version)
    menu3.add_separator()
    menu3.add_command(label="About Calculator", command=About)

    # ENTER MENUS IN MENU BAR
    menuBar.add_cascade(menu=menu1, label="File")
    menuBar.add_cascade(menu=menu2, label="Window")
    menuBar.add_cascade(menu=menu3, label="Help")

    # MAKE A FRAME FOR BUTTONS
    frame = Frame(win, bg='#0060af', relief=SUNKEN, borderwidth=3)
    frame.pack(side=LEFT, anchor=NW, padx=10, pady=10)


    # CLICK FUNCTION FOR BUTTONS
    def ButtonClicked(event):
        result = ''
        keyPressed = False
        if keyboard.is_pressed('enter'):
            keyPressed = True
            text = '='
        else:
            text = event.widget.cget("text")

        if text == '=' or keyPressed == True:
            if '%' in screenValue.get():
                exp = screenValue.get()
                num1, num2 = exp.split('%')
                result = (float(num1)/float(num2))*100
            elif '√' in screenValue.get():
                exp = screenValue.get()
                num = exp.split('√')
                result = math.sqrt(float(str(num[1])))
            else:
                if screenValue.get().isdigit():
                    result = int(screenValue.get())
                else:
                    try:
                        result = eval(screenValue.get())
                    except Exception:
                        screenValue.set("Error")
                        screen.update()
                        time.sleep(1)
                        screenValue.set("")
                        screen.update()
            if isinstance(result, float):
                result = round(result, 2)        
            screenValue.set(result)
            screen.update()
        elif text == 'C':
            screenValue.set("")
            screen.icursor(END)
            screen.update()
        else:
            screenValue.set(screenValue.get() + text)
            screen.icursor(END)
            screen.update()


    # MAKE BUTTONS:

    #ZERO ROW
    butC = Button(frame, text='C', font=('lucida', 25),activebackground="white", width=3, relief=RAISED, borderwidth=3, bg="#ffd582", fg="black")
    butC.grid(row=0, column=0, padx=6, pady=8)
    butC.bind('<Button-1>', ButtonClicked)
    
    butper = Button(frame, text='%', font=('lucida', 25),activebackground="white", width=3, relief=RAISED, borderwidth=3, bg="light green")
    butper.grid(row=0, column=1, padx=6, pady=8)
    butper.bind('<Button-1>', ButtonClicked)

    butsqrt = Button(frame, text='√', font=('lucida', 25),activebackground="white", width=3, relief=RAISED, borderwidth=3, bg="light green")
    butsqrt.grid(row=0, column=2, padx=6, pady=8)
    butsqrt.bind('<Button-1>', ButtonClicked)

    butdiv = Button(frame, text='/', font=('lucida', 25),activebackground="white", width=3, relief=RAISED, borderwidth=3, bg="light green")
    butdiv.grid(row=0, column= 3, padx=6, pady=8)
    butdiv.bind('<Button-1>', ButtonClicked)

    # FIRST ROW
    but7 = Button(frame, text='7', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but7.grid(row=1, column=0, padx=6, pady=8)
    but7.bind('<Button-1>', ButtonClicked)

    but8 = Button(frame, text='8', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but8.grid(row=1, column=1, padx=6, pady=8)
    but8.bind('<Button-1>', ButtonClicked)

    but9 = Button(frame, text='9', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but9.grid(row=1, column= 2, padx=6, pady=8)
    but9.bind('<Button-1>', ButtonClicked)

    butmul = Button(frame, text='*', font=('lucida', 25),activebackground="white", width=3, relief=RAISED, borderwidth=3, bg="light green")
    butmul.grid(row=1, column=3, padx=6, pady=8)
    butmul.bind('<Button-1>', ButtonClicked)

    # SECOND ROW
    but4 = Button(frame, text='4', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but4.grid(row=2, column=0, padx=6, pady=8)
    but4.bind('<Button-1>', ButtonClicked)

    but5 = Button(frame, text='5', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but5.grid(row=2, column=1, padx=6, pady=8)
    but5.bind('<Button-1>', ButtonClicked)

    but6 = Button(frame, text='6', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but6.grid(row=2, column=2, padx=6, pady=8)
    but6.bind('<Button-1>', ButtonClicked)

    butsub = Button(frame, text='-', font=('lucida', 25),activebackground="white", width=3, relief=RAISED, borderwidth=3, bg="light green")
    butsub.grid(row=2, column=3, padx=6, pady=8)
    butsub.bind('<Button-1>', ButtonClicked)

    # THIRD ROW
    but1 = Button(frame, text='1', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but1.grid(row=3, column=0, padx=6, pady=8)
    but1.bind('<Button-1>', ButtonClicked)

    but2 = Button(frame, text='2', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but2.grid(row=3, column=1, padx=6, pady=8)
    but2.bind('<Button-1>', ButtonClicked)

    but3 = Button(frame, text='3', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but3.grid(row=3, column=2, padx=6, pady=8)
    but3.bind('<Button-1>', ButtonClicked)

    butadd = Button(frame, text='+', font=('lucida', 25),activebackground="white", width=3, relief=RAISED, borderwidth=3, bg="light green")
    butadd.grid(row=3, column=3, padx=6, pady=8)
    butadd.bind('<Button-1>', ButtonClicked)

    # FOURTH ROW
    but0 = Button(frame, text='0', font=('lucida', 25),activebackground="white", activeforeground="black", width=7, padx=5, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    but0.grid(row=4, column=0, columnspan=2, padx=6, pady=8)
    but0.bind('<Button-1>', ButtonClicked)

    butpt = Button(frame, text='.', font=('lucida', 25),activebackground="light green", width=3, relief=RAISED, borderwidth=3, bg="#1272e6", fg="white")
    butpt.grid(row=4, column=2, padx=6, pady=8)
    butpt.bind('<Button-1>', ButtonClicked)

    buteq = Button(frame, text='=', font=('lucida', 25),activebackground="white", width=3, relief=RAISED, borderwidth=3, bg="#ffd582", fg="black")
    buteq.grid(row=4, column=3, padx=6, pady=8)
    buteq.bind('<Button-1>', ButtonClicked)
    

    win.bind('<Return>', ButtonClicked)

    # CHANGE BACKGROUND AND ADD MENU BAR TO CALCULATOR
    win.config(bg='#1272e6', menu=menuBar)
    win.mainloop()


# MAIN PROGRAM
if __name__ == "__main__":

    global root
    root = Tk()

    # PLACE WINDOWS IN CENTER OF SCREEN
    windows_width = 350
    windows_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_x = int((screen_width/2)-(windows_width/2))
    position_y = int((screen_height/2)-(windows_height/2))

    # LOADING SCREEN GEOMETRY
    root.geometry(f"{windows_width}x{windows_height}+{position_x}+{position_y}")
    root.minsize(windows_width,windows_height)
    root.maxsize(windows_width,windows_height)
    
    # REMOVE THE DEFAULT WINDOWS TITLE BAR
    root.overrideredirect(True)

    # NEW FRAME IN MIDDLE OF LOADING WINDOW
    frame = Frame(root, borderwidth=0)
    frame.place(relx=.5, rely=.4, anchor=CENTER)

    # MAKE A VIDEO PLAYER BOX WITH LABEL
    videoLabel = Label(frame, borderwidth=0)
    videoLabel.pack()

    # VIDEO FILE (.MP4) PATH
    videoPath = cwd + "\\loading.mp4"

    # ADD THE VIDEO TO LABEL AND PLAY IT
    player = tkvideo(videoPath, videoLabel, loop=2, size=(380,300))
    player.play()

    # OPENING TEXT
    text = Label(root, text="Opening Calculator", font=("Impact", 18), bg='#1272e6', fg='white')
    text.place(relx=0.5, rely=0.7, anchor=CENTER)

    # CHANGING BACKGROUND OF LOADING SCREEN
    root.config(bg='#1272e6')

    # CALL CALCULATOR METHOD
    root.after(5000, calculator)
    root.mainloop()