
number= input("Guess a number 1-9")
print('Enter guess:', number)
if (pocketMoney<5):
    print("Guess higher!")
elif(pocketMoney>6 and pocketMoney<10):
    print("Guess Lower!")
else:
    print("You Won!!")

chances<5

if not chances <5:
    print("You lose! The number is", number)