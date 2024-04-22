import random
import sys
while True: # this loop is to make the game repeatable
    tries = 0
    number = 0
    max_tries = 0
    
    num_of_players = int(input("Enter number of players from 1 to 6")):
    if num_of_players==1:
        continue
    while num_of_players<1 or num_of_players>6:
        print("Error,wrong invalid input given,try again: ")
        num_of_players = int(input("Enter number of players from 1 to 6"))
    if num_of_players==2:
        p1_score=0
        p2_score=0
        print("Total players: 2")
    elif num_ofplayers==3:
        p1_score=0
        p2_score=0
        p3_score=0
         print("Total players: 3")
    elif num_ofplayers==4:
        p1_score=0
        p2_score=0
        p3_score=0
         print("Total players: 4")
    elif num_ofplayers==5:
        p1_score=0
        p2_score=0
        p3_score=0
        p4_score=0
        p5_score=0
         print("Total players: 5")
    elif num_ofplayers==6:
        p1_score=0
        p2_score=0
        p3_score=0
        p4_score=0
        p5_score=0
        p6_score=0
         print("Total players: 6")
    number = random.randint(1,100)
    print("Welcome to guess game.")
    print("If you want to quit type q.")
    print("If you want to start over type r.")
    while True: # chacks for right variable
        max_tries = input("Whats the number of max attempts you want to have: ")
        if max_tries.lower() == "q": #completly ends the game
            sys.exit()
        elif max_tries.lower() == "r": # restarts the game
            continue
        try:
            max_tries = int(max_tries)
        except ValueError:
            print("thats not a number")
        else:
            break
    while max_tries>tries:
        guess = input("Enter a number from 1-100: ") # you dont need to include it all ifs
        if guess.lower() == "q": # completly ends the game
            sys.exit()
        elif guess.lower() == "r": # restarts the game
            break
        try: 
            guess = int(guess)
        except ValueError:
            print("thats not a number")
            continue
        tries += 1
        if guess>number:
            print(f'number is too high,attempts {tries}')
        elif guess<number:
            print(f'number is too small,attempts {tries}')
        else:
            print(f'Correct, you found the number!!: {number}\n\n') # no need for othe if since its already part of the while
            break
    if max_tries <= tries:
        print("Game over you lose because you reached the max number of attempts")
        print(f"The number was: {number}\n\n")
