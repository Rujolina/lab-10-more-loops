maximum_stories = 11
userinput = input("On what floor of the building is your office? ")
floor = int(userinput)
while floor > maximum_stories:
    print("You entered " + str(floor) + ". There are only 13 floors in the building. Try again.")
    userinput = input("On what floor of the building is your office? ")
    floor = int(userinput)
    print("Oh nice. Floor " + str(floor) + " exists in this building.")
