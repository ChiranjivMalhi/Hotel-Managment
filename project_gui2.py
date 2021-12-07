
from tkinter import *
import tkinter as tk
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox


def assign(n,c,x,df,d,s):
    for j in df.index:
        if df["Avail"].loc[j]==" Available" and df["type"].loc[j]==x :
            df["Avail"].loc[j]="Unavailable"
            df["Name"].loc[j]=n
            df["Contact Number"].loc[j]=c
            df["CheckinDate"].loc[j]=d
            df["Days"].loc[j]=s
            df.to_csv("hotel.csv",header=False)
            return j
            break

    
def rec(df1,df2,rn,r):
    l1=df1[["Name","Contact Number","CheckinDate","CheckoutDate","Days","type"]].loc[rn]
    l2=df2[["Spa","Swimming","Cycling","Gym","TS"]].loc[rn]
    df3=pd.DataFrame({"Name":[l1[0]],"Contact Number":[l1[1]],"CheckinDate":[l1[2]],"CheckoutDate":[l1[3]],"Days":[l1[4]],"type":[l1[5]],"Spa":[l2[0]],"Swimming":[l2[1]],"Cycling":[l2[2]],"Gym":[l2[3]],"TS":[l2[4]]})
    r=r.append(df3,ignore_index=True)
    r.to_csv("record.csv",header=False,index=False)


def bar(s,l,a,b,c):
    
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).bar(s,l)
    
    plt.title(a)
    plt.xlabel(b)
    plt.ylabel(c)
    
def num(df,a,p):
    s=df[a].sum(axis=0)/p
    return s    

def mon(a):
    l = [int(x) for x in a.split("-")]
    date1 = datetime.date(l[0], l[1], l[2])
    m=date1.month
    return m

def act(a,p,rn,df):
    df[a].loc[rn]+=p
    df.to_csv("ctivities.csv",header=False)
    
