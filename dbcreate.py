import mysql.connector

db=mysql.connector.connect(user="root",
                           host="localhost",
                           passwd="1Iam@9it",
                           database="temp")
mycursor=db.cursor(buffered=True)

st='''CREATE TABLE BANK(
ACCNO CHAR(8),
NAME CHAR(30),
MOBILE CHAR(10),
EMAIL CHAR(30),
COMPLETE_ADDRESS CHAR(30),
CITY CHAR(20),
STATE CHAR(20),
BALANCE FLOAT(10,2));'''
mycursor.execute(st)
db.commit()


l=[["10011401","RAMESH KUMAR","8565231465","rameshkumar54@gmail.com","MANPUR,BUDH BAZAAR","MORADABAD","UTTAR PRADESH",10550.50],["10011402","ARBAAZ KHAN","7856321025","arbaaz1950@yahoo.com","GALI NO.3, KARULA","MORADABAD","UTTAR PRADESH",9500.50],["10011403","FUZAIL AHMED","9785250065","fuzail25ahmed@gmail.com","CIVIL LINES","MORADABAD","UTTAR PRADESH",25000.00],["10011404","SUMNESH RASTOGI","6965200232","drrastogi@hotmail.com","PRABHAT MARKET","MORADABAD","UTTAR PRADESH",100950.75],["10011405","ANMOL RATAN","8423019635","ratantata@gmail.com","GANDHI NAGAR","MORADABAD","UTTAR PRADESH",5550.50],["10011406","VISHESH THAKUR","6752365414","thakurvishesh@gmail.com","PANDIT NAGLA","MORADABAD","UTTAR PRADESH",15010.30],["10011407","SHAKTI KAPOOR","9023654788","shaktikapoor@yahoo.com","MANSAROVER COLONY","MORADABAD","UTTAR PRADESH",20000.55]]


for i in l:
    cmd="INSERT INTO BANK VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(cmd,i)
    db.commit()
