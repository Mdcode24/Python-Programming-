from tkinter import *
import ephem

root=Tk()
root.geometry("300x400")
root.title("Know next sunrise and sunset in city")

c=Label(root,text="Enter city:")
c.pack()

c_e=Entry(root)
c_e.pack()


res=Entry(root)
res.pack()


def sunrise():
    city_name=c_e.get()
    for i in database:
        if  i==city_name:
            sunrise=i['sunrise']
            res["text"]=f"sunrise:{sunrise}"
        break
    else:
        res["text"]="City not found in list"


def sunset():
    city_name=c_e.get()
    for e in database:
        if  e==city_name:
            sunset=e['sunset']
            res["text"]=f"Sunset: {sunset}"
        break
    else:
        res["text"]="City not found in list"


def reset():
    c_e.delete(0,END)
    res.config(text="")
    

b_sunrise=Button(root,text="Sunrise",command=sunrise)
b_sunrise.pack()
b_sunset=Button(root,text="Sunset",command=sunset)
b_sunset.pack()
b_reset=Button(root,text="Reset",command=reset)
b_reset.pack()
root.mainloop()