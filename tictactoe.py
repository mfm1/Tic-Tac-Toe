import time
import sys
"""
    Tic Tac Toe Game
"""
game_active = True
#Board layout from 1 to 9
board = {
    1 : " ", 2 : " ", 3 : " ",
    4 : " ", 5 : " ", 6 : " ",
    7 : " ", 8 : " ", 9 : " "
}
#Winning combinations
winning_position  = [[1,2,3], [4,5,6],[7,8,9],
    [1,5,9], [3,5,7], [2,5,8],
    [1,4,7], [3, 6,9]
]

#This function prints the game board
def g_board():

    print(board[1] + " | " + board[2] + " | " + board[3])
    print("-" * 9)
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-" * 9)
    print(board[7] + " | " + board[8] + " | " + board[9])

#prompt player 1 (X) to make the first move into any position
def p1():
    print("Your Turn Player X")
    #check to see if the user inputs a valid number or not
    try:
        p_1 = int(input())
    except:
        print("type a number between 1 and 9: ")
        p1()
    #checking to see if a position is empty, if it is, X occupies it
    if board[p_1] == " ":
        board[p_1] = "X"
        g_board()
        winner()
        p2()

    elif board[p1] != " ":
        print("Position {} filled".format(str(p_1)))
        p1()

#prompt player 2 to take a position on the board
def p2():
    print("Your Turn Player O")

    #check to see if player 2 inputs a valid number
    try:
        p_2 = int(input())
    except:
        print("type a number between 1 and 9: ")
        p2()
    #checking to see if a position is empty, if it is O moves in
    if board[p_2] == " ":
        board[p_2] = "O"
        g_board()
        winner()
        p1()

    elif board[p_2] != " ":
        print("Position {} filled".format(str(p_2)))
        p2()

#Checking if we have a winner or a Tie
def winner():
    count = 0

    #checking to see if either X or O occupies a winning position
    for a in winning_position:
        if board[a[0]] == board[a[1]] == board[a[2]] == "X" or board[a[0]] == board[a[1]] == board[a[2]] == "O":
            print("Player X has won the game.")
            time.sleep(2)
            print("Congratulations!!!")
            play_again()

    #Checking to see if there's a Tie
    for a in range(1, 9 + 1):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:
            print("A Tie")
            play_again()

#prompt players if they want to play again
def play_again():
    print("""Do you want to play a new game?
    yes or no""")
    response = input("Yes or No? ")
    if response.title() == "Yes":
        active()
    elif response.title() == "No":
        print("Thank You, Goodbye")
        sys.exit()
    else:
        print("Enter Yes or No.")
        play_again()

#check if game is active
def active():
    while game_active:
        p1()


active()