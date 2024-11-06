from tkinter import *
import test

def clear_list():
    listbox.delete(0, END)

def fill_list(books, listbox):
    for book in books:
        listbox.insert("end",book)



win=Tk()

win.geometry("600x500")


lb1=Label(win,text="title")
lb1.grid(row=0,column=0)

lb1=Label(win,text="author")
lb1.grid(row=1,column=0)

lb1=Label(win,text="year")
lb1.grid(row=2,column=0)



title_text=StringVar()
author_text=StringVar()
year_text=StringVar()

e1=Entry(win,textvariable=title_text)
e1.grid(row=0,column=1)

e1=Entry(win,textvariable=author_text)
e1.grid(row=1,column=1)

e1=Entry(win,textvariable=year_text)
e1.grid(row=2,column=1)


def listbox(win, width,height):
    pass

listbox = Listbox(win, width=45, height=10)
listbox.grid(row=0, column=9, rowspan=10, columnspan=2)


def get_selected_row(event):
    global selected_Book
    if len (list1.curselection())>0:
        index=list1.curselection()[0]
        selected_book=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_Book[1])

    e1.delete(0, END)
    e1.insert(END, selected_Book[2])

    e1.delete(0, END)
    e1.insert(END, selected_Book[3])

    e1.delete(0, END)
    e1.insert(END, selected_Book[4])
def view_command():
   clear_list()

   books = test.view()
   fill_list(books,listbox)



b1=Button(win,text="view All",width=12,command=view_command)
b1.grid(row=12,column=1,pady=5)

def search_command(year_text=None):
    clear_list() 
    books = test.search(title_text.get(),author_text.get(),year_text.get())  # جستجو در دیتابیس
    fill_list(books)

b2=Button(win,text="selected Entry",width=12,command=search_command)
b2.grid(row=13,column=1,pady=5)

def add_command():
    test.insert(title_text.get(),author_text.get(),year_text.get())
    view_command()

b3=Button(win,text="Add Entry",width=12,command=add_command)
b3.grid(row=15,column=1,pady=5)

def update_command(selected_Book):
    test .update(selected_Book[0],title_text.get(),author_text.get(),year_text.get())
    view_command()

b4=Button(win,text="UpdateSelected",width=12,command=update_command)
b4.grid(row=18,column=1,pady=5)

def delete_command():
    test.delete(get_selected_row()[0])
    view_command()


b5=Button(win,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=21,column=1,pady=5)

b6=Button(win,text="close",width=12,command=win.destroy)
b6.grid(row=28,column=1,pady=5)















win.mainloop()