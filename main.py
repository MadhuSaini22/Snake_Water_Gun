import random
list=["g","w","s"]
print("Snake,Water and Gun Game!!")
i=1
chances=10
c=0
co=0
while i<=chances:
    computer=random.choice(list)
    choice=input("Enter your choice from s for snake\n,g for gun\n,w for water\n")
    if(choice=='g' or choice=='w' or choice=='s'):
        if(computer=='g' and choice=='w'):
            print("you won!!")
            c=c+1
        if (computer == 'g' and choice == 'g'):
            print("Oops!! tie")
        if (computer == 'g' and choice == 's'):
           print("you failed!")
           co=co+1
        if (computer == 'w' and choice == 'w'):
            print("Oops!! tie")
        if (computer == 'w' and choice == 'g'):
            print("You failed!")
            co=co+1
        if (computer == 'w' and choice == 's'):
              print("you won!!")
              c=c+1
        if (computer == 's' and choice == 'w'):
              print("you failed!")
              co=co+1
        if (computer == 's' and choice == 'g'):
              print("you won!!")
              c=c+1
        if (computer == 's' and choice == 's'):
              print("Oops!!tie")
        i=i+1
    else:
        print("Invalid input")
        i=i+1
print("your score:",c)
print("computer's score",co)
if(c>co):
    print("Hurray,Finally you won this Game!!")
elif c==co:
    print("Game Tied Finally!!")
else:
    print("Oops,Finally you lost!!")
