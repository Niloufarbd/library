import backend
from tkinter import*

from datetime import datetime,timedelta
import  tkinter.messagebox

def clearList1():
    listBox1.delete(0, END)
def clearList2():
    listBox2.delete(0,END)
def clearList3():
    listBox3.delete(0,END)

def fellList1(books):
    for book in books:
        listBox1.insert(END, book)
def fellList2(members):
    for m in members:
        listBox2.insert(END,m)
def fellList3(management):
    for m in management:
        listBox3.insert(END,m)

win = Tk()
win.title("Library")
win.geometry("500x400")
win.resizable(width=False, height=False)

name_text=StringVar()
book_text=StringVar()
expire_text=StringVar()

nameM=StringVar()
familyM=StringVar()
birthM=StringVar()
codeM=StringVar()

name_t=StringVar()
family_t=StringVar()
tahsilat_t=StringVar()


labela=Label(win,text="books",foreground="white",background="blue",width=10)
labela.place(x=30,y=2)

label1=Label(win,text="book")
label1.place(x=5 , y=25)
book_text=StringVar()
EntryLabel1=Entry(win,textvariable=book_text)
EntryLabel1.place(x=45,y=25,width=50)

label2=Label(win,text="writer")
label2.place(x=5 , y=45)
teacher_text=StringVar()
EntryLabel2=Entry(win,textvariable=teacher_text)
EntryLabel2.place(x=45,y=45,width=50)

label3=Label(win,text="year")
label3.place(x=5 , y=70)
year_text=StringVar()
EntryLabel3=Entry(win,textvariable=year_text)
EntryLabel3.place(x=45,y=70,width=50)

label4=Label(win,text="isbn")
label4.place(x=5 , y=95)
isbn_text=StringVar()
EntryLabel4=Entry(win,textvariable=isbn_text)
EntryLabel4.place(x=45,y=95,width=50)

listBox1 = Listbox(win,width=20,height=15)
listBox1.place(x=5,y=120)

scr=Scrollbar(win)
scr.place(x=135,y=200)
listBox1.configure(yscrollcommand=scr.set)
scr.configure(command=listBox1.yview)



def get_selected_row(event):
     global SelectedROW

     if len(listBox1.curselection())>0:
        index = listBox1.curselection()[0]
        #print(index)
        SelectedROW = listBox1.get(index)
        EntryLabel1.delete(0, END)

        EntryLabel1.insert(END, SelectedROW[1])

        EntryLabel2.delete(0, END)
        EntryLabel2.insert(END, SelectedROW[2])

        EntryLabel3.delete(0, END)
        EntryLabel3.insert(END, SelectedROW[3])

        EntryLabel4.delete(0, END)
        EntryLabel4.insert(END,SelectedROW[4])

listBox1.bind("<<ListboxSelect>>", get_selected_row)

labela=Label(win,text="members",foreground="white",background="blue",width=10)
labela.place(x=180,y=2)

label5=Label(win,text="name")
label5.place(x=160 , y=25)
nameM=StringVar()
EntryLabel5=Entry(win,textvariable=nameM)
EntryLabel5.place(x=205,y=25,width=50)

label6=Label(win,text="family")
label6.place(x=160 , y=45)
familyM=StringVar()
EntryLabel6=Entry(win,textvariable=familyM)
EntryLabel6.place(x=205,y=45,width=50)

label7=Label(win,text="birth")
label7.place(x=160 , y=70)
birthM=StringVar()
EntryLabel7=Entry(win,textvariable=birthM)
EntryLabel7.place(x=205,y=70,width=50)

label8=Label(win,text="code")
label8.place(x=160 , y=95)
codeM=StringVar()
EntryLabel8=Entry(win,textvariable=codeM)
EntryLabel8.place(x=205,y=95,width=50)

listBox2=Listbox(win,width=15,height=15)
listBox2.place(x=160,y=120)

scr2=Scrollbar(win)
scr2.place(x=260,y=200)
listBox2.configure(yscrollcommand=scr2.set)
scr2.configure(command=listBox2.yview)


def get_selected_row2(event):
    global Selectedrow

    if len(listBox2.curselection())>0:
        index = listBox2.curselection()[0]
        # print(index)
        Selectedrow = listBox2.get(index)

        EntryLabel5.delete(0, END)
        EntryLabel5.insert(END, Selectedrow[1])

        EntryLabel6.delete(0, END)
        EntryLabel6.insert(END, Selectedrow[2])

        EntryLabel7.delete(0, END)
        EntryLabel7.insert(END, Selectedrow[3])

        EntryLabel8.delete(0, END)
        EntryLabel8.insert(END, Selectedrow[4])


listBox2.bind("<<ListboxSelect>>", get_selected_row2)

lebleC=Label(win,text="Management",width=10,foreground="white",background="blue")
lebleC.place(x=290,y=2)

leble9=Label(win,text="name")
leble9.place(x=270,y=25)
entrylabel9=Entry(win,textvariable=name_t)
entrylabel9.place(x=313,y=28,width=50)

leble10=Label(win,text="family")
leble10.place(x=270,y=50)
entrylabel10=Entry(win,textvariable=family_t)
entrylabel10.place(x=313,y=50,width=50)

