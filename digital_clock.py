import tkinter as tk
from time import strftime 

root = tk.Tk()
root.title("Digital Clock")  # Fixed typo in title

def time():
    string = strftime('%H:%M:%S  %p \n %D')  # Fixed format specifier: %P → %p (lowercase am/pm)
    label.config(text=string) 
    label.after(1000, time)

# Fixed typo: 'Lable' → 'Label', and 'archor' → 'anchor'
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='red')
label.pack(anchor='center')

time()
root.mainloop()
