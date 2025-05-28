from zxcvbn import zxcvbn
import random
import time

#Ask the user the which mode they want to use Mode 1/ Mode 2
def main():
    check1=False
    check2=False
    check3=False
    while check1 == False:
        mode=ask_for_mode()
        if mode == "1":
            password=input("Please enter your password: ")
            required_time=mode1(password)
            print(f"The estimate time to crack your password by brute force is {required_time}.\n")
        elif mode == "2":
            while check3 == False:
                try:
                    digit=int(input("How many digits ur password wanna have? (6-15): "))
                except ValueError:
                    print("\nPlease enter a integer value")
                    time.sleep(1)
                    continue
                check3=True
            password=mode2(digit)
            print(f"Your password is {password}\n")

        #Ask the user to use another mode or not
        while check2 == False:
            again=input("Would you like to try a different mode? (yes/no): ")
            if again == "yes":
                check2 = True
            elif again == "no":
                check1 = True
                check2 = True
            else:
                print("Invalid input")
                continue
        check2=False
    print("\nThank you for using my password project\n")

def ask_for_mode():
    while True:
        print("Welcome to PassGuard!")
        mode=input("\nPlease enter the mode number \nType 1 for Password strength test \nType 2 for Random password generator\nMode choice: ")
        if mode != "1" and mode !="2":
            print("Invalid Mode")
            continue
        else:
            return mode

#Mode 1 function test the strength of the password
def mode1(password):
    #create a dict for the different level of score to the rating of the strength
    checkscore={
        0:"very weak",
        1:"weak",
        2:"normal",
        3:"good",
        4:"strong",
    }
    #assign different value to its own variable
    result=zxcvbn(password)
    required_time = result["crack_times_display"]["online_no_throttling_10_per_second"]
    score=result["score"]
    feedback=result["feedback"]["suggestions"]
    check=bool(result["feedback"]["warning"])
    strength=checkscore[score]

    #Output the comment , time to crack and strength of password
    print("Loading")
    for _ in range(3):
        print(". ", end='', flush=True)
        time.sleep(1)
    print(f"\nYour password ({password}) is {strength}, it got {score} out of 4.\n")
    if check == True:
        print(f"Here is some feedback of your password: \n{feedback}\n")
    return required_time

def mode2(digit):
    password = ""
    #ask for digit and check if it's valid or not
    while True:
        if digit < 6 or digit > 15:
            print("\nOut of range plz re-enter:")
            continue
        else:
            break

    #generate random character and number
    generated=[]
    for _ in range(4):
        num=random.randint(0,9)
        lower=chr(random.randint(ord("a"),ord("z")))
        upper=chr(random.randint(ord("A"),ord("Z")))
        symbol=random.choice("!@#$%^*()_+-=")
        generated.append(num)
        generated.append(lower)
        generated.append(upper)
        generated.append(symbol)
        random.shuffle(generated)

    #get the password out of the array
    for i in range(digit):
        character = str(generated[i])
        password += character

    #Output the password that generated randomly for the user
    print("Loading")
    for _ in range(3):
        print(". ", end='', flush=True)
        time.sleep(1)
    return password

if __name__ == "__main__":
    main()