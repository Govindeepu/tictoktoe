# write your code here
game = "         "
game1 = list(game)
print("---------")
print("|"+" "+game1[0]+" "+game1[1]+" "+game1[2]+" "+"|")
print("|"+" "+game1[3]+" "+game1[4]+" "+game1[5]+" "+"|")
print("|"+" "+game1[6]+" "+game1[7]+" "+game1[8]+" "+"|")
print("---------")
position = [[1,1],[1,2],[1, 3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
number1 = "0123456789"
number = list(number1)
empty5 = []
while True:
    x, y = input("Enter the coordinates:").split()
    if (x not in number) or (y not in number):
        print("You should enter numbers!")
    elif int(x) > 3 or int(y) > 3:
        print("Coordinates should be from 1 to 3!")
    elif game1[position.index([int(x), int(y)])] == "X" or game1[position.index([int(x), int(y)])] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        game1[position.index([int(x), int(y)])] = "X"
        print("---------")
        print("|" + " " + game1[0] + " " + game1[1] + " " + game1[2] + " " + "|")
        print("|" + " " + game1[3] + " " + game1[4] + " " + game1[5] + " " + "|")
        print("|" + " " + game1[6] + " " + game1[7] + " " + game1[8] + " " + "|")
        print("---------")
        list1 = [[game1[x] for x in range(3)], [game1[x] for x in range(3, 6)], [game1[x] for x in range(6, 9)]]
        empty0 = []
        empty1 = []
        empty2 = []
        empty3 = [game1[0], game1[4], game1[8]]
        empty4 = [game1[2], game1[4], game1[6]]
        for x in list1:
            empty0.append(x[0])
            empty1.append(x[1])
            empty2.append(x[2])

        b = list1[0].count("O") == 3 or list1[1].count("O") == 3 or list1[2].count("O") == 3 or empty0.count(
            "O") == 3 or empty1.count("O") == 3 or empty2.count("O") == 3 or empty3.count("O") == 3 or empty4.count(
            "O") == 3

        c = list1[0].count("X") == 3 or list1[1].count("X") == 3 or list1[2].count("X") == 3 or empty0.count(
            "X") == 3 or empty1.count("X") == 3 or empty2.count("X") == 3 or empty3.count("X") == 3 or empty4.count(
            "X") == 3
        if b == False and c == False and " " not in empty0 and " " not in empty1 and " " not in empty2:
            print("Draw")
            break
        elif b == False and c == True:
            print("X wins ")
            break
        elif b == True and c == False:
            print("O wins")
            break
        while True:
            x, y = input("Enter the coordinates:").split()
            if (x not in number) or (y not in number):
                print("You should enter numbers!")
            elif int(x) > 3 or int(y) > 3:
                print("Coordinates should be from 1 to 3!")
            elif game1[position.index([int(x), int(y)])] == "X" or game1[position.index([int(x), int(y)])] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                game1[position.index([int(x), int(y)])] = "O"
                print("---------")
                print("|" + " " + game1[0] + " " + game1[1] + " " + game1[2] + " " + "|")
                print("|" + " " + game1[3] + " " + game1[4] + " " + game1[5] + " " + "|")
                print("|" + " " + game1[6] + " " + game1[7] + " " + game1[8] + " " + "|")
                print("---------")
            list1 = [[game1[x] for x in range(3)], [game1[x] for x in range(3, 6)], [game1[x] for x in range(6, 9)]]
            empty0 = []
            empty1 = []
            empty2 = []
            empty3 = [game1[0], game1[4], game1[8]]
            empty4 = [game1[2], game1[4], game1[6]]
            for x in list1:
                empty0.append(x[0])
                empty1.append(x[1])
                empty2.append(x[2])

            b = list1[0].count("O") == 3 or list1[1].count("O") == 3 or list1[2].count("O") == 3 or empty0.count(
                "O") == 3 or empty1.count("O") == 3 or empty2.count("O") == 3 or empty3.count("O") == 3 or empty4.count(
                "O") == 3

            c = list1[0].count("X") == 3 or list1[1].count("X") == 3 or list1[2].count("X") == 3 or empty0.count(
                "X") == 3 or empty1.count("X") == 3 or empty2.count("X") == 3 or empty3.count("X") == 3 or empty4.count(
                "X") == 3
            if b == False and c == False and " " not in empty0 and " " not in empty1 and " " not in empty2:
                print("Draw")
                break
            elif b == False and c == True:
                print("X wins ")
                break
            elif b == True and c == False:
                print("O wins")
                break
            if abs(game1.count("X") - game1.count("O")) == 0:
                break





