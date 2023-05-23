from tkinter import *
pg = Tk()
pg.geometry("500x500")
pg.title("Arrays Multidimensionales")
pg.configure(background="#264653")

a1 = ["Juan","Pedro","Pancho"]
a2 = [["Juan","9.4/10"],["Pedro","8.6/10"],["Pancho","4.9/10"]]
a3 = [["Juan","9.4/10","perfecto!"],["Pedro","8.6/10", "muy bien"],["Pancho: ","4.9/10, ", "muy mal"]]

def fn1():
    lb1["text"] = a3[2][0] + a3[2][1] + a3 [2][2]
    print(a3[2][0] + a3[2][1] + a3 [2][2])

lb1 = Label(pg, text="a", bg="#e76f51", fg="white", font=200)
lb1.place(relx=0.5, rely=0.55, anchor=CENTER,)

bt1 = Button(pg, text="Ejecutar", bg="#e76f51", fg="white", command=fn1)
bt1.place(relx=0.5, rely=0.45, anchor=CENTER,)

pg.mainloop()