leble11=Label(win,text="tahsilat")
leble11.place(x=270,y=72)
entrylabel11=Entry(win,textvariable=tahsilat_t)
entrylabel11.place(x=313,y=72,width=50)

listBox3=Listbox(win,width=15,height=15)
listBox3.place(x=275,y=120)
scr2=Scrollbar(win)
scr2.place(x=370,y=200)
listBox3.configure(yscrollcommand=scr2.set)
scr2.configure(command=listBox3.yview)


def  get_selected_row3(event):

    global Selected

    if len(listBox3.curselection())>0:
        index = listBox3.curselection()[0]
        Selected = listBox3.get(index)

        entrylabel9.delete(0, END)
        entrylabel9.insert(END, Selected[1])

        entrylabel10.delete(0, END)
        entrylabel10.insert(END,Selected[2])

        entrylabel11.delete(0, END)
        entrylabel11.insert(END, Selected[3])


listBox3.bind("<<ListboxSelect>>", get_selected_row3)

def view_command():
    clearList1()
    books = backend.viewall1()
    fellList1(books)
    clearList2()
    members=backend.viewall2()
    fellList2(members)
    clearList3()
    management=backend.viewall3()
    fellList3(management)

b1=Button(win,text="view all",width=10,command=view_command)
b1.place(x=410,y=85)

bookes = book_text.get()
teacheres = teacher_text.get()
yeares = year_text.get()
isbnes = isbn_text.get()

nemes = nameM.get()
familyMes = familyM.get()
birthMes = birthM.get()
codeMes = codeM.get()

name_tes = name_t.get()
family_tes = family_t.get()
tahsilat_tes = tahsilat_t.get()

def search_command():
    clearList1()
    clearList2()
    clearList3()
    books=backend.search1(book_text.get(),teacher_text.get(),year_text.get(),isbn_text.get())
    fellList1(books)
    members=backend.search2(nameM.get(),familyM.get(),birthM.get(),codeM.get())
    fellList2(members)
    management=backend.search3(name_t.get(),family_t.get(),tahsilat_t.get())
    fellList3(management)
b2=Button(win,text="search",width=10,command=search_command)
b2.place(x=410,y=120)



def add_command():
    bookes = book_text.get()
    teacheres = teacher_text.get()
    yeares = year_text.get()
    isbnes = isbn_text.get()


    if bookes == "": bookes ="___"
    if teacheres == "": teacheres = "___"
    if yeares == "" : yeares = "___"
    if isbnes == "" : isbnes = "___"

    book = backend.insert1(bookes, teacheres, yeares, isbnes)
    nemes = nameM.get()
    familyMes = familyM.get()
    birthMes = birthM.get()
    codeMes = codeM.get()

    if nemes == "": nemes = "___"
    if familyMes == "": familyMes = "___"
    if birthMes == "" : birthMes = "___"
    if codeMes == "" : codeMes = "___"

    member = backend.insert2(nemes, familyMes, birthMes, codeMes)
    name_tes = name_t.get()
    family_tes = family_t.get()
    tahsilat_tes = tahsilat_t.get()

    if name_tes == "": name_tes = "___"
    if family_tes == "": family_tes = "___"
    if tahsilat_tes == "" : tahsilat_tes = "___"

    management = backend.insert3(name_tes, family_tes, tahsilat_tes)
    a = backend.deleteEmptyRows()
    b =backend.deleteEmptyRows1()
    c = backend.deleteEmptyRows2()
    view_command()


b3=Button(win,text="Add",width=10,command= add_command)
b3.place(x=410,y=155)

def update_command():
    backend.update1(SelectedROW[0],book_text.get(),teacher_text.get(),year_text.get(),isbn_text.get())
    view_command()
    backend.update2(Selectedrow[0],nameM.get(),familyM.get(),birthM.get(),codeM.get())
    view_command()
    backend.update3(Selected[0],name_t.get(),family_t.get(),tahsilat_t.get())
    view_command()

b4=Button(win,text="update",width=10,command=update_command)
b4.place(x=410,y=190)

def delete_command():
    backend.delete1(SelectedROW[0])
    view_command()
    backend.delete2(Selectedrow[0])
    view_command()
    backend.delete3(Selected[0])
    view_command()

b5=Button(win,text="Delete",width=10,command=delete_command)
b5.place(x=410,y=225)

start=datetime.now()
end = start + timedelta(days=10)
Expiretime = (end - start)
Finally = Expiretime.days

def erroemsg(ms):
    if ms=="this book dont reserv":
        tkinter.messagebox.showerror('Error',f'you can not reserv,this book will be released in after {Finally} days')
    elif ms=="this book was reserv":
         tkinter.messagebox.showinfo('successful','The desired book was reserved')



def reserv_command():
    book = backend.insert4(SelectedROW[1],SelectedROW[0],Finally  )
    b=backend.check()
    c=backend.deleteRuw()


    if b:
        erroemsg("this book dont reserv")
    else:
        erroemsg("this book was reserv")

    view_command()


b6=Button(win,text="borrow",width=10,command=reserv_command)
b6.place(x=410,y=260)


b7=Button(win,text="Close",width=10,command=win.destroy)
b7.place(x=410,y=295)


view_command()
win.mainloop()

