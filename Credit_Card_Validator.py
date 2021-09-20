from tkinter import *

def validate(card_no) :
    odd_sum = 0
    even_sum = 0 
    double_list = []
    number = list(card_no)
    for index, val in enumerate(number) :
        if index%2 !=0 :  # odd index number
            odd_sum += int(val)
        else : # even index number
            double_list.append(int(val)*2)

# converting double_list into string 
    double_string = ""
    for i in double_list :
        double_string += str(i)

    # converting double_string back into list 
    double_list = list(double_string)

    for x in double_list :
        even_sum += int(x)

    net_sum = odd_sum + even_sum
    listbox = Listbox(canvas, width=40, height=1)
    canvas.create_window(200, 200, window=listbox)
    if net_sum%10 == 0 :
        listbox.insert(END, "This is a valid credit card number.")
    else :
        listbox.insert(END, "This is not a valid credit card number.")
        

root = Tk()
root.title("Credit Card Validator")

canvas = Canvas(root, width=400, height=250) 
canvas.pack()

title = Label(root, text="Credit Card Validator", font=("Comic Sans MS", 20), fg="Brown")
canvas.create_window(200, 20, window=title )

label = Label(root, text="Enter credit card number ")
canvas.create_window(100, 100, window=label )
entry = Entry(root)
canvas.create_window(250,100, window=entry)
button = Button(root, text="Validate", command=lambda :validate(entry.get()))
canvas.create_window(200, 150, window=button)

root.mainloop()
