import random
tries = 0
number = 0
max_attemts = 0 # just a additional function of the code

while True: # this loop is to make the game repeatable
    print("Welcome to guess game.")
    print("If you want to quit type q.")
    print("If you want to start over type r.")
    
    
    while True: # chacks for right variable
        max_attemts = input("Whats the number of max attempts you want to have: ")
        if max_attemts.lower() == "q": #completly ends the game
            break
        elif max_attemts.lower() == "r": # restarts the game
            continue
        try:
            max_attemts = int(max_attemts)
        except ValueError:
            print("thats not a number")
        else:
            break
    while True: # chacks for right variable
        guess = input("Enter a whole number from 1-100: ")
        if guess.lower() == "q": #completly ends the game
            break
        elif guess.lower() == "r": # restarts the game
            continue

        try: #added try to make sure right variable type
            guess = int(guess)
        except ValueError:
            print("thats not a number")
            continue
        else:
            break
    number = random.randint(1,100) # chenged from 101 to 100 - the description of the function says that it includes both end points
    while guess!= number and loop2_on:
        tries += 1
        if guess>number:
            print(f'number is too high,attempts {tries}')
        elif guess<number:
            print(f'number is too small,attempts {tries}')
        elif tries == max_attemts: # the elif can stay but you need to change > to ==
            print(f'Your number of attempt is finishes, you lose,the number is{number}')
            break # the function 
        while True: #added try loop to make sure right variable type and avoid errors so the game continues
            guess = input("Enter a number from 1-100: ") # you dont need to include it all ifs
            if guess.lower() == "q": # completly ends the game
                loop1_on = False
                loop2_on = False
                break
            elif guess.lower() == "r": # restarts the game
                loop2_on = False
                break
            try: 
                guess = int(guess)
            except ValueError:
                print("thats not a number")
            else:
                break
                
    if number == guess:
        print(f'Correct, you found the number!!: {number}\n\n') # no need for othe if since its already part of the while

