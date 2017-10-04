import sqlite3
import time
import os
from decimal import Decimal



conn = sqlite3.connect('jamesPOS.db')
c = conn.cursor()
total = float(0.00)

def creatTable():
       c.execute('CREATE TABLE IF NOT EXISTS price(product TEXT, cost TEXT, product_id TEXT)')
       c.execute('CREATE TABLE IF NOT EXISTS login(usr TEXT, Pass TEXT)')



def dataEntry():

       print('Please type a product name')
       product = input()

       print('Please type a price')
       cost = input()


       print('please type the id for your product')
       product_id = input()
             
       c.execute("INSERT INTO price(product, cost, product_id) VALUES (?,?,?)", (product, cost, product_id))
       conn.commit()
       print('do you want to add another product? y/n')
       loop = input()
       if loop == 'y':
              dataEntry()
       else:
              os.system('cls')
              main()
def addUsr():
       global usrName

       if usrName == 'admin':
              print('new username')
              newUsr = input()
              print('new password')
              newPass = input()

              c.execute("INSERT INTO login(usr, Pass) VALUES (?,?)", (newUsr, newPass))
              conn.commit()
              os.system('cls')
              main()

              

def machine():
       global total
       print('If finished type /')
       search = input('Please type or scan the product id: ')

       if search == '/':
              print('Total to pay is:£','{0:.2f}'.format(total))
              payment = float(input('Ammount given:£'))
              change = float(total-payment)
              print('Change:£','{0:.2f}'.format(change))
              time.sleep(3)
              total = float(0.00)
              os.system('cls')
              main()
       else:
              
              c.execute("SELECT * FROM price WHERE product_id =?",(search,))
              for row in c.fetchall():
                     print(row[0],row[1])
              #total is at the top
              price = float(row[1])
              amount = int(input('quantity = '))
              total = float(total+price*amount)
              print('Your overall total is:£','{0:.2f}'.format(total))       
              machine()

def productCheck():
       search = input('Please type or scan the product id: ')
       c.execute("SELECT * FROM price WHERE product_id =?",(search,))
       for row in c.fetchall():
              print(row[0],row[1])
       time.sleep(1)
       os.system('cls')
       main()

def productList():
       c.execute("SELECT * FROM price")
       for row in c.fetchall():
              print(row)
       print('press / to exit')
       leave = input()
       if leave == '/':
              os.system('cls')
              main()
       else:
              productList()
def userCheck():
       c.execute("select * FROM login")
       for row in c.fetchall():
              print(row)
       print('press / to exit')
       leave == input()
       if leave == '/':
              os.system('cls')
              main()
       else:
              userCheck()

def main():
       
       global cls
       print('Welcome to James POS')
       print('What do you want to do?')
       print('option 1: Add a product')
       print('Option 2: Add user')
       print('option 3: Product check')
       print('option 4: Use the POS')
       print('option 5: Show all products')
       print('option 6: Show all users')
       print('option 7: Logout')
       action = input()

       if action == '1':
              os.system('cls')
              dataEntry()
       elif action =='2':
              os.system('cls')
              addUsr()
       elif action == '3':
              os.system('cls')
              productCheck()
       elif action == '4':
              os.system('cls')
              machine()
       elif action == '5':
              os.system('cls')
              productList()
       elif action == '6':
              os.system('cls')
              userCheck()
       elif action == '7':
              os.system('cls')
              logout()
       else:
              print('Sorry something went wrong')
              main()

def login():
       global usrName

#optional admin login
       newUsr = 'admin'
       newPass = 'admin'
       c.execute("INSERT INTO login(usr, Pass) VALUES (?,?)", (newUsr, newPass))
       conn.commit()
       
       usrName = input('User: ')
       usrPass = input('Pass: ')

       if usrName == 'admin':
              if usrPass == 'admin':
                     main()
       else:
       
              c.execute("SELECT * FROM login WHERE usr =? AND Pass =?",(usrName, usrPass))

              for row in c.fetchall():
                     usrNameInput = row[0]
                     usrPassInput = row[1]
        
              if usrNameInput == usrName:
                     if usrPassInput == usrPass:
                            main()
                     else:
                            print('sorry your username or password is incorrect!')
                            login()
              
              
creatTable()              
login()    
c.close()
conn.close()       
