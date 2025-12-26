import mysql.connector

db=mysql.connector.connect(user="root",
                           host="localhost",
                           passwd="1Iam@9it",
                           database="BANKDB")
mycursor=db.cursor(buffered=True)

def menu():
    print("-"*133)
    print("-: MAIN MENU :-\n".center(133))
    print("1. Insert Record(s) \n".center(133))
    print("2. Display Records".center(133))
    print("   a. Sorted as per Account Number".center(133))
    print("    b. Sorted as per Customer Name".center(133))
    print("      c. Sorted as per Customer Balance\n".center(133))
    print("3. Search Record Details as per Account Number\n".center(133))
    print("4. Update Record\n".center(133))
    print("5. Delete Record\n".center(133))
    print("6. Transactions".center(133))
    print("   a. Debit/Withdraw from the Account".center(133))
    print("     b. Credit into the Account\n".center(133))
    print("7. Exit".center(133))
    print("-"*133)

def menusort():
    print("a. Sorted as per Account Number".center(133))
    print("b. Sorted as per Customer Name".center(133))
    print("c. Sorted as per Customer Balance".center(133))
    print("d. Back".center(133))

def menutransaction():
    print("a. Debit/Withdraw from the Account".center(133))
    print("b. Credit into the Account".center(133))
    print("c. Back".center(133))

#inserting records
def insert():
    while True:
        acc=input("Enter Account Number: ")
        name=input("Enter Name: ")
        mob=input("Enter Mobile Number: ")
        email=input("Enter Email: ")
        add=input("Enter Address: ")
        city=input("Enter City: ")
        state=input("Enter State: ")
        bal=float(input("Enter Account Balance: "))
        rec=[acc,name.upper(),mob,email,add.upper(),city.upper(),state.upper(),bal]
        cmd="INSERT INTO BANK VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(cmd,rec)
        db.commit()
        ch=input("Do you want to enter more records[Y/N]: ")
        if ch=="N" or ch=="n":
            break

#displaying records asc. order of acc. no.
def dispsortacc():
    try:
        mycursor.execute("SELECT * FROM BANK ORDER BY AccNo")
        f="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(f % ("AccNo","Name","Mobile","Email","Complete Address","City","State","Balance"))
        print("-"*133)
        for i in mycursor:
            for j in i:
                print("%14s" % j,end=" ")
            print()
        print("_"*133)
    except:
        print("Table doesn't exist.")
            
#displaying records asc. order of customer name
def dispsortname():
    try:
        mycursor.execute("SELECT * FROM BANK ORDER BY Name")
        f="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(f % ("AccNo","Name","Mobile","Email","Complete Address","City","State","Balance"))
        print("-"*133)
        for i in mycursor:
            for j in i:
                print("%14s" % j,end=" ")
            print()
        print("_"*133)
    except:
        print("Table doesn't exist.")
        

#displaying records asc. order of customer balance
def dispsortbal():
    try:
        mycursor.execute("SELECT * FROM BANK ORDER BY Balance")
        f="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(f % ("AccNo","Name","Mobile","Email","Complete Address","City","State","Balance"))
        print("-"*133)
        for i in mycursor:
            for j in i:
                print("%14s" % j,end=" ")
            print()
        print("_"*133)
    except:
        print("Table doesn't exist.")
        
#searching record
def srch():
    try:
        mycursor.execute("SELECT * FROM BANK")
        ch=input("Enter Account number to be searched: ")
        for i in mycursor:
            if i[0]==ch:
                print("-"*133)
                f="%15s %15s %15s %15s %15s %15s %15s %15s"
                print(f % ("AccNo","Name","Mobile","Email","Complete Address","City","State","Balance"))
                print("-"*133)
                for j in i:
                    print("%14s" % j,end=" ")
                print()
                break
        else:
            print("Record Not Found.")
    except:
        print("Table doesn't exist.")

