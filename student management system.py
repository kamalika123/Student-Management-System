from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import filedialog
import time
from tkinter import ttk
from tkinter.ttk import Treeview
import pymysql
import pandas












def add_student():
    def submitadd():
        id = idval.get() 
        name = nameval.get() 
        mobile = mobileval.get()  
        email = emailval.get()  
        address = addressval.get()  
        gender = genderval.get() 
        dob = dobval.get()
        added_time = time.strftime('%H:%M:%S')
        added_date = time.strftime('%d/%m/%Y')
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,added_time,added_date))
            con.commit()
            res = messagebox.askyesnocancel('notification','id{} Name {} added succcessfully and want to clean form?'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('') 
                nameval.set('') 
                mobileval.set('')  
                emailval.set('')  
                addressval.set('')  
                genderval.set('') 
                dobval.set('') 

        except:
            messagebox.showerror('notifications','ID already exists,try another ID',parent=addroot)

        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vb)

        






        

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+200+150')
    addroot.title('Student Management System')
    addroot.config(bg='pink')
    addroot.resizable(False,False)

    ############# add student labels ###############333333
    idlabel = Label(addroot,text='Enter Id: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Phone No:  ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email Id: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    

    addresslabel = Label(addroot,text='Enter address: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter D.O.B: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    ################# ADD STUDENT ENTRY LABELS ####################################
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()



    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)


    ############################## ADD BUTTONS ##############################
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='gold',command=submitadd)
    submitbtn.place(x=150,y=420)

    



    addroot.mainloop()


def search_student():
    print('Student Search')
    def search():
        id = idval.get() 
        name = nameval.get() 
        mobile = mobileval.get()  
        email = emailval.get()  
        address = addressval.get()  
        gender = genderval.get() 
        dob = dobval.get()
        added_date = time.strftime('%d/%m/%Y')

        if(id != ''):
            strr = 'select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vb)

        if(name != ''):
            strr = 'select * from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vb)


        if(mobile != ''):
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vb)


        if(email != ''):
            strr = 'select * from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vb)

        if(address != ''):
            strr = 'select * from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vb)

        if(gender != ''):
            strr = 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vb)

        if(dob != ''):
            strr = 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vb)


        if(added_date != ''):
            strr = 'select * from studentdata1 where added_date=%s'
            mycursor.execute(strr,(added_date))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vb)

                

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+200+150')
    searchroot.title('Student Management System')
    searchroot.config(bg='pink')
    searchroot.resizable(False,False)

    ############# search student labels ###############333333
    idlabel = Label(searchroot,text='Enter Id: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Phone No:  ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter Email Id: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    

    addresslabel = Label(searchroot,text='Enter address: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text='Enter Gender: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text='Enter D.O.B: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(searchroot,text='Enter Date: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    ################# SEARCH STUDENT ENTRY LABELS ####################################
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()



    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)


    ############################## ADD BUTTONS ##############################
    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='gold',command=search)
    submitbtn.place(x=150,y=480)

    



    searchroot.mainloop()


def delete_student():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('notifications','Id {} deleted successfully'.format(pp))

    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vb = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vb)


def update_student():
    print('Student update')
    def update():
        
        id = idval.get() 
        name = nameval.get() 
        mobile = mobileval.get()  
        email = emailval.get()  
        address = addressval.get()  
        gender = genderval.get() 
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        # Update the database
        strr = 'update studentdata1 set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo('notifications', 'Id {} modified successfully...'.format(id))

        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vb = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vb)











    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x600+180+40')
    updateroot.title('Student Management System')
    updateroot.config(bg='pink')
    updateroot.resizable(False,False)

    ############# update student labels ###############333333
    idlabel = Label(updateroot,text='Enter Id: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Phone No:  ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter Email Id: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    

    addresslabel = Label(updateroot,text='Enter address: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text='Enter Gender: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text='Enter D.O.B: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text='Enter Date: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text='Enter Time: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    timelabel.place(x=10,y=490)



    ################# UPDATE STUDENT ENTRY LABELS ####################################
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()



    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)


    ############################## ADD BUTTONS ##############################
    submitbtn = Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='gold',command=update)
    submitbtn.place(x=150,y=550)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0]) 
        nameval.set(pp[1]) 
        mobileval.set(pp[2])  
        emailval.set(pp[3])  
        addressval.set(pp[4])  
        genderval.set(pp[5]) 
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    



    updateroot.mainloop()

def show_student():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vb = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vb)


