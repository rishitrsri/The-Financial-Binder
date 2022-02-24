#Modules Imported Start Below
import time

import mysql.connector as msc
dbs=msc.connect(host="localhost", user="root", password="1397", db="binderdb")
mycursor=dbs.cursor()

#Function Definitions Start Below

#for Home expenditures
def viewinfo():
    give="SELECT * FROM homeexp" 
    mycursor.execute(give,)
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

def addinfo():
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> ₹"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO homeexp VALUES(%s,%s)"
    mycursor.execute(give,(info,value))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo():
    pass

#for Investments
def viewinfo2():
    give="SELECT * FROM invest" 
    mycursor.execute(give,)
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

def addinfo2():
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> ₹"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO invest VALUES(%s,%s)"
    mycursor.execute(give,(info,value))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo2():
    pass

# for income info
def viewinfo3():
    give="SELECT * FROM income" 
    mycursor.execute(give,)
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

def addinfo3():
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> ₹"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO income VALUES(%s,%s)"
    mycursor.execute(give,(info,value,))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo3():
    pass

#for Profile
def viewinfo4():
    give="SELECT * FROM income" 
    mycursor.execute(give,)
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

def addinfo4():
    print("Please enter the amount you want to add to Home Expenditures")
    time.sleep(0.25)
    value=float(input("> ₹"))
    time.sleep(0.5)
    print("Please enter any information you would like to add for this transaction")
    print("LESS THAN 200 Characters")
    time.sleep(0.25)
    info=input("> ")
    give="INSERT INTO income VALUES(%s,%s)"
    mycursor.execute(give,(info,value,))
    dbs.commit()
    time.sleep(0.25)
    #print(mycursor.rowcount,"Records Inserted")

def editinfo4():
    pass

def mainopt1():
    #dbname='homeexp'
    while True:
        print('                    𝗛𝗼𝘂𝘀𝗲𝗵𝗼𝗹𝗱 𝗘𝘅𝗽𝗲𝗻𝗱𝗶𝘁𝘂𝗿𝗲𝘀                    ')
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
               viewinfo()
            elif mch==2:
                addinfo()
            elif mch==3:
                editinfo()
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
        print("          𝗜𝗻𝘃𝗲𝘀𝘁𝗺𝗲𝗻𝘁𝘀          ")
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
                viewinfo2()
            elif mch==2:
                addinfo2()
            elif mch==3:
                editinfo2()
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
        print("                𝗜𝗻𝗰𝗼𝗺𝗲 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻                ")
        print(""" 
              M E N U
        (1) View Current Income Information
        (2) Edit existing Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo3()
            elif mch==2:
                editinfo3()
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
        print("      𝗣𝗿𝗼𝗳𝗶𝗹𝗲      ")
        print(""" 
              M E N U
        (1) View Information related to current Profile.
        (2) Edit existing Profile Information
        (3) Exit to Main Menu
        """)
        try:
            mch=int(input("Please enter your choice: "))
            if mch==1:
                viewinfo4()
            elif mch==2:
                editinfo4()
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
        
        (1) Go to 𝗛𝗼𝘂𝘀𝗲𝗵𝗼𝗹𝗱 𝗘𝘅𝗽𝗲𝗻𝗱𝗶𝘁𝘂𝗿𝗲𝘀.
        
        (2) Go to 𝗜𝗻𝘃𝗲𝘀𝘁𝗺𝗲𝗻𝘁𝘀.
        
        (3) Go to 𝗜𝗻𝗰𝗼𝗺𝗲 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻.
        
        (4) Go to 𝗣𝗿𝗼𝗳𝗶𝗹𝗲.
        
        (5) 🆀🆄🅸🆃
       
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