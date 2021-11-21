import random
rand= random.randint(1,9)
chances=0
while(chances<5):
    number= input("Guess a number 1-9")
    print('Enter guess:', number)
    if (number<rand):
        print("Guess higher!")
    elif(number>rand):
        print("Guess Lower!")
    else:
        print("You Won!!")
    chances+=1
if not chances <5:
    print("You lose! The number is", number)