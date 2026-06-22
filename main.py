from tkinter import *

def calculate_fee():
    if hours.get() == "2":
        fee.set("Rs. 18,000")
    elif hours.get() == "3":
        fee.set("Rs. 51,500")
    elif hours.get() == "4":
        fee.set("Rs. 75,000")

root = Tk()
root.title("Student Fee Calculator")
root.geometry("350x300")

Label(root, text="Student Fee Calculator",
      font=("Arial", 16, "bold")).pack(pady=10)

gender = StringVar()
gender.set("Male")

Label(root, text="Select Gender").pack()
Radiobutton(root, text="Male",
            variable=gender, value="Male").pack()
Radiobutton(root, text="Female",
            variable=gender, value="Female").pack()

hours = StringVar()
hours.set("2")

Label(root, text="Credit Hours").pack(pady=10)
OptionMenu(root, hours, "2", "3", "4").pack()

Button(root, text="Calculate Fee",
       command=calculate_fee).pack(pady=10)

fee = StringVar()
Label(root, textvariable=fee,
      font=("Arial", 12, "bold")).pack()

root.mainloop()