def g():
    
    
    
    def types():
        
        def nex():
            Types.destroy()
            checkin()
            
        global h
        
        Types=Toplevel()
        can=Canvas(Types,height=500,width=700,bg="#ECE4B7")
        can.pack()
        
        d={"Deluxe":0,"Suite":0,"Super Deluxe":0}
        
        for i in h.index:
            if h["Avail"].loc[i]==" Available" and i<=50:
                d["Deluxe"]+=1
            elif h["Avail"].loc[i]==" Available" and i<=80:
                d["Suite"]+=1
            elif h["Avail"].loc[i]==" Available" and i>80:
                d["Super Deluxe"]+=1
        
        n=Label(can,text="Deluxe :",font=f1,bg="#ECE4B7",fg="#602f74")
        n1=Label(can,text="Suite :",font=f1,bg="#ECE4B7",fg="#602f74")
        n2=Label(can,text="Super Deluxe :",font=f1,bg="#ECE4B7",fg="#602f74")
        n3=Label(can,text=d["Deluxe"],font=f1,bg="#ECE4B7",fg="#602f74")
        n4=Label(can,text=d["Suite"],font=f1,bg="#ECE4B7",fg="#602f74")
        n5=Label(can,text=d["Super Deluxe"],font=f1,bg="#ECE4B7",fg="#602f74")
        head=Label(can,text="Availability of Rooms",font=f2,bg="#ECE4B7",fg="#602f74")      
              
        n.place(relx=0.1,rely=0.5)
        n1.place(relx=0.35,rely=0.5)
        n2.place(relx=0.6,rely=0.5) 
        n3.place(relx=0.25,rely=0.5) 
        n4.place(relx=0.5,rely=0.5) 
        n5.place(relx=0.8,rely=0.5) 
        head.place(relx=0.3,rely=0.2)

        submit=Button(can,text="Next",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=nex)
        submit.place(relx=0.35,rely=0.95,anchor="s")
        back=Button(can,text="Back",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=Types.destroy)
        back.place(relx=0.65,rely=0.95,anchor="s")
        
        
        Types.mainloop()
    
    
    def checkin():
        

        def values():
            global h
            name=na.get()
            c=co.get()
            date=da.get()
            st=s.get()
            t=var.get()
            for j in [name,c,date,st,t]:
                if j=="":
                    messagebox.showerror("Error","Please fill all the details")
                    break
            else:
                j=assign(name,c,t,h,date,int(st))
                rono=Label(c2,text="Your Room Number is "+ str(j),font=f1,bg="#ECE4B7",fg="#602f74")
                rono.place(relx=0.35,rely=0.05)
                submit['state']=tk.DISABLED
        
        
        chi=Toplevel()
    
        c2=Canvas(chi,height=500,width=700,bg="#ECE4B7")
        c2.pack()
        
        na=Entry(c2)
        co=Entry(c2)
        da=Entry(c2)
        s=Entry(c2)
        
        var = StringVar(chi)
        R1 = Radiobutton(c2, text="Deluxe", variable=var, value="Deluxe",font=f3,bg="#ECE4B7",fg="#602f74")
        R1.place(relx=0.5,rely=0.65)
        R2 = Radiobutton(c2, text="Suite", variable=var, value="Suite",font=f3,bg="#ECE4B7",fg="#602f74")
        R2.place(relx=0.64,rely=0.65)
        R3 = Radiobutton(c2, text="Super Deluxe", variable=var,value="Super Deluxe",font=f3,bg="#ECE4B7",fg="#602f74")
        R3.place(relx=0.8,rely=0.65)
        
        p1=Label(c2,text="Rs 5000 \n per night",font=f3,bg="#ECE4B7",fg="#602f74")
        p2=Label(c2,text="Rs 7000 \n per night",font=f3,bg="#ECE4B7",fg="#602f74")
        p3=Label(c2,text="Rs 9000 \n per night",font=f3,bg="#ECE4B7",fg="#602f74")
        
        p1.place(relx=0.5,rely=0.7)
        p2.place(relx=0.64,rely=0.7)
        p3.place(relx=0.8,rely=0.7)
        
        n=Label(c2,text="Check-In",font=f2,bg="#ECE4B7",fg="#602f74")
        n1=Label(c2,text="Name",font=f1,bg="#ECE4B7",fg="#602f74")
        n2=Label(c2,text="Contact Number",font=f1,bg="#ECE4B7",fg="#602f74")
        n3=Label(c2,text="Date (YYYY-MM-DD)",font=f1,bg="#ECE4B7",fg="#602f74")
        n4=Label(c2,text="Lenght of Stay",font=f1,bg="#ECE4B7",fg="#602f74")
        n5=Label(c2,text="Type of Room",font=f1,bg="#ECE4B7",fg="#602f74")
    
        submit=Button(c2,text="Submit",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=values)
        submit.place(relx=0.4,rely=0.95,anchor="s")
        back=Button(c2,text="Back",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=chi.destroy)
        back.place(relx=0.7,rely=0.95,anchor="s")
    
        n.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.1)
        n1.place(relx=0.1,rely=0.25,relwidth=0.35,relheight=0.05)
        n2.place(relx=0.1,rely=0.35,relwidth=0.35,relheight=0.05)
        n3.place(relx=0.1,rely=0.45,relwidth=0.35,relheight=0.05)
        n4.place(relx=0.1,rely=0.55,relwidth=0.35,relheight=0.05)
        n5.place(relx=0.1,rely=0.65,relwidth=0.35,relheight=0.05)
        
        na.place(relx=0.5,rely=0.25,relwidth=0.4,relheight=0.05)
        co.place(relx=0.5,rely=0.35,relwidth=0.4,relheight=0.05)
        da.place(relx=0.5,rely=0.45,relwidth=0.4,relheight=0.05)
        s.place(relx=0.5,rely=0.55,relwidth=0.4,relheight=0.05)
    
        chi.mainloop()
    
    def activites():
        
    
        def activates():
            if a1.get()==1:
                s.config(state=NORMAL)
            else:
                s.config(state=DISABLED)
        
        def activateg():
            if a2.get()==1:
                g.config(state=NORMAL)
            else:
                g.config(state=DISABLED)
    
        def activatec():
            if a3.get()==1:
                c.config(state=NORMAL)
            else:
                c.config(state=DISABLED)
    
        def activatesi():
            if a4.get()==1:
                si.config(state=NORMAL)
            else:
                si.config(state=DISABLED)
    
        def activatet():
            if a5.get()==1:
                t.config(state=NORMAL)
            else:
                t.config(state=DISABLED)
    
        def acti():
            global ac
            global act
            enjoy=Label(c3,text="Enjoy your Activites",font=f,bg="#ECE4B7",fg="#602f74")
            enjoy.place(relx=0.25,rely=0.1)
            submit.config(state=DISABLED)
            rn=rono.get()

            if rn=="":
                messagebox.showerror("Error","Please enter the Room Number")
            else:
                rn=int(rn)
                if a1.get()==1:
                    act("Spa",1000*int(s.get()),rn,ac)
                if a4.get()==1:
                    act("Swimming",500*int(si.get()),rn,ac)
                if a3.get()==1:
                    act("Cycling",200*int(c.get()),rn,ac)
                if a2.get()==1:
                    act("Gym",300*int(g.get()),rn,ac)
                if a5.get()==1:
                    act("TS",150*int(t.get()),rn,ac)
        
        
        ac=Toplevel()
        
        c3=Canvas(ac,height=500,width=700,bg="#ECE4B7")
        c3.pack()
    
        frame=Frame(ac,bd=5,bg="#ECE4B7")
        frame.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.5,anchor="center")
    
        a1=IntVar(ac)
        a2=IntVar(ac)
        a3=IntVar(ac)
        a4=IntVar(ac)
        a5=IntVar(ac)
    
        s=Entry(frame,state=DISABLED)
        g=Entry(frame,state=DISABLED)
        c=Entry(frame,state=DISABLED)
        si=Entry(frame,state=DISABLED)
        t=Entry(frame,state=DISABLED)
        
        rono=Entry(c3)
        rono.place(relx=0.5,rely=0.8)
        r=Label(c3,text="Room no",font=f1,bg="#ECE4B7",fg="#602f74")
        r.place(relx=0.2,rely=0.8)
    
        a=Label(frame,text="Activites",font=f2,bg="#ECE4B7",fg="#602f74")
        a.place(relx=0,rely=0)
        p=Label(frame,text="How many people",font=f1,bg="#ECE4B7",fg="#602f74")
        p.place(relx=0.45,rely=0)
        
        spa=Checkbutton(frame,text="Spa: Rs 1000 per person",bg="#ECE4B7",fg="#602f74",font=f3,variable=a1,command=activates)
        gym=Checkbutton(frame,text="Gym: Rs 300 per person",bg="#ECE4B7",fg="#602f74",font=f3,variable=a2,command=activateg)
        cyc=Checkbutton(frame,text="Cycling: Rs 200 per person",bg="#ECE4B7",fg="#602f74",font=f3,variable=a3,command=activatec)
        swim=Checkbutton(frame,text="Swimming: Rs 500 per person",bg="#ECE4B7",fg="#602f74",font=f3,variable=a4,command=activatesi)
        ts=Checkbutton(frame,text="Tourists Spots: Rs 150 per person",bg="#ECE4B7",fg="#602f74",font=f3,variable=a5,command=activatet)
    
    
        spa.place(relx=0,rely=0.15,relheight=0.2)
        gym.place(relx=0,rely=0.3,relheight=0.2)
        cyc.place(relx=0,rely=0.5,relheight=0.2)
        swim.place(relx=0,rely=0.7,relheight=0.2)
        ts.place(relx=0,rely=0.9,relheight=0.2)
    
        s.place(relx=0.5,rely=0.15)
        g.place(relx=0.5,rely=0.35)
        c.place(relx=0.5,rely=0.55)
        si.place(relx=0.5,rely=0.75)
        t.place(relx=0.5,rely=0.95)
    
        submit=Button(c3,text="Submit",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=acti)
        submit.place(relx=0.3,rely=0.95,anchor="s")
        back=Button(c3,text="Back",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=ac.destroy)
        back.place(relx=0.7,rely=0.95,anchor="s")
    
        ac.mainloop()
    
    
    def cho():
        
        global h
        global ac
        global record
        
        def chout():
            
            rn=rono.get()
            date2=date1.get()
            submit.config(state=DISABLED)
            for j in [rn,date2]:
                if j=="":
                    messagebox.showerror("Error","Please fill all the details")
                    break
            else:
                rn=int(rn)
                h["CheckoutDate"].loc[rn]=date2
                rec(h,ac,rn,record)
                bill(rn,ac,h)
        
        def bill(rn,df2,df1):
        
        
            a=df2[["Spa","Swimming","Cycling","Gym","TS"]].loc[rn].sum()
            b=int(df2["Base Fare"].loc[rn]+df2["Tax"].loc[rn])
            c=int(df1["Days"].loc[rn])
            d=b*c
            
            
            bi=Label(frame,text="Bill",font=f1,bg="#ECE4B7",fg="#602f74")
            spa=Label(frame,text="Spa:   "+str(df2["Spa"].loc[rn]),font=f1,bg="#ECE4B7",fg="#602f74")
            gym=Label(frame,text="Gym:   "+str(df2["Gym"].loc[rn]),font=f1,bg="#ECE4B7",fg="#602f74")
            swim=Label(frame,text="Swim:   "+str(df2["Swimming"].loc[rn]),font=f1,bg="#ECE4B7",fg="#602f74")           
            cyc=Label(frame,text="Cycling:   "+str(df2["Cycling"].loc[rn]),font=f1,bg="#ECE4B7",fg="#602f74")
            ts=Label(frame,text="Tourits Spots:   "+str(df2["TS"].loc[rn]),font=f1,bg="#ECE4B7",fg="#602f74")
            tot_act=Label(frame,text="Total for Activites is "+str(a),font=f1,bg="#ECE4B7",fg="#602f74")  
            tot=Label(c4,font=f1,bg="#ECE4B7",fg="#602f74",text="Base Fare with 18%GST for " + str(df1["Days"].loc[rn]) + " days is" + "("+str(df2["Base Fare"].loc[rn]) + " plus " + str(df2["Tax"].loc[rn]) + ")  x " + str(df1["Days"].loc[rn]) + " equals " + str(d))
            pay=Label(c4,text="Total Payable amount is "+str(d+a),font=f1,bg="#ECE4B7",fg="#602f74")        
                      
            bi.place(relx=0.35,rely=0.5)
            spa.place(relx=0.2,rely=0.6)
            gym.place(relx=0.2,rely=0.7)
            swim.place(relx=0.2,rely=0.8)
            cyc.place(relx=0.4,rely=0.6)
            ts.place(relx=0.4,rely=0.7)
            tot_act.place(relx=0.2,rely=0.9)
            tot.place(relx=0.05,rely=0.75)
            pay.place(relx=0.25,rely=0.8)
                      
            
            df1["Avail"].loc[rn]=" Available"
            df1["Name"].loc[rn]=" "
            df1["Contact Number"].loc[rn]=" "
            df1["CheckinDate"].loc[rn]=" "
            df1["CheckoutDate"].loc[rn]=" "
            df1["Days"].loc[rn]=''
            df2[["Spa","Swimming","Cycling","Gym","TS"]]=0,0,0,0,0
            df1.to_csv("hotel.csv",header=False)
            df2.to_csv("ctivities.csv",header=False)
        
        def dest():
            gu.destroy()
            chou.destroy()
        
        chou=Toplevel()
        c4=Canvas(chou,height=500,width=700,bg="#ECE4B7")
        c4.pack()
    
        frame=Frame(chou,bd=5,bg="#ECE4B7")
        frame.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.5,anchor="center")
    
        n=Label(c4,text="Check-Out",font=f2,bg="#ECE4B7",fg="#602f74")
        n.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.1)
    
        rono=Entry(frame)
        rono.place(relx=0.5,rely=0.1)
        r=Label(frame,text="Room no",font=f1,bg="#ECE4B7",fg="#602f74")
        r.place(relx=0.2,rely=0.1)
    
        date1=Entry(frame)
        date1.place(relx=0.5,rely=0.3)
        r1=Label(frame,text="Date (YYYY-MM-DD)",font=f1,bg="#ECE4B7",fg="#602f74")
        r1.place(relx=0.1,rely=0.3)
    
        submit=Button(c4,text="Submit",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=chout)
        submit.place(relx=0.3,rely=0.95,anchor="s")
        back=Button(c4,text="Exit",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=dest)
        back.place(relx=0.7,rely=0.95,anchor="s")
    
        chou.mainloop()
    
    gu=Toplevel()

    c1=Canvas(gu,height=500,width=700,bg="#ECE4B7")
    c1.pack()

    frame=Frame(gu,bd=5,bg="#ECE4B7")
    frame.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.5,anchor="center")

    h=Label(frame,text="How can I help you",font=f,bg="#ECE4B7",fg="#602f74")
    chin=Button(frame,text="Check-In",padx=5,pady=1,command=types,fg="#ECE4B7",bg="#602f74",font=f1)
    chout=Button(frame,text="Check-Out",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=cho)
    act=Button(frame,text="Activites",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=activites)

    h.place(relx=0.5, rely=0.1,anchor="n")
    chin.place(relx=0.35,rely=0.3,relwidth=0.3,relheight=0.2)
    act.place(relx=0.35,rely=0.5,relwidth=0.3,relheight=0.2)
    chout.place(relx=0.35,rely=0.7,relwidth=0.3,relheight=0.2)
    
    back=Button(c1,text="Back",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=gu.destroy)
    back.place(relx=0.5,rely=0.95,anchor="s")

    gu.mainloop()