#updating record
def recupdate():
    try:
        mycursor.execute("SELECT * FROM BANK")
        a=input("Enter the Account Number: ")
        for i in mycursor:
            i=list(i)
            if i[0]==a:
                ch=input("Change Name[Y/N]: ")
                if ch=="y" or ch=="Y":
                    i[1]=input("Enter Name: ")
                    i[1]=i[1].upper()

                ch=input("Change Mobile[Y/N]: ")
                if ch=="y" or ch=="Y":
                    i[2]=input("Enter Mobile: ")

                ch=input("Change Email[Y/N]: ")
                if ch=="y" or ch=="Y":
                    i[3]=input("Enter Email: ")

                ch=input("Change Address[Y/N]: ")
                if ch=="y" or ch=="Y":
                    i[4]=input("Enter Address: ")
                    i[4]=i[4].upper()

                ch=input("Change City[Y/N]: ")
                if ch=="y" or ch=="Y":
                    i[5]=input("Enter City: ")
                    i[5]=i[5].upper()

                ch=input("Change State[Y/N]: ")
                if ch=="y" or ch=="Y":
                    i[6]=input("Enter State: ")
                    i[6]=i[6].upper()

                ch=input("Update Balance[Y/N]: ")
                if ch=="y" or ch=="Y":
                    i[7]=float(input("Enter Balance: "))
                cmd="UPDATE BANK SET NAME=%s,MOBILE=%s,EMAIL=%s,COMPLETE_ADDRESS=%s,CITY=%s,STATE=%s,BALANCE=%s WHERE ACCNO=%s"    
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                db.commit()
                print("Account Updated.")
                break
        else:
            print("Record not found.")
    except:
        print("No such table.")

#deleting record
def dlt():
    try:
        mycursor.execute("SELECT * FROM BANK")
        ac=input("Enter the Account number: ")
        for i in mycursor:
            i=list(i)
            if i[0]==ac:
                cmd="DELETE FROM BANK WHERE ACCNO=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                db.commit()
                print("Account Deleted.")
                break
        else:
             print("Record Not Found.")
    except:
        print("Table Doesn't Exist.")

#debit min bal. 2000
def debit():
    mycursor.execute("SELECT * FROM BANK")
    print("NOTE: Money can be debited upto a minimum balance of Rs.2000")
    acc=input("Enter the Account number: ")
    for i in mycursor:
        i=list(i)
        if i[0]==acc:
            amt=float(input("Enter the amount to be withdrawn: "))
            if i[7]-amt>=2000:
                i[7]-=amt
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                db.commit()
                print("Amount Debited Successfully.")
                break
            else:
                print("Requirements not met[min. bal Rs.2000]")
                break
    else:
        print("Record Not Found.")
               
            
#credit
def credit():
    try:
        mycursor.execute("SELECT * FROM BANK")
        acc=input("Enter the Account number: ")
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                amt=float(input("Enter Credit Amount: "))
                i[7]+=amt
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                db.commit()
                print("Amount Credited Successfully.")
                break
        else:
            print("Record Not Found.")
    except:
        print("Table Doesn't Exist.")



print('''ProjektX 0.1.1 (tags/v0.1.1:, Oct 10 2022, 22:06:33) [MSC v.1950 64 bit (Intel)] on win32
Type "menu" "copyright", "credits" or "license" for more information.''')
print("-"*133)

while True:
    comm=input(">>>")
    if comm=="copyright":
        print('''Copyright (c) 2022-2023 Virender Saini.
All Rights Reserved.
''')
    elif comm=="credits":
        print('''Virender Saini''')
        
    elif comm=="license":
        print('''All ProjektX releases including the ones being in early stage of developement are NOT Open Source.
Ironically, most, but not all.
Any attempt to changes in the source code of the project can have its equivalent consequences.

This project was developed as an year-end project for the AISSCE 2022-23.
For further licensing information (which actually doesn't exist), Contact the Computer Science Department, DPGS(2022-23).
''')
        
    elif comm=="menu":
        while True:
            menu()
            chce=int(input("Enter Your Choice: "))
            if chce==1:
                insert()
                continue
            elif chce==2:
                while True:
                    menusort()
                    chce2=input("Enter your choice [a/b/c/d]: ")
                    if chce2=="a" or chce2=="A":
                        dispsortacc()
                        continue
                    elif chce2=="b" or chce2=="B":
                        dispsortname()
                        continue
                    elif chce2=="c" or chce2=="C":
                        dispsortbal()
                        continue
                    elif chce2=="d" or chce2=="D":
                        break
                    else:
                        print("Invalid")
                        continue
            elif chce==3:
                srch()
                continue
            elif chce==4:
                recupdate()
                continue
            elif chce==5:
                dlt()
                continue
            elif chce==6:
                while True:
                    menutransaction()
                    chce3=input("Enter your Choice [a/b/c]: ")
                    if chce3=="a" or chce3=="A":
                        debit()
                        continue
                    elif chce3=="b" or chce3=="B":
                        credit()
                        continue
                    elif chce3=="c" or chce3=="C":
                        break
                    else:
                        print("Invalid")
                        continue
            elif chce==7:
                print("Babye...")
                break
            else:
                print("Invalid")
                continue
    else:
        print("That's not what I expected.")
    

