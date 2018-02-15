from Tkinter import *
def print_me():
    print 'HI'
##root=Tk()
##B1=Button(root,text='Print HI',command=print_me)
##B1.pack()
##root.mainloop()
root1=Tk()
L1=Label(text='name');
L1.pack()
E1=Entry();
E1.pack()

L2=Label(text='place');
L2.pack()
E2=Entry();
E2.pack()

L3=Label(text='course');
L3.pack()
E3=Entry();
E3.pack()

def data():
    print(E1.get())
    print(E2.get())
    print(E3.get())
B2=Button(root1,text='Submit',command=data)
B2.pack()
root1.mainloop()