def export_student():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,added_date,added_time=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),added_date.append(pp[7]),added_time.append(pp[8])

    dd = ['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,added_date,added_time)),columns=dd)   
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('notifications','student data is saved {}'.format(paths))


def exit_student():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if res == True:
        root.destroy()

    






def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('notifications','Data is Incorrect, please try again')
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('notification',' database created and now you are connected',parent=dbroot)
            
        except:

            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('notification','Now you are connected to the database',parent=dbroot)

        dbroot.destroy()    
           





        

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.resizable(False,False)
    dbroot.config(bg='pink')
    dbroot.geometry('470x250+800+220')

    #----------------------connect labels--------------------------
    hostlabel = Label(dbroot,text='Enter Host: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)
    
    userlabel = Label(dbroot,text='Enter User: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text='Enter Password: ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)


####################### Connectdb entry ################################
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()


    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #-----------connect button ----------------------
    submit_button = Button(dbroot,text = 'Submit',font=('times',15,'bold'),bd=5,width=20,bg='gold',
                           activebackground='brown',activeforeground='white',command=submitdb)
    submit_button.place(x=150,y=190)


    dbroot.mainloop()





########################### configuring time & date ######################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date: '+date_string+"\nTime: "+time_string)
    clock.after(200,tick)
                
 ################## CONFIGURING INTRO SLIDER COLOR CHANGE ##############
import random
colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)



###################### CONFIGURING OF APPEARING TEXT IN INTRO SLIDE LABEL ############################                    

def IntroLabelTick():
    global count,text
    if (count >= len(ss)):
       count = 0
       text = ''
       SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    
    SliderLabel.after(200,IntroLabelTick)


#############################################################################################################3

root = Tk()
root.title('Student Management System')
root.config(bg='gold')
root.geometry('1174x700+50+50')
root.resizable(False,False)
##################################################### Frames #################################################

DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=500)

######################### DATA ENTRY FRAME #################
frontlabel = Label(DataEntryFrame,text='------------Welcome-----------',width=30,font=('arial',20,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add student',width=22,font=('chiller',15,'bold'),bd=5,bg='sky blue',activebackground='blue',relief=RIDGE,activeforeground='white',command=add_student)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search student',width=22,font=('chiller',15,'bold'),bd=5,bg='sky blue',activebackground='blue',relief=RIDGE,activeforeground='white',command=search_student)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete student',width=22,font=('chiller',15,'bold'),bd=5,bg='sky blue',activebackground='blue',relief=RIDGE,activeforeground='white',command=delete_student)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update student',width=22,font=('chiller',15,'bold'),bd=5,bg='sky blue',activebackground='blue',relief=RIDGE,activeforeground='white',command=update_student)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=22,font=('chiller',15,'bold'),bd=5,bg='sky blue',activebackground='blue',relief=RIDGE,activeforeground='white',command=show_student)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',width=22,font=('chiller',15,'bold'),bd=5,bg='sky blue',activebackground='blue',relief=RIDGE,activeforeground='white',command=export_student)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=22,font=('chiller',15,'bold'),bd=5,bg='sky blue',activebackground='blue',relief=RIDGE,activeforeground='white',command=exit_student)
exitbtn.pack(side=TOP,expand=True)









###################### SHOW DATA FRAME ########################
ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=500)

style=ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)

studenttable = Treeview(
    ShowDataFrame,
    column=('Id', 'Name', 'Mobile no', 'Email', 'Address', 'Gender', 'DOB', 'Added Date', 'Added Time'),
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)

# Pack the widgets
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
studenttable.pack(fill=BOTH, expand=True)

# Set the scrollbar commands
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)


studenttable.heading('Id',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile no',text='Mobile no')
studenttable.heading('Email',text='Email ID')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('DOB',text='DOB')
studenttable.heading('Added Date',text='Date')
studenttable.heading('Added Time',text='Time')
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile no',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=300)
studenttable.column('Gender',width=100)
studenttable.column('DOB',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)







###############################    VARIABLES    ##################################################
ss = 'Welcome to Student Management System'
count = 0
text = ''
############################ slider #############################################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()

#################################  clock   ################3

clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()

################################## CONNECT TO DATABASE BUTTON  ###############
connect_button = Button(root,text='Connect to Database',font=('chiller',18,'italic bold'),relief=RIDGE,borderwidth=4,width=23,bg='green2',activebackground='blue',activeforeground='white',command=Connectdb)
connect_button.place(x=930,y=0)



root.mainloop()








    