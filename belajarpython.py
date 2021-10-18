msg = input("What's the secret password: ")

# Password attempt is 3 times, starts at 2, then 1 and ends when counter is 0
num = 3

# bananas is the correct password
while msg != "":
   
 # exhausted all 3 attempts, should print given message.
    if msg == "bananas":
        print("DECRYPT SUCSSESFUL")
        break
    elif num < 1:
            print("Too many wrong attempts. You are locked out!")
            break
    else:
        print(f"Wrong Password! You have {num} chances left")  # password incorrect, display attempts left
        msg = input("What's the secret password: ")
        num = num - 1
        

