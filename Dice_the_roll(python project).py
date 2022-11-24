import random
score=0
while(True):
    n=int(input("Please Enter a static number between 1 to 6 :  "))
    r=random.randint(1,6)
    print("on rolling the dice ,the randomly generated value is : ",r)
    if(n==r):
        score+=1
        print("Congrats !!! You WON")
        print("Score: ",score)
    else:
        print("Better luck next time")
        print("Score: ", score)
    ch=input("Do you want to continue (yes/no) : ").lower()
    if(ch=="no"):
        print("Thank You .  Your present Score is : ",score)


