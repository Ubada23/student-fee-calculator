from tkinter import *

def calculate_fee():
    if hours.get() == "2":
        fee.set("Rs. 18,000")
    elif hours.get() == "3":
        fee.set("Rs. 51,500")
    elif hours.get() == "4":
        fee.set("Rs. 75,000")

def clear():
    fee.set("")
    gender.set("Male")
    hours.set("2")

root = Tk()
root.title("Student Fee Calculator")
root.geometry("380x380")
root.config(bg="#dbeafe")

Label(root, text="Student Fee Calculator",
      font=("Arial", 18, "bold"),
      bg="#dbeafe", fg="#1e3a8a").pack(pady=15)

gender = StringVar()
gender.set("Male")

Label(root, text="Select Gender",
      font=("Arial", 11, "bold"),
      bg="#dbeafe").pack()

Radiobutton(root, text="Male",
            variable=gender, value="Male",
            bg="#dbeafe").pack()

Radiobutton(root, text="Female",
            variable=gender, value="Female",
            bg="#dbeafe").pack()

hours = StringVar()
hours.set("2")

Label(root, text="Credit Hours",
      font=("Arial", 11, "bold"),
      bg="#dbeafe").pack(pady=10)

OptionMenu(root, hours, "2", "3", "4").pack()

Button(root, text="Calculate Fee",
       command=calculate_fee,
       bg="#2563eb", fg="white",
       font=("Arial", 10, "bold")).pack(pady=12)

Button(root, text="Clear",
       command=clear,
       bg="#ef4444", fg="white",
       font=("Arial", 10, "bold")).pack()

fee = StringVar()
Label(root, textvariable=fee,
      font=("Arial", 14, "bold"),
      bg="#dbeafe", fg="#111827").pack(pady=15)

root.mainloop()