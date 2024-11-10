def check_balance(balance):
    print(f"Your balance is ₹{balance:.2f}")

def deposit(balance):
    amount = float(input("Enter the amount to be deposited: "))
    
    if amount < 0:
        print("Please enter a valid amount")
        return balance  
    else:
        return balance + amount  

def withdraw(balance):
    amount = float(input("Please enter the amount to withdraw: "))
    
    if amount > balance:
        print("Insufficient balance")
        return balance  
    elif amount < 0:
        print("Please enter a valid amount")
        return balance  
    else:
        return balance - amount 

def main():
    balance = 100  
    is_running = True

    while is_running:
        print("\nEnter your choice:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
    
        choice = input("Enter your choice (1-4): ")
    
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)  
        elif choice == "3":
            balance = withdraw(balance)  
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice.")
        
    print("Thank you, have a nice day!")


if __name__ == '__main__':
    main()
