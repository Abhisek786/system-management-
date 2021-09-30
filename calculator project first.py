# It is used to import all the required modules for our calculator
from tkinter import*

# Then let's create window
win = Tk()

# Setting a name and icon for the window
win.title("CALCULATOR")
win.iconbitmap("calculator.ico")


# Creating a  box to display the all the content
e = Entry(win, font=('Helvetica', 20, 'bold'), bd=30, insertwidth=4, bg='grey67', width=30, borderwidth=20, justify='right')
e.grid(columnspan=5)

# Setting size of the window
x = 500
y = 450
win.geometry(f"{x}x{y}")

# Open the file
file0 = open('abc.txt', 'w')

# Write on the file
file0.write("")

# Close the file
file0.close()


# Delete a character from the display
def b_del():
    current_number = e.get()
    length = len(current_number) - 1
    e.delete(length, END)

# To show the previous calculations
def show():
    global x
    global y
    # Saving the data to a file
    file0 = open('abc.txt', 'r+')
    data_var = file0.read()
    file0.write('\n')
    # Close the file
    file0.close()

    # Display what's in the file
    Label(win, text=data_var,font=("PT Sans",20,'bold'), bg="grey").grid(columnspan=5,rowspan=6)

    # Extend the size of window to show history
    win.geometry(f"{x}x{y}")


# All the number buttons
def buttonclick(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(num)) # Concatinate the strings

# Clear the screen
def btn_cls():
    e.delete(0,END)

# Add
def btn_add():
    firstnum=e.get()
    global math
    global fnum
    math = "add"
    fnum = int(firstnum)
    e.delete(0,END)

# Multiply
def btn_mul():
    firstnum=e.get()
    global math
    global fnum
    math="mul"
    fnum=int(firstnum)
    e.delete(0,END)


# Subtract
def btn_sub():
    firstnum=e.get()
    global math
    global fnum
    math="sub"
    fnum=int(firstnum)
    e.delete(0,END)


# Divide
def btn_div():
    firstnum=e.get()
    global math
    global fnum
    math="div"
    fnum=int(firstnum)
    e.delete(0,END)

# Modulus
def btn_mod():
    firstnum = e.get()
    global math
    global fnum
    math = "mod"
    fnum = int(firstnum)
    e.delete(0, END)

# Power
def btn_pwr():
    firstnum = e.get()
    global math
    global fnum
    math = "pwr"
    fnum = int(firstnum)
    e.delete(0, END)


# Check operator and display the result
def btn_equal():
   global y
   snum = int(e.get())
   e.delete(0, END)
   y+=32
   file0 = open('abc.txt', 'r+')
   file0.read()
   file0.write(str(fnum))
   file0.close()

   if math == "mul":
       m = fnum * snum
       e.insert(0, m)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" * " + str(snum) + ' = ' + str(m) + "\n")
       file0.close()

   elif math == "sub":
       s = fnum - snum
       e.insert(0, s)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" - " + str(snum) + ' = ' + str(s) + "\n")
       file0.close()

   elif math == "add":
       a = fnum+snum
       e.insert(0, a)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" + " + str(snum) + ' = ' + str(a) + "\n")
       file0.close()

   elif math == "div":
       d = fnum/snum
       e.insert(0, d)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" / " + str(snum) + ' = ' + str(d) + "\n")
       file0.close()

   elif math == "mod":
       d = fnum % snum
       e.insert(0, d)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" % " + str(snum) + ' = ' + str(d) + "\n")
       file0.close()

   elif math == "pwr":
       d = fnum ** snum
       e.insert(0, d)
       file0 = open('abc.txt', 'r+')
       file0.read()
       file0.write(" ^ " + str(snum) + ' = ' + str(d) + "\n")
       file0.close()


# All the required buttons
btn1 = Button(win,text="1",padx=20,pady=10,command=lambda : buttonclick(1),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn2 = Button(win,text="2",padx=20,pady=10,command=lambda : buttonclick(2),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn3 = Button(win,text="3",padx=20,pady=10,command=lambda : buttonclick(3),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn4 = Button(win,text="4",padx=20,pady=10,command=lambda : buttonclick(4),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn5 = Button(win,text="5",padx=20,pady=10,command=lambda : buttonclick(5),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn6 = Button(win,text="6",padx=20,pady=10,command=lambda : buttonclick(6),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn7 = Button(win,text="7",padx=20,pady=9,command=lambda : buttonclick(7),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn8 = Button(win,text="8",padx=20,pady=10,command=lambda : buttonclick(8),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn9 = Button(win,text="9",padx=20,pady=10,command=lambda : buttonclick(9),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btn0 = Button(win,text="0",padx=20, pady=9,command=lambda : buttonclick(0),bg='red',fg='black',bd=7,font=("PT Serif",20,'bold'))
btnequal=Button(win,text="=",padx=26,pady=17,command=btn_equal,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))
btnadd=Button(win,text="+",padx=28,pady=18, command=btn_add,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))
btnpwr=Button(win,text="^",padx=26,pady=16,command=btn_pwr,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))
btnsub=Button(win,text="-",padx=28,pady=18,command=btn_sub,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))
btndiv=Button(win,text="/",padx=28,pady=18,command=btn_div,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))
btnmul=Button(win,text="*",padx=27,pady=17,command=btn_mul,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))
btncls=Button(win,text="C",padx=25,pady=17,command=btn_cls,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))
btnmod=Button(win,text="mod",padx=14,pady=17,command=btn_mod,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))
history_btn = Button(win, text='History', padx=5, pady=20, command=show,bg='black',fg='white',bd=7,font=("PT Serif", 12,'bold'))
bdel = Button(win, text="←", padx=23, pady=16, command=b_del,bg='black',fg='white',bd=7,font=("PT Serif", 15,'bold'))


# First row
btn7.grid(column=0, row=3, padx=5, pady=5)
btn8.grid(column=1, row=3, padx=5, pady=5)
btn9.grid(column=2, row=3, padx=5, pady=5)
btncls.grid(column=3, row=3, padx=5, pady=5)
bdel.grid(column=4, row=3, padx=5, pady=5)

# Second row
btn4.grid(column=0, row=4, padx=5, pady=5)
btn5.grid(column=1, row=4, padx=5, pady=5)
btn6.grid(column=2, row=4, padx=5, pady=5)
btnsub.grid(column=3, row=4, padx=5, pady=5)
btnmod.grid(column=4, row=4, padx=5, pady=5)

# Third row
btn1.grid(column=0,row=5, padx=5, pady=5)
btn2.grid(column=1,row=5, padx=5, pady=5)
btn3.grid(column=2,row=5, padx=5, pady=5)
btndiv.grid(column=3,row=5, padx=5, pady=5)
btnadd.grid(column=4,row=5, padx=5, pady=5)

# Fourth row
history_btn.grid(column=0, row=6, padx=5, pady=5)
btn0.grid(column=1, row=6, padx=5, pady=5)
btnmul.grid(column=2,row=6, padx=5, pady=5)
btnpwr.grid(column=3, row=6, padx=5, pady=5)
btnequal.grid(column=4,row=6, padx=5, pady=5)

# Changing the background color of the window
win.config(bg="grey")

win.mainloop()