player1=int(input("What is your choice? 0 for Rock,1 for Paper,2 for Scissors"))
player2=int(input("Enter your choice:0 for Rock,1 for Paper,2 for Scissors"))
if player1=="0" & player2=="2":
    print("player1 wins!")
elif player2=="0" & player1=="2":
    print("player2 wins!")
elif player1>player2:
    print("player1 wins!")
elif player2>player1:
    print("player2 wins!")
elif player1==player2:
    print("it's a draw")
else:
    print("You type a invalid number")