def admin_r():
     
    global h
    
    def curr():
        
        graph=Toplevel()
        
        count=0
        for j in h.index:
            if h["Avail"].loc[j]==" Available":
                count+=1
        av,unav=count,100-count
        li=[av,unav]
        lis=["Available","Unavailable"]
        
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).pie(li, labels=lis, startangle=90,autopct='%1.1f%%')
        
        canvas = FigureCanvasTkAgg(fig, master=graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        graph.mainloop()
        
    
    def room():
        
        graph=Toplevel()
        
        d={"Deluxe":0,"Suite":0,"Super Deluxe":0}
        for j in record["type"]:
            d[j]+=1
        
        fig = Figure(figsize=(5, 5), dpi=100)
        a1=fig.add_subplot(111)
        a1.bar(d.keys(),d.values())
        a1.set_title("Rooms")
        a1.set_xlabel("Types")
        a1.set_ylabel("No of Rooms")
        
        
        canvas = FigureCanvasTkAgg(fig, master=graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        graph.mainloop()
                            
        
    def activity():
        
        global record
        
        graph=Toplevel()
        
        d={"Spa":num(record,"Spa",1000),"Swimming":num(record,"Swimming",500),"Cycling":num(record,"Cycling",200),"Gym":num(record,"Gym",300),"TS":num(record,"TS",150)}
        
        
        fig = Figure(figsize=(5, 5), dpi=100)
        a1=fig.add_subplot(111)
        a1.bar(d.keys(),d.values())
        a1.set_title("Activities")
        a1.set_xlabel("Types")
        a1.set_ylabel("No of times used")
        
        
        canvas = FigureCanvasTkAgg(fig, master=graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        graph.mainloop()
        
    def length():
        
        global record
        
        graph=Toplevel()
        
        d={}
        l=[]
        for i in record["Days"]:
            if i not in l:
                d[i]=1
                l.append(i)
            else:
                d[i]+=1
        
        fig = Figure(figsize=(5, 5), dpi=100)
        a1=fig.add_subplot(111)
        a1.bar(d.keys(),d.values())
        a1.set_title("Length of stay")
        a1.set_xlabel("No of Days")
        a1.set_ylabel("Frequency")
        
        
        canvas = FigureCanvasTkAgg(fig, master=graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        graph.mainloop()
        
    
    def cof():
        
        graph=Toplevel()
        
        
        d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        l=["Jan","Feb","Mar","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
        for i in record["CheckinDate"]:
            d[mon(i)]+=1
        
        fig = Figure(figsize=(5, 3), dpi=100)
        a1=fig.add_subplot(111)
        a1.bar(d.keys(),d.values())
        a1.set_title("Customers")
        a1.set_xlabel("Months")
        a1.set_ylabel("Frequency")
        
        
        canvas = FigureCanvasTkAgg(fig, master=graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        fig2 = Figure(figsize=(5, 3), dpi=100)
        a2=fig2.add_subplot(111)
        a2.plot(l,list(d.values()))
        a2.set_title("Customers")
        a2.set_xlabel("Months")
        a2.set_ylabel("Frequency")
        
        canvas = FigureCanvasTkAgg(fig2, master=graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        
        
        
        graph.mainloop()
    
    adi=Toplevel()
    
    c6=Canvas(adi,height=500,width=700,bg="#ECE4B7")
    c6.pack()

    frame=Frame(adi,bd=5,bg="#ECE4B7")
    frame.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.5,anchor="center")
    
    n=Label(c6,text="Menu",font=f2,bg="#ECE4B7",fg="#602f74")
    n.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.1)
    
    cr=Button(frame,text="Current Availablity of Rooms",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=curr)
    rt=Button(frame,text="Room Type Preferences",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=room)
    actp=Button(frame,text="Activites Prefernces",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=activity)
    lp=Button(frame,text="Length of stay preferences",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=length)
    cf=Button(frame,text="Customer Frequency",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=cof)
              
    cr.place(relx=0.0,rely=0.3,relwidth=0.5,relheight=0.2)
    rt.place(relx=0.0,rely=0.5,relwidth=0.5,relheight=0.2)
    actp.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.2)
    lp.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.2)
    cf.place(relx=0.25,rely=0.7,relwidth=0.5,relheight=0.2)
    
    back=Button(c6,text="Back",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=adi.destroy)
    back.place(relx=0.5,rely=0.95,anchor="s")
    
    adi.mainloop()
    

def admin():
    
    def password():
        if pas.get()=="hello":
            submit.after(1,ad.destroy)
            admin_r()
            
        else:
            wp=Label(frame,text="Wrong Password",font=f1,bg="#ECE4B7",fg="#602f74")
            wp.place(relx=0.3,rely=0.3)
    
    ad=Toplevel()
    
    c5=Canvas(ad,height=300,width=400,bg="#ECE4B7")
    c5.pack()

    frame=Frame(ad,bd=5,bg="#ECE4B7")
    frame.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.5,anchor="center")
    
    pas=Entry(frame,show="*")
    pas.place(relx=0.5,rely=0.1)
    r=Label(frame,text="Password",font=f1,bg="#ECE4B7",fg="#602f74")
    r.place(relx=0.2,rely=0.1)
    
    submit=Button(c5,text="Submit",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=password)
    submit.place(relx=0.3,rely=0.95,anchor="s")
    back=Button(c5,text="Back",padx=5,pady=1,fg="#ECE4B7",bg="#602f74",font=f1,command=ad.destroy)
    back.place(relx=0.7,rely=0.95,anchor="s")
    
    ad.mainloop()


    
h=pd.read_csv("hotel.csv",names=["Name","Contact Number","CheckinDate","CheckoutDate","Days","type","Avail"])
ac=pd.read_csv("ctivities.csv",names=["Spa","Swimming","Cycling","Gym","TS","Base Fare","Tax"])
record=pd.read_csv("record.csv",names=["Name","Contact Number","CheckinDate","CheckoutDate","Days","type","Spa","Swimming","Cycling","Gym","TS"])
h.index=np.arange(1,101)
ac.index=np.arange(1,101)

root=Tk()
canvas=Canvas(root,height=600,width=1000)
canvas.pack()


f=("Campton-Light",20)
f1=("Campton-Light",13)
f2=("Campton-Bold",20)
f3=("Campton-Light",10)


bg_image=PhotoImage(file="h1.png")
bglabel=Label(root,image=bg_image)
bglabel.place(relwidth=1,relheight=1)

frame=Frame(root,bd=5,bg="#602f74")
frame.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.5,anchor="center")

wel=Label(frame,text="""Welcome to The McAvoy \n """,font=f,fg="#ECE4B7",bg="#602f74")
admin=Button(frame,text="Administrator",padx=5,pady=1,font=f1,bg="#ECE4B7",fg="#602f74",command=admin)
guest=Button(frame,text="Guest",padx=5,pady=1,command=g,font=f1,bg="#ECE4B7",fg="#602f74")

wel.place(relx=0.5,rely=0,anchor="n")
admin.place(relx=0.35,rely=0.3,relwidth=0.3,relheight=0.2)
guest.place(relx=0.35,rely=0.5,relwidth=0.3,relheight=0.2)
root.mainloop()
