#Modules Imported Start Below
import time

import mysql.connector as msc
dbs=msc.connect(host="localhost", user="root", password="1397", db="binderdb")
mycursor=dbs.cursor()

#Function Definitions Start Below

#for Home expenditures
def viewinfo(dbname):
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def addinfo(dbname):
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> βΉ"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO %s VALUES(info=%s,value=%s)"
    mycursor.execute(give,(dbname[1,len(dbname)-1],info,value,))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo():
    pass

#for Investments
def viewinfo2(dbname):
    #give="SELECT * FROM homeexp" 
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def mainopt1():
    #dbname='homeexp'
    while True:
        print('                    ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π                    ')
        print(""" 
              M E N U
        (1) View Current Expenditures
        (2) Add new Expenditure
        (3) Edit existing Expenditures
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
               viewinfo('homeexp')
            elif mch==2:
                addinfo('homeexp')
            elif mch==3:
                editinfo('homeexp')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            
            
def mainopt2():
    #dbname='invest'
    while True:    
        print("          ππ»ππ²πππΊπ²π»ππ          ")
        print(""" 
              M E N U
        (1) View Current Investments
        (2) Add definitions for new Investments
        (3) Edit existing Investments
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('invest')
            elif mch==2:
                addinfo('invest')
            elif mch==3:
                editinfo('invest')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
    
def mainopt3():
    #dbname='income'
    while True:    
        print("                ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ»                ")
        print(""" 
              M E N U
        (1) View Current Income Information
        (2) Edit existing Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('income')
            elif mch==2:
                editinfo('income')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)    
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            

def mainopt4():
    #dbname='userid'
    while True:
        print("      π£πΏπΌπ³πΆπΉπ²      ")
        print(""" 
              M E N U
        (1) View Information related to current Profile.
        (2) Edit existing Profile Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('userid')
            elif mch==2:
                editinfo('userid')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
          

#Program Starts Below
while True:
    print("""
        WELCOME TO THE FINANCIAL BINDER
    How may we help you today?
        
        (1) Go to ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π.
        
        (2) Go to ππ»ππ²πππΊπ²π»ππ.
        
        (3) Go to ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ».
        
        (4) Go to π£πΏπΌπ³πΆπΉπ².
        
        (5) πππΈπ
       
    """)
    try:
        mmenuopt=int(input("> "))
        if mmenuopt==1:
            mainopt1() 
        elif mmenuopt==2:
            mainopt2()
        elif mmenuopt==3:            
            mainopt3()
        elif mmenuopt==4:
            mainopt4()
        elif mmenuopt==5:
            time.sleep(0.5)
            print(" ")
            print("Thank you for using The Financial Binder.")
            print(" ")
            time.sleep(1)
            break
        else:
            print(" ")
            print("Please input any of the displayed options")
            print(" ")
    except TypeError:
        print(" ")
        print("Please input any of the displayed options")
        print(" ")

#Modules Imported Start Below
import time

import mysql.connector as msc
dbs=msc.connect(host="localhost", user="root", password="1397", db="binderdb")
mycursor=dbs.cursor()

#Function Definitions Start Below

#for Home expenditures
def viewinfo(dbname):
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def addinfo(dbname):
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> βΉ"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO %s VALUES(info=%s,value=%s)"
    mycursor.execute(give,(dbname[1,len(dbname)-1],info,value,))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo():
    pass

#for Investments
def viewinfo2(dbname):
    #give="SELECT * FROM homeexp" 
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def mainopt1():
    #dbname='homeexp'
    while True:
        print('                    ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π                    ')
        print(""" 
              M E N U
        (1) View Current Expenditures
        (2) Add new Expenditure
        (3) Edit existing Expenditures
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
               viewinfo('homeexp')
            elif mch==2:
                addinfo('homeexp')
            elif mch==3:
                editinfo('homeexp')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            
            
def mainopt2():
    #dbname='invest'
    while True:    
        print("          ππ»ππ²πππΊπ²π»ππ          ")
        print(""" 
              M E N U
        (1) View Current Investments
        (2) Add definitions for new Investments
        (3) Edit existing Investments
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('invest')
            elif mch==2:
                addinfo('invest')
            elif mch==3:
                editinfo('invest')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
    
def mainopt3():
    #dbname='income'
    while True:    
        print("                ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ»                ")
        print(""" 
              M E N U
        (1) View Current Income Information
        (2) Edit existing Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('income')
            elif mch==2:
                editinfo('income')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)    
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            

def mainopt4():
    #dbname='userid'
    while True:
        print("      π£πΏπΌπ³πΆπΉπ²      ")
        print(""" 
              M E N U
        (1) View Information related to current Profile.
        (2) Edit existing Profile Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('userid')
            elif mch==2:
                editinfo('userid')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
          

#Program Starts Below
while True:
    print("""
        WELCOME TO THE FINANCIAL BINDER
    How may we help you today?
        
        (1) Go to ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π.
        
        (2) Go to ππ»ππ²πππΊπ²π»ππ.
        
        (3) Go to ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ».
        
        (4) Go to π£πΏπΌπ³πΆπΉπ².
        
        (5) πππΈπ
       
    """)
    try:
        mmenuopt=int(input("> "))
        if mmenuopt==1:
            mainopt1() 
        elif mmenuopt==2:
            mainopt2()
        elif mmenuopt==3:            
            mainopt3()
        elif mmenuopt==4:
            mainopt4()
        elif mmenuopt==5:
            time.sleep(0.5)
            print(" ")
            print("Thank you for using The Financial Binder.")
            print(" ")
            time.sleep(1)
            break
        else:
            print(" ")
            print("Please input any of the displayed options")
            print(" ")
    except TypeError:
        print(" ")
        print("Please input any of the displayed options")
        print(" ")

#Modules Imported Start Below
import time

import mysql.connector as msc
dbs=msc.connect(host="localhost", user="root", password="1397", db="binderdb")
mycursor=dbs.cursor()

#Function Definitions Start Below

#for Home expenditures
def viewinfo(dbname):
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def addinfo(dbname):
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> βΉ"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO %s VALUES(info=%s,value=%s)"
    mycursor.execute(give,(dbname[1,len(dbname)-1],info,value,))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo():
    pass

#for Investments
def viewinfo2(dbname):
    #give="SELECT * FROM homeexp" 
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def mainopt1():
    #dbname='homeexp'
    while True:
        print('                    ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π                    ')
        print(""" 
              M E N U
        (1) View Current Expenditures
        (2) Add new Expenditure
        (3) Edit existing Expenditures
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
               viewinfo('homeexp')
            elif mch==2:
                addinfo('homeexp')
            elif mch==3:
                editinfo('homeexp')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            
            
def mainopt2():
    #dbname='invest'
    while True:    
        print("          ππ»ππ²πππΊπ²π»ππ          ")
        print(""" 
              M E N U
        (1) View Current Investments
        (2) Add definitions for new Investments
        (3) Edit existing Investments
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('invest')
            elif mch==2:
                addinfo('invest')
            elif mch==3:
                editinfo('invest')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
    
def mainopt3():
    #dbname='income'
    while True:    
        print("                ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ»                ")
        print(""" 
              M E N U
        (1) View Current Income Information
        (2) Edit existing Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('income')
            elif mch==2:
                editinfo('income')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)    
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            

def mainopt4():
    #dbname='userid'
    while True:
        print("      π£πΏπΌπ³πΆπΉπ²      ")
        print(""" 
              M E N U
        (1) View Information related to current Profile.
        (2) Edit existing Profile Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('userid')
            elif mch==2:
                editinfo('userid')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
          

#Program Starts Below
while True:
    print("""
        WELCOME TO THE FINANCIAL BINDER
    How may we help you today?
        
        (1) Go to ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π.
        
        (2) Go to ππ»ππ²πππΊπ²π»ππ.
        
        (3) Go to ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ».
        
        (4) Go to π£πΏπΌπ³πΆπΉπ².
        
        (5) πππΈπ
       
    """)
    try:
        mmenuopt=int(input("> "))
        if mmenuopt==1:
            mainopt1() 
        elif mmenuopt==2:
            mainopt2()
        elif mmenuopt==3:            
            mainopt3()
        elif mmenuopt==4:
            mainopt4()
        elif mmenuopt==5:
            time.sleep(0.5)
            print(" ")
            print("Thank you for using The Financial Binder.")
            print(" ")
            time.sleep(1)
            break
        else:
            print(" ")
            print("Please input any of the displayed options")
            print(" ")
    except TypeError:
        print(" ")
        print("Please input any of the displayed options")
        print(" ")

#Modules Imported Start Below
import time

import mysql.connector as msc
dbs=msc.connect(host="localhost", user="root", password="1397", db="binderdb")
mycursor=dbs.cursor()

#Function Definitions Start Below

#for Home expenditures
def viewinfo(dbname):
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def addinfo(dbname):
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> βΉ"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO %s VALUES(info=%s,value=%s)"
    mycursor.execute(give,(dbname[1,len(dbname)-1],info,value,))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo():
    pass

#for Investments
def viewinfo2(dbname):
    #give="SELECT * FROM homeexp" 
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def mainopt1():
    #dbname='homeexp'
    while True:
        print('                    ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π                    ')
        print(""" 
              M E N U
        (1) View Current Expenditures
        (2) Add new Expenditure
        (3) Edit existing Expenditures
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
               viewinfo('homeexp')
            elif mch==2:
                addinfo('homeexp')
            elif mch==3:
                editinfo('homeexp')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            
            
def mainopt2():
    #dbname='invest'
    while True:    
        print("          ππ»ππ²πππΊπ²π»ππ          ")
        print(""" 
              M E N U
        (1) View Current Investments
        (2) Add definitions for new Investments
        (3) Edit existing Investments
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('invest')
            elif mch==2:
                addinfo('invest')
            elif mch==3:
                editinfo('invest')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
    
def mainopt3():
    #dbname='income'
    while True:    
        print("                ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ»                ")
        print(""" 
              M E N U
        (1) View Current Income Information
        (2) Edit existing Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('income')
            elif mch==2:
                editinfo('income')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)    
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            

def mainopt4():
    #dbname='userid'
    while True:
        print("      π£πΏπΌπ³πΆπΉπ²      ")
        print(""" 
              M E N U
        (1) View Information related to current Profile.
        (2) Edit existing Profile Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('userid')
            elif mch==2:
                editinfo('userid')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
          

#Program Starts Below
while True:
    print("""
        WELCOME TO THE FINANCIAL BINDER
    How may we help you today?
        
        (1) Go to ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π.
        
        (2) Go to ππ»ππ²πππΊπ²π»ππ.
        
        (3) Go to ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ».
        
        (4) Go to π£πΏπΌπ³πΆπΉπ².
        
        (5) πππΈπ
       
    """)
    try:
        mmenuopt=int(input("> "))
        if mmenuopt==1:
            mainopt1() 
        elif mmenuopt==2:
            mainopt2()
        elif mmenuopt==3:            
            mainopt3()
        elif mmenuopt==4:
            mainopt4()
        elif mmenuopt==5:
            time.sleep(0.5)
            print(" ")
            print("Thank you for using The Financial Binder.")
            print(" ")
            time.sleep(1)
            break
        else:
            print(" ")
            print("Please input any of the displayed options")
            print(" ")
    except TypeError:
        print(" ")
        print("Please input any of the displayed options")
        print(" ")

#Modules Imported Start Below
import time

import mysql.connector as msc
dbs=msc.connect(host="localhost", user="root", password="1397", db="binderdb")
mycursor=dbs.cursor()

#Function Definitions Start Below

#for Home expenditures
def viewinfo(dbname):
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def addinfo(dbname):
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> βΉ"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO %s VALUES(info=%s,value=%s)"
    mycursor.execute(give,(dbname[1,len(dbname)-1],info,value,))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo():
    pass

#for Investments
def viewinfo2(dbname):
    #give="SELECT * FROM homeexp" 
    give="SELECT * FROM %s" 
    mycursor.execute(give,(dbname[1,len(dbname)-1],))
    data=mycursor.fetchall()
    if data==[]:
        print("No data present in Database!")
        time.sleep(0.25)
    else:
        #sno=data[0]
        info=data[0]
        value=data[1]
        #print("Serial Number:",sno)
        print("Information",info)
        print("Value:",value)

def mainopt1():
    #dbname='homeexp'
    while True:
        print('                    ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π                    ')
        print(""" 
              M E N U
        (1) View Current Expenditures
        (2) Add new Expenditure
        (3) Edit existing Expenditures
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
               viewinfo('homeexp')
            elif mch==2:
                addinfo('homeexp')
            elif mch==3:
                editinfo('homeexp')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            
            
def mainopt2():
    #dbname='invest'
    while True:    
        print("          ππ»ππ²πππΊπ²π»ππ          ")
        print(""" 
              M E N U
        (1) View Current Investments
        (2) Add definitions for new Investments
        (3) Edit existing Investments
        (4) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('invest')
            elif mch==2:
                addinfo('invest')
            elif mch==3:
                editinfo('invest')
            elif mch==4:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
    
def mainopt3():
    #dbname='income'
    while True:    
        print("                ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ»                ")
        print(""" 
              M E N U
        (1) View Current Income Information
        (2) Edit existing Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('income')
            elif mch==2:
                editinfo('income')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)    
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
            

def mainopt4():
    #dbname='userid'
    while True:
        print("      π£πΏπΌπ³πΆπΉπ²      ")
        print(""" 
              M E N U
        (1) View Information related to current Profile.
        (2) Edit existing Profile Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo('userid')
            elif mch==2:
                editinfo('userid')
            elif mch==3:
                print("")
                print("Returning to Main Menu")
                time.sleep(0.25)
                print("...")
                time.sleep(0.5)
                break
            else:
                print("Incorrect input! Please try again.")
        except TypeError:
            print("Incorrect input! Please try again.")
          

#Program Starts Below
while True:
    print("""
        WELCOME TO THE FINANCIAL BINDER
    How may we help you today?
        
        (1) Go to ππΌπππ²π΅πΌπΉπ± πππ½π²π»π±πΆπππΏπ²π.
        
        (2) Go to ππ»ππ²πππΊπ²π»ππ.
        
        (3) Go to ππ»π°πΌπΊπ² ππ»π³πΌπΏπΊπ?ππΆπΌπ».
        
        (4) Go to π£πΏπΌπ³πΆπΉπ².
        
        (5) πππΈπ
       
    """)
    try:
        mmenuopt=int(input("> "))
        if mmenuopt==1:
            mainopt1() 
        elif mmenuopt==2:
            mainopt2()
        elif mmenuopt==3:            
            mainopt3()
        elif mmenuopt==4:
            mainopt4()
        elif mmenuopt==5:
            time.sleep(0.5)
            print(" ")
            print("Thank you for using The Financial Binder.")
            print(" ")
            time.sleep(1)
            break
        else:
            print(" ")
            print("Please input any of the displayed options")
            print(" ")
    except TypeError:
        print(" ")
        print("Please input any of the displayed options")
        print(" ")

