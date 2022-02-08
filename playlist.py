import random 
song = ['"love story" by Taylor Swift', '"perfect" by Ed Sheeran"','"levitating" by Dua Lipa', '"deja vu" by Olivia Rodrigo"' ] 
choice = input("Do you want to shuffle your music? Enter 's' for shuffle or 'c' for chronological: ")

s =  random.choice(song) 
x = 0 
chronological = song[x]

if (choice == 's'):
    print(s) 
    another = input("Do you want to play another song? enter 'y' for yes or 'n' for no: ")  
    while (another == 'y'):
        s = random.choice(song)
        print(s)
        another = input("Do you want to play another song? enter 'y' for yes or 'n' for no: ")  
        if (another == 'n'):
            print("thanks for listening! :) ")
                
elif (choice == 'c'):
    x = 0
    chronological = song[x]
    print(chronological) 
    another = input("Do you want to play another song? enter 'y' for yes or 'n' for no: ")  
    while (another == 'y') and (x+1 < len(song)):
        x = x + 1
        print(song[x]) 
        another = input("Do you want to play another song? enter 'y' for yes or 'n' for no: ") 
        if (another == 'n'):
            print("thanks for listening! :) ")
    while (another == 'y') and (x+1 >= len(song)):
        print("no more songs! you've reached the end of the playlist!")
        break 
else:
    print("please stop running the program and follow the instructions by entering 's' or 'c' next time.")
