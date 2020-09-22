import socket
import pickle
from tkinter import *
from _thread import *
import threading
import time


msg1 = "User Successfully added to database"
msg2 = "Logged in Successfully"

# printing seating pattern

def appointment_status(k):
    count = 0
    for i in k:
        if count == 2:
            count = count + 1
            if i == "B" or i < 10:
                print(str(i) + " ", end="    ")
            else:
                print(str(i), end="    ")
        elif count == 5:
            count = 1
            if i == "B" or i < 10:
                print("\n" + str(i) + " ", end=" ")
            else:
                print("\n" + str(i), end=" ")
        else:
            count = count + 1
            if i == "B" or i < 10:
                print(str(i) + " ", end=" ")
            else:
                print(str(i), end=" ")
    print()


    

#creating and connecting socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1026))
info = ''
root = Tk() 
root.minsize(640,480)
root.configure(background='black')
def display(event):
    #while True:
    id_val = []
    usrname =e1.get()
    if(usrname == "q"):
        #break
        return
    usrname = usrname.encode()
    id_val.append(usrname)
    #print("Enter Password:", end = " ")
    password = e2.get()
    
    if(password == "q"):  #to quit
        return
    password = password.encode()
    id_val.append(password)
    id_send = pickle.dumps(id_val)
    s.send(id_send)
    msg_recv = s.recv(100)
    msg_recv = msg_recv.decode()
    print(msg_recv)
    if(msg_recv == msg1 or msg_recv == msg2):    #checking if user entered correct password
        #loop_val = 1
        Mainbooking=Toplevel()
        def book_appointment(self):
            a='1'
            s.send(a.encode())
            q1 = s.recv(100)
            q = q1.decode()
            def book(self):
             disease = []
             disease1 = board.get()
             disease1 = disease1.encode()
             disease.append(disease1)
             disease2 = drop.get()
             disease2 = disease2.encode()
             disease.append(disease2)
             data1 = pickle.dumps(disease)
             s.send(data1)
             p = s.recv(100)
             k = pickle.loads(p)
             def check(self):
              var=StringVar()
              var.set(k[1])
              best_doctor=Label(Mainbooking,text='\nBest doctor for given disease:',font=('Courier',14))
              best_doctor.grid(row=8,column=1)
              train=Label(Mainbooking, textvariable=var,font=('Courier',14))
              train.grid(row=8,column=2)
              layout1=Label(Mainbooking,text='\nAppointment slots on terminal',font=('Courier',14))
              layout1.grid(row=9,column=0)
              appointment_status(k[0])
              def appointment_select(self):
               b = Seat.get()    
               b = b.split(" ")
               b1 = pickle.dumps(b)
               s.send(b1)
               for i in b:
                p2 = s.recv(100) #recieve msg for every seat trying to be booked. Wether booking was successful or failed
                s.send(str(i).encode())
                msg = p2.decode("utf-8")
                if msg[0] == "F":
                    Status=Label(Mainbooking,text='\nWrong Selection/Already Selected Appointment no:',font=('Courier',14))
                    Status.grid(row=11,column=0)
                    val2=StringVar()
                    val2.set(msg[1])
                    Status2=Label(Mainbooking, textvariable=val2,font=('Courier',14))
                    Status2.grid(row=11,column=1)
                elif msg[0] == "S":
                    Status=Label(Mainbooking,text='\nBooking Successful/Appointment Booked:',font=('Courier',14))
                    Status.grid(row=11,column=0)
                    val2=StringVar()
                    val2.set(msg[1])
                    Status2=Label(Mainbooking, textvariable=val2,font=('Courier',14))
                    Status2.grid(row=11,column=1)
                def destroy1(self):
                    best_doctor.destroy()
                    train.destroy()
                    layout1.destroy()
                    Status.destroy()
                    Status2.destroy()
                    bpoint.destroy()
                    apoint.destroy()
                    board.destroy()
                    drop.destroy()
                    Submit.destroy()
                    best_doctor.destroy()
                    Seatlbl.destroy()
                    Seat.destroy()
                    Check1.destroy()
                    remove_appointment.destroy()
                remove_appointment=Button(Mainbooking,text='\nDone', width=15,font=('Courier',14))
                remove_appointment.grid(row=12,column=0)
                remove_appointment.bind("<Button-1>",destroy1)


                   
               throw =  s.recv(100)   
              Seatlbl=Label(Mainbooking, text='\nEnter your Seat(s):',font=('Courier',14))
              Seatlbl.grid(row=10,column=0)
              Seat=Entry(Mainbooking,width=15,font=('Courier',14))
              Seat.grid(row=10,column=1)
              Seat.bind("<Return>",appointment_select)
             Check1=Button(Mainbooking,text='\nCheck', width=15,font=('Courier',14))
             Check1.grid(row=8,column=0)
             Check1.bind("<Button-1>",check)

              
              
             
            bpoint=Label(Mainbooking,text='\nEnter Disease 1 (Fever, Cold, Fractures, Heart Problems, Neurology)',font=('Courier',14))
            bpoint.grid(row=5,column=0)
            board=Entry(Mainbooking,width=15,font=('Courier',14))
            board.grid(row=5,column=1)
            apoint=Label(Mainbooking,text='\nEnter Disease 2 (Fever, Cold, Fractures, Heart Problems, Neurology)',font=('Courier',14))
            apoint.grid(row=6,column=0)
            drop=Entry(Mainbooking,width=15,font=('Courier',14))
            drop.grid(row=6,column=1)
            Submit=Button(Mainbooking, text='\nSubmit', width=15,font=('Courier',14))
            Submit.grid(row=7,column=0)
            Submit.bind("<Button-1>",book)
            
        
        def cancel_appointment(self):
            a='2'
            s.send(a.encode())
            q1 = s.recv(200)
            q = pickle.loads(q1)   
            pres = 0                    
            train_track = []
            x=' '
            for i in q:
                if(len(q[i]) > 0):
                    pres = 1                    #variable stores 1 if user has atleast one seat booked
                    train_track.append(i)
                    x=x+i
                    x=x+str(q[i])
                    x=x+' '
            if(x!=' '):
             val3=StringVar()
             val3.set(x)             
             no=Label(Mainbooking,text='\nDoctor appointment allotment:',font=('Courier',11))
             no.grid(row=5,column=0)
             x1=Label(Mainbooking,textvariable=val3,font=('Courier',11))
             x1.grid(row=5,column=1)

                    
            if(pres != 1):
                Empty=Label(Mainbooking,text='\nNo appointments to cancel',font=('Courier',14))
                Empty.grid(row=5,column=0)
                def done_destroy2(self):
                 Empty.destroy()
                 Done2.destroy()
                Done2=Button(Mainbooking, text='\nDone', width=15,font=('Courier',14))
                Done2.grid(row=6,column=0)
                Done2.bind("<Button-1>",done_destroy2)                
                a = "F"
                a = a.encode()
                s.send(a)
                s.recv(10)
            else:
                a = "P"
                a = a.encode()
                s.send(a)
                s.recv(10)
                def cancel_appointment1(self):
                 #print("Enter 0. to cancel all tickets at once. 1 to cancel one train seat(s) at a time") #0 cancels all train tickets at once
                 cancel_ticket = number.get()
                 y=' ' # 1 cancels based on input provided from the user
                 if(cancel_ticket == '1'):
                  for i in train_track:
                   print(train_track.index(i)+1, i, sep = ": ", end = "  ")              
                   y=str(train_track.index(i)+1)
                   y=y+': '
                   y=y+i
                  var1=StringVar()
                  var1.set(y)
                  id0=Label(Mainbooking,text="\nDoctor ID with Name",font=('Courier',11))
                  id0.grid(row=9,column=0)
                  id1=Label(Mainbooking,textvariable=var1,font=('Courier',11))
                  id1.grid(row=9,column=1)
                  ss=Label(Mainbooking,text="\nSelect ID",font=('Courier',11))
                  ss.grid(row=10,column=0)
                  sse=Entry(Mainbooking,width=15,font=('Courier',11))
                  sse.grid(row=10,column=1)
                  
                  def removes(self):
                   cancel1 = sse.get()
                   print()
                   cancel1 = cancel1.split(' ')
                   cancel1[0] = train_track[int(cancel1[0]) -1]
                   cancel2 = []
                   cancel2.append(cancel_ticket)
                   cancel1 = cancel2 + cancel1
                   ct=Label(Mainbooking,text="\nCancelled Appointments:",font=('Courier',11))
                   ct.grid(row=12,column=0)
                   z=StringVar()
                   z.set(cancel1)
                   ctc=Label(Mainbooking,textvariable=z,font=('Courier',11))
                   ctc.grid(row=12,column=1)
                   def rDestroyf(self):
                    ticket.destroy()
                    number.destroy()
                    Submit1.destroy()
                    remove.destroy()
                    no.destroy()
                    x1.destroy()
                    id0.destroy()
                    id1.destroy()
                    ss.destroy()
                    sse.destroy()
                    ct.destroy()
                    ctc.destroy()
                    rDestroy.destroy()
                   rDestroy=Button(Mainbooking, text='\nDone', width=15,font=('Courier',11))
                   rDestroy.grid(row=13,column=0)
                   rDestroy.bind("<Button-1>",rDestroyf)
                   #print(cancel1)
                   cancel1 = pickle.dumps(cancel1)
                   s.send(cancel1)
                   cancel_status = s.recv(100)
                  remove=Button(Mainbooking, text='\nCancel Appointments(s)', width=15,font=('Courier',11))
                  remove.grid(row=11,column=0)
                  remove.bind("<Button-1>",removes)
                 else:
                  ct=Label(Mainbooking,text="\nAll Appointments Cancelled Successfully:",font=('Courier',11))
                  ct.grid(row=9,column=0)
                  def rDestroyf(self):
                     ct.destroy()
                     no.destroy()
                     x1.destroy()
                     ticket.destroy()
                     number.destroy()
                     Submit1.destroy()
                     rDestroy.destroy()

                  rDestroy=Button(Mainbooking, text='\nDone', width=15,font=('Courier',11))
                  rDestroy.grid(row=10,column=0)
                  rDestroy.bind("<Button-1>",rDestroyf)
                  cancel1 = []
                  cancel1.append(cancel_ticket)
                  cancel1 = pickle.dumps(cancel1)
                  s.send(cancel1)
                  cancel_status = s.recv(100)    
                #print("Enter 0. to cancel all appointments at once. 1 to cancel one appointment at a time") #0 cancels all train tickets at once
                ticket=Label(Mainbooking,text='\nEnter 0 to cancel all appointments at once / 1 to cancel one appointment at a time\n',font=('Courier',11))
                ticket.grid(row=6,column=0)
                number=Entry(Mainbooking,width=15,font=('Courier',11))
                number.grid(row=6,column=1)
                Submit1=Button(Mainbooking, text='Submit', width=15,font=('Courier',11))
                Submit1.grid(row=7,column=0)
                Submit1.bind("<Button-1>",cancel_appointment1)
                    
       

        def exit_status(self):
            a='3'
            s.send(a.encode())
            q1 = s.recv(200)
            q = q1.decode()
            Mainbooking.destroy()
            Mainbooking.update()
        
        title1= Label(Mainbooking, text='Appointment Booking', width=20,height=2,font=('Courier',20,'bold underline'))
        title1.grid(row=0,column=0)
        Mainbooking.minsize(640,480)
        Options=Label(text='Enter Your Choice:',font=('Courier',14))
        Options.grid(row=2)
        Book=Button(Mainbooking, text='1.Book ', width=15,font=('Courier',14))
        Book.grid(row=4,column=0)
        Book.bind("<Button-1>",book_appointment)
        Cancel=Button(Mainbooking, text='2.Cancel', width=15,font=('Courier',14))
        Cancel.grid(row=4,column=1)
        Cancel.bind("<Button-1>",cancel_appointment)
        Exit=Button(Mainbooking, text='3.exit', width=15,font=('Courier',14))
        Exit.grid(row=4,column=3)
        Exit.bind("<Button-1>",exit_status)
           
        Mainbooking.mainloop()
        
    else:
        print("Retry")        

title = Label(root, text='Doctor Appointment', width=20,height=2,font=('Courier',20,'bold underline')) 
title.grid(row=0,column=0)
l1=Label(text='Enter Username:',font=('Courier',14)).grid(row=10)
l2=Label(text="Enter Password:",font=('Courier',14)).grid(row=12)
e1=Entry(root,width=15,font=('Courier',14))
e1.grid(row=10,column=2)
e2=Entry(root,width=15,font=('Courier',14),show='*')
e2.grid(row=12,column=2)
e2.bind("<Return>",display)
root.configure(background='white')
root.mainloop()
