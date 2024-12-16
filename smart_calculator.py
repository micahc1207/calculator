#Calculator

#import tkinter module
import tkinter as tk

#Addition Function

  
def add():
 total = int(num1.get()) + int(num2.get())
 output.delete(0,tk.END)
 output.insert(0,total)

def sub():
  total = int(num1.get()) - int(num2.get())
  output.delete(0,tk.END)
  output.insert(0,total)

def multiply():
  total = int(num1.get()) *  int(num2.get())
  output.delete(0,tk.END)
  output.insert(0,total)

def div():
 total = int(num1.get()) /  int(num2.get())
 output.delete(0,tk.END)
 output.insert(0,total)

  
   

        
        

#set variable for loop execution
window = tk.Tk()



#Creating a frame. Where you can place widgets on the GUI
frame_a = tk.Frame(master=window , width=200, height=210, background= "blue")

#Header line for cacluator
header = tk.Label( master= frame_a , text = "Welcome to Micah's Calculator", background= "blue", fg="white")
header.place(x=0, y=0)

#Get first number
num1_label = tk.Label( master= frame_a, text = "Enter first number", background="blue", fg="white")
num1= tk.Entry(master=frame_a, width= 6)
num1_label.place(x=0, y=45)
num1.place(x=100, y=45)




#Get second number
num2_label = tk.Label(master=frame_a, text="Enter second number", bg= "blue", fg="white")
num2 = tk.Entry(master=frame_a , width = 6)
num2_label.place(x=0, y=75)
num2.place(x=120, y=75)


#BUTTONS for math functions

#----ADDITION
add_button = tk.Button(master= frame_a ,text="+",command=add)
add_button.place(x = 0, y = 150)

#----SUBTRACTION
subtract_button = tk.Button(master= frame_a, text="-", command=sub)
subtract_button.place (x = 20 , y = 150)

#----Multiplication
multiply_button = tk.Button(master=frame_a, text="x", command=multiply)
multiply_button.place (x=40, y=150)


#---- Division
division_button = tk.Button(master=frame_a, text="%", command=div)
division_button.place(x=60, y=150)

#Output box
output = tk.Entry(master= frame_a , width= 20)
output.place(x=0, y=180)



#Placing the frame on the GUI and in what order
frame_a.pack()


#To run the app
window.mainloop()
    