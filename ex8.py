#!/usr/bin/python3

print("ROCK PAPER SCISSORS")
while True:
    usr_command = input("Type 'start' to play or 'q' to quit: ")
    if str(usr_command) == "q":
        break
    if usr_command == "start":
        print("Let's play!!!\nr = rock\np = paper\ns = scissors\n")
        p1 = input("Player1 type your choice: ")
        p2 = input("Player2 type your choice: ")
        while p1 != p2:
            if p1 == "s" and p2 == "r":
                print("Player2 is winner!")
                break
            elif p1 == "s" and p2 == "p":
                print("Player1 is winner!")
                break
            elif p1 == "r" and p2 == "s":
                print("Player1 is winner!")
                break
            elif p1 == "r" and p2 == "p":
                print("Player2 is winner!")
                break
            elif p1 == "p" and p2 == "s":
                print("Player2 is winner!")
                break
            elif p1 == "p" and p2 == "r":
                print("Player1 is winner!")
                break

        