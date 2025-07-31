from tkinter  import*
root=Tk()
root.geometry("400x400")
root.title("Simple Calculator")

f_lbl=Label(root,text="First  Number=")
f_lbl.pack()

e1=Entry(root)
e1.pack()

s_lbl=Label(root,text="Second  Number=")
s_lbl.pack()

e2=Entry(root)
e2.pack()

res=Label(root,text="Result appers here")
res.pack()

def add():
    n1=float(e1.get())
    n2=float(e2.get())
    result=n1+n2
    print(result)
    res["text"]=str(result)

def sub():
    n1=float(e1.get())
    n2=float(e2.get())
    result=n1-n2
    print(result)
    res["text"]=str(result)

def multiple():
    n1=float(e1.get())
    n2=float(e2.get())
    result=n1*n2
    print(result)
    res["text"]=str(result)

def div():
    n1=float(e1.get())
    n2=float(e2.get())
    result=round((n1/n2),2)
    print(result)
    res["text"]=str(result)

def reset():
    e1.delete(0,END)
    e2.delete(0,END)
    res.config(text="")

b_add=Button(root,text="Addition",command=add)
b_add.pack()
b_sub=Button(root,text="Substraction",command=sub)
b_sub.pack()
b_multiple=Button(root,text="Multiplication",command=multiple)
b_multiple.pack()
b_div=Button(root,text="Division",command=div)
b_div.pack()
b_reset=Button(root,text="Reset",command=reset)
b_reset.pack()


root.mainloop()