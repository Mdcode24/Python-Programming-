from  tkinter  import *
root=Tk()
root.geometry("300x200")
root.title("Converter  of  string  to  ascii")

f_lbl=Label(root,text="Enter:")
f_lbl.pack()

e1=Entry(root)
e1.pack()

res=Label(root,text="Conversion is  printed  here")
res.pack()


def ascii():
    s1=e1.get()
    for char in s1:
        #len(s1)=str(ord(char))
        res["text"]=str(ord(char))

def string():
    s1=e1.get()
    for value in s1:
        ascii=[ord(value)]
        res["text"] = ' '.join(map(str, ascii)) 

def reset():
    e1.delete(0,END)
    res.config(text="")


b_ascii=Button(root,text="Ascii",command=ascii)
b_ascii.pack()
b_string=Button(root,text="String",command=string)
b_string.pack()
b_reset=Button(root,text="Reset",command=reset)
b_reset.pack()
root.mainloop()
