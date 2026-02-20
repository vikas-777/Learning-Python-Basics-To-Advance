number = 7
attempts = 3
while attempts > 0:
    guess = (int(input("Enter the number")))
    if guess == 7:
        print("Your guess is correct")
        break
    else:
        print("Your guess is wrong")
        attempts -= 1
if attempts == 0:
    print("You have completed your attempts")
