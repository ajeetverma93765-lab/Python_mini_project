balance = 5000
correct_pin = "1234"
attempt = 0

while attempt < 3: 
    pin = input("Enter ATM Pin:")
    if pin == correct_pin:    
        print("login sucsecfully:")
        break
    else:
        attempt += 1
        print("Wrong Pin:")    
if attempt == 3:
    print("ATM Blocked")
    exit()
    
history = []

while True:        
    print("=========MENU==========")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdral")
    print("4. Transaction History")
    print("5.Exit")
            
    choice = input("Enter your choice:")
    if choice == "1":
        print("Your balance is:", balance)
    elif choice == "2":
        amount = int(input("Enter your deposit amount:"))
        balance += amount
        history.append(f"Deposit : +{amount}")
        print("Deposit Sucsecfully!")
    elif choice == "3":
        withdral = int(input("Enter your withdral amount:")) 
        if withdral <= balance: 
            balance -= withdral
            history.append(f"Withdral : -{withdral}")
            print("withdral sucsecfully")
        else:
            print("Insufficient Balance") 
    elif choice == "4":
        print("\n=======Transaction History=======")   
        if len(history) == 0:
            print("No transaction histry")
        else:
            for item in history:
                print(item)    
                 
                
    elif choice == "5":
        print("Thank You! Visit Again:")
        break
    else:
        print("Invalid Choice:")            