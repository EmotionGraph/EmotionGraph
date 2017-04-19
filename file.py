import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

#try:

file_path = filedialog.askopenfilename(filetypes=(("Text Files","*.txt"),("All","*.*")))
print(file_path)
#except:                   # <- naked except is a bad idea
#    print("Open Source File", "Failed to read file" )
        
