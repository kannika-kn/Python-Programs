class ATM:
    def __init__(self,balance):
        self.__balance=balance  #private attribute
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited:{amount}. New balance:{self.__balance}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"withdrew:{amount}. New balance:{self.__balance}")
        else:
            print("insufficient balance")

atm=ATM(1000)
atm.deposit(500)
atm.withdraw(300)      

#2
class user:
    def __init__(self,username,password):
        self.username=username
        self.__password=password  #private attribute
    def get_username(self):
        return self.username
    def check_password(self,password):
        return password==self.__password
user=user("dhanu_mandya","pass7777")
print(user.get_username()) #acess allowed
print(user.check_password("h7777"))  #retuen false
print(user.check_password("pass7777")) #return true
#3
class database:
    def __init__(self):
        self.__storage ={}
    def save_data(self,key,value):
        self.__storage[key]=value
        print(f"Data saved for {key}")
    def get_data(self,key):
        return self.__storage.get(key,"no data found")
db=database()
db.save_data("user_101",{"name":"raj","age":30})
print(db.get_data("user_101"))


