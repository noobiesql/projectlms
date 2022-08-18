import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="nopassword",database="library")

def addbook():
  bn=input("enter book name :")
  c=input("enter book code :")
  t=input("total books :")
  s=input("enter subject :")
  data=(bn,c,t,s)
  sql='insert into books values(%s,%s,%s,%s)'
  c=con.cursor()
  c.execute(sql,data)
  con.commit()
  print("____________________")
  print("Data entered successfully")
  main()

def issueb():
  n=input("enter name :")
  r=input("enter reg no :")
  co=input("enter book code :")
  d=input("enter date :")
  a='insert into issue values(%s,%s,%s,%s)'
  data=(n,r,co,d)
  c=con.cursor()
  c.execute(a,data)
  con.commit()
  print("____________________")
  print("Book isuued to:" ,n)
  bookup(co,-1)

def submitb():
  n=input("enter name :")
  r=input("enter reg no :")
  co=input("total book code :")
  d=input("enter date :")
  a='insert into submit values(%s,%s,%s,%s)'
  data=(n,r,co,d)
  c=con.cursor()
  c.execute(a,data)
  con.commit()
  print("____________________")
  print("Book isuued to:",n)
  bookup(co,1)

def bookup(co,u):
   a="select TOTAL from books where BCODE =%s"
   data=(co,)
   c=con.cursor()
   c.execute(a,data)
   myresult=c.fetchone()
   t=myresult[0]+u
   sql="update books set TOTAL =%s where BCODE=%s"
   d=(t,co)
   c.execute(sql,d)
   con.commit()
   main()

def dbook():
    ac=input("enter book code :")
    a="delete from BOOKS where BCODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def dispbook():
    a="select*from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("book name:",i[0])
        print("book code:",i[1])
        print("total: ",i[2])
        print("subject: ",i[3])
        print("____________________")
    main()

def main():
    print("""                    LIBRARY MANAGEMENT
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOKS
    """)   
    choice=input("enter task number:")
    print("_________________")
    if (choice=="1"):
        addbook()
    elif (choice=="2"):
        issueb()
    elif (choice=="3"):
        submitb()
    elif (choice=="4"):             
        dbook()
    elif (choice=="5"):
        dispbook()
    else: 
        print("wrong choice")    
    main()           

def pswd():
    ps=input("enter password: ")
    if ps=="123456":
        main()
    else:
        print("wrong password")
        pswd()
pswd()        

