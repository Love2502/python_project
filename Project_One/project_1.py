name = input("Type your name: ")
print(" Hello " + name + " Welcome to the jungle game ")

should_we_play = input(" Do you want to play? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print(" We are going to play.")

    directiom = input(" Do you want to go left or right in the jungle path ? (left/right)")

    if directiom == "left":
        print(" okay you went left and the lion killed you, YOU DIE! THE END ")

    elif directiom=="right":
        choice = input( " Now you see a giant fallen tree, do you wanna go back for another path  or cross it ? (back/cross)")
        if choice == "back":
            print(" You couldn't reach the other path, you die, THE END" )
        else:    
            print(" you went right and you found a flying carpet, you escaped succesfully , YOU WON")

    else:
        print(" No such direction exists...")

    print(" Try a new game ")