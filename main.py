
import csv


def option1():
    day = input("Enter a day in the format MM-DD-YYYY: ")
    count = 1
    for row in data:
        if data[count][0] == day:
            print("The top song on  {} was {} by {}.".format(
                    day, data[count][2], data[count][3]))
            break
        count += 1

def option2():
    artist = input("Enter an artist: ")
    count = 0
    for i in range(1, 101):
        if data[i][3] == artist:
            count += 1

    print("{} has {} songs in the top 100.".format(artist, count))


def option3():
    lst = []
    top_lst = []

    for row in data[1:]:
        lst.append(row)

    for i in range(0, 10):
        max_week = max(lst, key=lambda sublist: sublist[6])
        top_lst.append(max_week)
        lst.remove(max_week)

    print("The top 10 songs with longest no. of weeks on board are as:\n")
    for l in top_lst:
        print("{} by {} was on the board for {} weeks.".format(l[2], l[3], l[6]))
        print("\n")


def option4():
    print("The song that moved the most on the board was {} by {}.".format(data[-1][3], data[-1][2]))


def option5():
    listt = []
    artist = input("Enter the artist name: ")
    print("The top 10 songs of  {} are:".format(artist))
    for row in data:
        if artist in row:
            listt.append(row)

    for l in listt[:10]:
        print(f"{l[2]} with a ranking of {l[1]}")


with open('charts.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    print("This program allows you to explore the Billboard Top 100 Songs data set.")
    print("Please select from the following options:")
    print("1 - Retrieve the details for the top ranked song for a particular day")
    print("2 - Retrieve the details of the artist with the most top ranked songs")
    print("3 - Retrieve the details of the 10 songs with the longest number of weeks on the board")
    print("4 - Retrieve the song that has moved the most in ranking on the board")
    print("5 - Visualize the top songs (the criteria for 'top' is up to you)")
    print("6 - Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        option1()

    elif choice == 2:
        option2()

    elif choice == 3:
        option3()

    elif choice == 4:
        option4()

    elif choice == 5:
        option5()

    elif choice == 6:
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        exit()


