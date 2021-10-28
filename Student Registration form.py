from tkinter import *
from tkinter import messagebox as tkMessageBox

root = Tk()

root.geometry("500x700")
root.title('Student Registration form')


label_0 =Label(root,text="Student Registration form", width=20, font=("bold",20))
label_0.place(x=90,y=60)

label_1 =Label(root,text="Student Name", width=20, font=("bold",10))
label_1.place(x=70,y=130)

entry_2=Entry(root)
entry_2.place(x=240,y=130)

label_3 =Label(root,text="Father's Name", width=20, font=("bold",10))
label_3.place(x=70,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

label_4 =Label(root,text="Mother's Name", width=20, font=("bold",10))
label_4.place(x=70,y=230)

entry_4=Entry(root)
entry_4.place(x=240,y=234)

label_5 =Label(root,text="School Name", width=20, font=("bold",10))
label_5.place(x=70,y=281)

entry_5=Entry(root)
entry_5.place(x=240,y=284)

label_6 =Label(root,text="Class", width=20, font=("bold",10))
label_6.place(x=60,y=330)


list_of_class=[ '1 Class' ,'2 Class' , '3 Class' ,'4 Class' ,'5 Class' ,'6 Class' ,'7 Class' ,'8 Class' ,'9 Class' ,'10 Class' ]

class_var=StringVar()

droplist=OptionMenu(root, class_var, *list_of_class)
droplist.config(width=20)

class_var.set('Select your Class')
droplist.place(x=230,y=328)

label_7 =Label(root,text="Parents Contact Number", width=20, font=("bold",10))
label_7.place(x=70,y=380)

entry_7=Entry(root)
entry_7.place(x=240,y=380)

label_8 =Label(root,text="Gender", width=20, font=("bold",10))
label_8.place(x=70,y=425)

gender_var=IntVar()
gender_list = ["Male", "Female"]

Radiobutton(root, text=gender_list[0], padx= 5, variable= gender_var, value=0).place(x=240,y=425)
Radiobutton(root, text=gender_list[1], padx= 20, variable= gender_var, value=1).place(x=295,y=425)

label_9 =Label(root,text="Date of Birth of Student", width=20, font=("bold",10))
label_9.place(x=70,y=470)

entry_9=Entry(root)
entry_9.place(x=240,y=475)

label_10 =Label(root,text="Country", width=20, font=("bold",10))
label_10.place(x=70,y=515)

list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austrelia' ,'China' ,'Japan' ,'Sri lanka' ]

country_var=StringVar()

droplist=OptionMenu(root, country_var, *list_of_country)
droplist.config(width=20)

country_var.set('Select your Country')
droplist.place(x=230,y=515)

def process():
    f = open("user-registration-details.txt", "a")

    student  = entry_2.get()
    father  = entry_3.get()
    mother  = entry_4.get()
    school = entry_5.get()
    Class  = class_var.get()
    parents  = entry_7.get()
    gender = gender_list[gender_var.get()]
    date  = entry_9.get()
    country = country_var.get()

    content_to_save = "{},{},{},{},{},{},{},{},{}\n".format(student ,father ,mother ,school ,Class ,parents ,gender ,date ,country)
    f.write(content_to_save)    
    f.close()

    print("Record saved")

    tkMessageBox.showinfo("Response Box", "Details Saved Successfully")


Button(root, text='Submit', width=20, bg="yellow", fg='red', command=process).place(x=160,y=590)

root.mainloop()

















