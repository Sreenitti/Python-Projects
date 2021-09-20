import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog

'''similar to root=Tk() 
can also be given as 

import tkinter as Hi
window = Hi.Tk()
    (or)
from tkinter import *
window = Tk() '''
 
''' creating a function which allows us to open a file in our 
computer and returns the path of the file '''
def open_file() :
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file to compress ")
    return filename 


def compression(i,o) :
    compress(i,o)

def decompression(i,o) :
    decompress(i,o)

window = tk.Tk()
window.title("Compression and Decompression Engine")
window.geometry("600x400")

#COMPRESSION PART

output_label = tk.Label(window, text="Name of compressed file")
output_label.grid(row=2, column=0)
output_entry = tk.Entry(window)
output_entry.grid(row=2,column=1)

button1 = tk.Button(window, text="Compress", command=lambda:compression(open_file(), output_entry.get()))
button1.grid(row=3,column=1)

#DECOMPRESSION PART

out_label = tk.Label(window, text="Name of the decompressed file")
out_label.grid(row=4,column=0)
out_entry = tk.Entry(window)
out_entry.grid(row=4, column=1)
button2 = tk.Button(window, text="Decompress", command= lambda:decompression(open_file(), out_entry.get()))
button2.grid(row=5,column=1)

window.mainloop()