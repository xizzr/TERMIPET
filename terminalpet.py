import os
import tkinter as tk
import time
import threading
from nava import play

root = tk.Tk()  # Removes the window decorations
root.geometry("400x300")  # Set window size
root.configure(bg="black")
root.title("Terminal Pet Name")
root.iconbitmap(default="C:/Users/Admin/Desktop/xizzr/terminalpet/hampter.ico")

newpet = False
currentname = ""

# Overhead text (initialized as empty)
overheadtext = tk.Label(root, text="", fg="white", bg="black", font=("Courier", 25))
overheadtext.pack(pady=20)

# ASCII art for hamster
hamster_default = """
             .      .
            (>\---/<)
            ,'     `.
           /  o   o  \\
          (  >(_Y_)<  )
           >-' `-' `-<-.
          /  _.== ,=.,- \\
         /,    )`  '(    )
        ; `._.'      `--<
       :     \        |  )
       \      )       ;_/ 
        `._ _/_  ___.'-\\\\
           `--\\\\
""" 
hamster_sleepy = """
             .      .
            (<\---/>)
            ,'     `.
           /  __ __  \\
          (  >(_Y_)<  )
           >-' `-' `-<-.
          /  _.== ,=.,- \\
         /,    )`  '(    )
        ; `._.'      `--<
       :     \        |  )
       \      )       ;_/ 
        `._ _/_  ___.'-\\\\
           `--\\\\
"""
hamster_what = """
             .      .
            (>\---/<)
            ,'     `.
           /  .   .  \\
          (  >(_v_)<  )
           >-' `-' `-<-.
          /  _.== ,=.,- \\
         /,    )`  '(    )
        ; `._.'      `--<
       :     \        |  )
       \      )       ;_/ 
        `._ _/_  ___.'-\\\\
           `--\\\\
"""
hamster_sad = """
             .      .
            (>\---/<)
            ,',   , `.
           /  T   T  \\
          (  >(_y_)<  )
           >-' `-' `-<-.
          /  _.== ,=.,- \\
         /,    )`  '(    )
        ; `._.'      `--<
       :     \        |  )
       \      )       ;_/ 
        `._ _/_  ___.'-\\\\
           `--\\\\
"""   
hamster_happy = """
             .      .
            (>\---/<)
            ,'     `.
           /  ^   ^  \\
          (  > (_v_) < )
          >-' -`-' ``-<-.
          /  _.== ,=.,- \\
         /,    )`  '(    )
        ; `._.'      `--<
       :     \\        |  )
       \\      )       ;_/ 
        `._ _/_  ___.'-\\\\
           `--\\\\
""" 

# Read data from the file
def read_datafile():
    global newpet, dataread
    with open("C:/Users/Admin/Desktop/xizzr/terminalpet/termipet.txt", "r") as DATAFILE:
        dataread = DATAFILE.read()

    if dataread == "oops!":
        newpet = True
    else:
        newpet = False

    if newpet:
        root.attributes("-fullscreen", True)
        play("C:/Users/Admin/Desktop/xizzr/terminalpet/sounds/startup.wav", async_mode=True, )
        time.sleep(3)
        for i in range(1, 101):
            overheadtext.config(text=f"Welcome. Enter the desirable name for your TERMIPET.", fg="grey" + str(i))
            time.sleep(0.05)
            root.update()

        time.sleep(3)
        # Input for name
        label = tk.Label(root, text="Enter the name for your TERMIPET:", fg="white", bg="black", font=("Courier", 20))
        label.pack(pady=20)
        
        nameentry = tk.Entry(root, font=("Courier", 15), bg="black", fg="white", highlightcolor="white", highlightthickness="1.25")
        nameentry.pack(pady=10)

        def submit_action():
            user_input = nameentry.get()  # Get the text entered in the input field
            print(f"User Input: {user_input}")
            if currentname != user_input & user_input == "YES":
                print("confriemd")
            else:
                overheadtext.config(text=f"Are you sure you want to name your TERMIPET {user_input}?")
                currentname = user_input
                nameentry.delete(0, tk.END)  # Clear the input field after submitting
                label.config(text="Enter YES to confirm.")

        # Bind the Enter key to submit the name without a button
        nameentry.bind("<Return>", lambda event: submit_action())

# Run the background task in a separate thread
threading.Thread(target=read_datafile, daemon=True).start()

root.mainloop()  # Tkinter main loop
