runPlayer1=int(input("enter run of player 1 "))
runPlayer2=int(input("enter run of player 2 "))
runPlayer3=int(input("enter run of player 3 "))
strikeRate1=runPlayer1*100 / 60
strikeRate2=runPlayer2*100 / 60
strikeRate3=runPlayer3*100 / 60
print("Strike rate of player 1 is ",strikeRate1)
print("Strike rate of player 2 is ",strikeRate2)
print("Strike rate of player 3 is ",strikeRate3)
print("Run when player 1 played 60 balls more ",runPlayer1*2)
print("Run when player 2 played 60 balls more ",runPlayer2*2)
print("Run when player 3 played 60 balls more ",runPlayer3*2)
print("Maximum no of six player 1 could have hit ",runPlayer1//6)
print("Maximum no of six player 2 could have hit ",runPlayer2//6)
print("Maximum no of six player 3 could have hit ",runPlayer3//6)
