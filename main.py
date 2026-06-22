from tkinter import *

def calculate_fee():
    if hours.get() == "2":
        fee.set("Rs. 18000")

    elif hours.get() == "3":
        fee.set("Rs. 53000")     

    elif hours.get() == "4":
        fee.set("Rs. 75000")

root = Tk()
root.title("Fee Calculator")
root.geometry("350x300") 

Label(root, text= "Fee Calculator"
      font= ("Aerial", 16, "bold")).pack(pady=10)

gender = StringVar()
gender.set("Male")

Label(root, text="Select gender").pack()

Radiobutton(root,
            text ="Male",
            variable=gender,
            value="Male").pack()

Radiobutton(root,
            text="Female",
            variable=gender,
            value="Female").pack()

hours = StringVar()
hours.set("2")

Label(root, text="Credit hours").pack(pady=10)
OptionMenu(root, hours, "2", "3", "4").pack()



