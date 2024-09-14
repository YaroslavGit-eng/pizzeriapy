from tkinter import *

def calculate_cost():
    basic_price = 20 
    size = 0.75 if pr12_var.get() == 1 else 1.25 
    selected = [
        ("Помідори", pr1_var.get() * 5),
        ("Сир", pr2_var.get() * 10),
        ("Курка", pr3_var.get() * 15),
        ("Ананас", pr4_var.get() * 10),
        ("Кукурудза", pr5_var.get() * 5),
        ("Гриби", pr6_var.get() * 10),
    ]
    cost = sum(price for name, price in selected)
    total_cost = size * (basic_price + cost)
    result_label.config(text=f"Вартість піци: {total_cost:.2f} гривень")

w = Tk()
w.title("Найпростіше вікно")
w.minsize(400, 400)

nadpis = Label(w, text="Піцерія", font="Times 32")
nadpis.pack()

pr1_var = IntVar()
pr2_var = IntVar()
pr3_var = IntVar()
pr4_var = IntVar()
pr5_var = IntVar()
pr6_var = IntVar()

pr1 = Checkbutton(w, text="Помідори", font="Arial 18", fg="navy", variable=pr1_var, command=calculate_cost)
pr1.pack()

pr2 = Checkbutton(w, text="Сир", font="Arial 18", fg="navy", variable=pr2_var, command=calculate_cost)
pr2.pack()

pr3 = Checkbutton(w, text="Курка", font="Arial 18", fg="navy", variable=pr3_var, command=calculate_cost)
pr3.pack()

pr4 = Checkbutton(w, text="Ананас", font="Arial 18", fg="navy", variable=pr4_var, command=calculate_cost)
pr4.pack()

pr5 = Checkbutton(w, text="Кукурудза", font="Arial 18", fg="navy", variable=pr5_var, command=calculate_cost)
pr5.pack()

pr6 = Checkbutton(w, text="Гриби", font="Arial 18", fg="navy", variable=pr6_var, command=calculate_cost)
pr6.pack()

pr12_var = IntVar()

pr12 = Radiobutton(w, text="Мала", font="Arial 18", fg="navy", variable=pr12_var, value=1, command=calculate_cost)
pr12.pack()

pr13_var = IntVar()
pr13 = Radiobutton(w, text="Велика", font="Arial 18", fg="navy", variable=pr12_var, value=0, command=calculate_cost)
pr13.pack()

result_label = Label(w, text="", font="Arial 18")
result_label.pack()

w.mainloop()
