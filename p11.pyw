from tkinter import Tk,Button,Label,DoubleVar,Entry

window = Tk()
window.title("Meter App")
window.configure(background = "light blue")
window.geometry("520x360")
window.resizable(width = False,height = False)

def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)

def clear():
    ft_value.set("")
    mt_value.set("")

ft_ld1 = Label(window,text="Feet",bg="red",fg="white",width = 18)
ft_ld1.grid(column=1,row=1,padx=75,pady=75)

ft_value = DoubleVar()
ft_entry = Entry(window,textvariable=ft_value,width=18)
ft_entry.grid(column=2,row = 1)
ft_entry.delete(0,'end')

mt_ld1 = Label(window,text="meter",bg="purple",fg="white",width = 18)
mt_ld1.grid(column=1,row=2,padx=75,pady=1)

mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=18)
mt_entry.grid(column=2,row = 2)
mt_entry.delete(0,'end')

c_btn = Button(window,text='Convert',bg='green',fg='white',width = 18,command=convert)
c_btn.grid(column=1,row = 3,padx = 20,pady = 55)

c_btn = Button(window,text='Clear',bg='violet',fg='white',width = 18,command=clear)
c_btn.grid(column=2,row = 3,padx = 20,pady = 55)

window.mainloop()