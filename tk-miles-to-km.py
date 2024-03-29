# Tkinter - Miles to kilometers conversion

import tkinter as tk 
# from tkinter import ttk 
import ttkbootstrap as ttk

def convert():
    result = entry_int.get() * 1.61
    output_string.set(f'{result:.2f} kms')

# window
window = tk.Tk()
window.title('LEARNING TKINTER')
window.geometry('300x200')

# title 
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 22 bold')
title_label.pack(pady = 15)

# input field 
input_frame = ttk.Frame(master = window)
input_frame.pack(pady = 10)

# entry
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
entry.pack(side = 'left', padx = 10)

# button
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
button.pack(side = 'left')

# output 
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 22', textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()