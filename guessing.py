i = 1
a = 5
j = 9
while i<=9:
    guess=int(input("guess number between 1 to 9:-"))
    if guess >=1 and guess<=9:
        if guess == a:
            print("well guessed")
            break
        print("try again" + str(j) +"chance r left")
        i+=1
        j-=1
    else:
        print("guess no between 1 to 9")
else:
    print("you lost game")
