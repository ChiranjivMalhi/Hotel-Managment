# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:49:43 2020

@author: Chiranjiv
"""
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt


def assign(n,c,x,df,d,s):
    for j in df.index:
        if df["Avail"].loc[j]==" Available" and df["type"].loc[j]==x :
            print("Your room number is ",j)
            df["Avail"].loc[j]="Unavailable"
            df["Name"].loc[j]=n
            df["Contact Number"].loc[j]=c
            df["CheckinDate"].loc[j]=d
            df["Days"].loc[j]=s
            df.to_csv("D:\ip\hotel.csv",header=False)
            break
    else:
        print("Unavailable")

def act(a,p,rn,df):
    df[a].loc[rn]+=p
    df.to_csv("D:\ip\ctivities.csv",header=False)

def bill(rn,df2,df1):
    a=df2[["Spa","Swimming","Cycling","Gym","TS"]].loc[rn].sum()
    b=(df2["Base Fare"].loc[rn]+df2["Tax"].loc[rn])*df1["Days"].loc[rn]
    print("Activites bill ", df2[["Spa","Swimming","Cycling","Gym","TS"]].loc[rn])
    print("Total for Activites is ",a)
    print("Base Fare with 18%GST for " ,df1["Days"].loc[rn] , "days is" ,"(", df2["Base Fare"].loc[rn],"+",df2["Tax"].loc[rn],")  * ",df1["Days"].loc[rn],"=",b )
    print("Payable Amount is ",a+b)
    print("Thank you for choosing us")
    
    df1["Avail"].loc[rn]=" Available"
    df1["Name"].loc[rn]=" "
    df1["Contact Number"].loc[rn]=" "
    df1["CheckinDate"].loc[rn]=" "
    df1["CheckoutDate"].loc[rn]=" "
    df1["Days"].loc[rn]=''
    df2[["Spa","Swimming","Cycling","Gym","TS"]]=0,0,0,0,0
    df1.to_csv("D:\ip\hotel.csv",header=False)
    df2.to_csv("D:\ip\ctivities.csv",header=False)
 
def pie(s,l):
    fig1, ax1 = plt.subplots()
    ax1.pie(s, labels=l, startangle=90,autopct='%1.1f%%')
    ax1.axis('equal')
    plt.show()

def bar(s,l,a,b,c):
    plt.bar(s,l,lw=2)
    plt.title(a)
    plt.xlabel(b)
    plt.ylabel(c)
    plt.show()

def line(s,l,a,b,c):
    plt.plot(s,l)
    plt.title(a)
    plt.xlabel(b)
    plt.ylabel(c)
    plt.show()
    
def rec(df1,df2,rn,r):
    l1=df1[["Name","Contact Number","CheckinDate","CheckoutDate","Days","type"]].loc[rn]
    l2=df2[["Spa","Swimming","Cycling","Gym","TS"]].loc[rn]
    df3=pd.DataFrame({"Name":[l1[0]],"Contact Number":[l1[1]],"CheckinDate":[l1[2]],"CheckoutDate":[l1[3]],"Days":[l1[4]],"type":[l1[5]],"Spa":[l2[0]],"Swimming":[l2[1]],"Cycling":[l2[2]],"Gym":[l2[3]],"TS":[l2[4]]})
    r=r.append(df3,ignore_index=True)
    r.to_csv("D:/ip/record.csv",header=False,index=False)
    
def mon(a):
    l = [int(x) for x in a.split("-")]
    date1 = datetime.date(l[0], l[1], l[2])
    m=date1.month
    return m
    
def num(df,a,p):
    s=df[a].sum(axis=0)/p
    return s


h=pd.read_csv("D:\ip\hotel.csv",names=["Name","Contact Number","CheckinDate","CheckoutDate","Days","type","Avail"])
ac=pd.read_csv("D:\ip\ctivities.csv",names=["Spa","Swimming","Cycling","Gym","TS","Base Fare","Tax"])
record=pd.read_csv("D:/ip/record.csv",names=["Name","Contact Number","CheckinDate","CheckoutDate","Days","type","Spa","Swimming","Cycling","Gym","TS"])
h.index=np.arange(1,101)
ac.index=np.arange(1,101)


print("Welcome to the hotel")
a=int(input("""Are you  
            1) Administrator
            2) Guest
            Enter your Choice"""))
if a==2:
    b=int(input("""How can i help
                1) Check-in
                2) Activities
                3) Check-out
                Enter your choice"""))
    if b==1:
        n=int(input("Enter no of rooms"))
        for i in range(n):
            name=input("Enter name")
            c=int(input("Enter contact number"))
            t=int(input("""Enter Room type
                        1) Deluxe -Rs.5000/night
                        2) Suite -Rs.7000/night
                        3) Super Deluxe -Rs.9000/night"""))
            date = input('Enter a date in YYYY-MM-DD format')
            st=int(input("Enter number of nights staying"))
            if t==1:
                assign(name,c,"Deluxe",h,date,st)
            if t==2:
                assign(name,c," Suite",h,date,st)
            if t==3:
                assign(name,c," Super Deluxe",h,date,st)
    elif b==2:
        rn=int(input("Enter Room Number"))
        k=input("""What would you like to do
              1) Spa - 1000
              2) Swimming - 500
              3) Cycling - 200
              4) Gym - 300
              5) Visit Tourist Spots - 150
                 Enter Choice or multiple choices with a space""")
        l=[int(x) for x in k.split(" ")]
        for j in l:
            if j==1:
                act("Spa",1000,rn,ac)
            elif j==2:
                act("Swimming",500,rn,ac)
            elif j==3:
                act("Cycling",200,rn,ac)
            elif j==4:
                act("Gym",300,rn,ac)
            elif j==5:
                act("TS",150,rn,ac)
        print("Enjoy you Activities")
    elif b==3: 
        rn=int(input("Enter your Room Number"))
        date = input('Enter a date in YYYY-MM-DD format')
        h["CheckoutDate"].loc[rn]=date
        rec(h,ac,rn,record)
        bill(rn,ac,h)
elif a==1:
    pa=input("Enter Password")
    w=True
    if pa=="hello":
        while w:
            z=int(input("""Enter Your Choice
                            1) Current Availability of Rooms
                            2) Analysis of Room type preferences
                            3) Analysis of Activity preferences
                            4) Analysis of length of stay
                            5) Customer Frequency
                            6) Exit"""))        
            if z==1:
                count=0
                for j in h.index:
                    if h["Avail"].loc[j]==" Available":
                        count+=1
                av,unav=count,100-count
                li=[av,unav]
                lis=["Available","Unavailable"]
                pie(li,lis)
            elif z==2:
                d={"Deluxe":0," Suite":0," Super Deluxe":0}
                for j in record["type"]:
                    d[j]+=1
                bar(d.keys(),d.values(),"Rooms","Types","No of Rooms")
            elif z==3:
                d={"Spa":num(record,"Spa",1000),"Swimming":num(record,"Swimming",500),"Cycling":num(record,"Cycling",200),"Gym":num(record,"Gym",300),"TS":num(record,"TS",150)}
                bar(d.keys(),d.values(),"Activities","Types","No of times used")
            elif z==4:
                d={}
                l=[]
                for i in record["Days"]:
                    if i not in l:
                        d[i]=1
                        l.append(i)
                    else:
                        d[i]+=1
                bar(d.keys(),d.values(),"Length of stay","No of Days","Frequency")
            elif z==5:
                d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
                l=["Jan","Feb","Mar","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
                for i in record["CheckinDate"]:
                    d[mon(i)]+=1
                t=int(input("""Enter your choice
                            1) Bar Graph
                            2) Line Graph"""))
                if t==1:
                    bar(l,d.values(),"Customers","Months","Frequency")
                else:
                    line(l,d.values(),"Customers","Months","Frequency")
            elif z==6:
                w=False
    else:
        print("Wrong Password")


                    
        
        
        

                        
        
        
        
        
        
        
        
        
        