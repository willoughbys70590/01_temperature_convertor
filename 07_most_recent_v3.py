# Get data from user and stire it in a list, then
# display the most recent three entires nicely

# Set up empty list
all_calculations =[]

# Get five items of Data
get_item = ""
while get_item != "xxx":
    get_item = input("Entre an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("Oops - the list is empty")

else:

    #Show that everything made it to the list..
    print()
    print("*** The Full List ***")
    print(all_calculations)

    # print item starting at the End of the list
    if len(all_calculations) >= 3:
        print("*** Most Recent 3 ****")
        for item in range(0,3):
            print(all_calculations[len(all_calculations) - item - 1])

    else:
        print("*** Items from Newst to Oldest ****")
        for item in all_calculations:
            print(all_calculations[len(all_calculations) - all_calculations.index()])