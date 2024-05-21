# A basic implementation of a bubble sort
# These sorts are very simple, but also very slow since 
# the list must be iterated through completely multiple times
# As list size grows, compute time increases
# NOTE: This coded is meant to serve as a tutorial so it has
#       more comments than would normally be found

numberList = [54,78,23,900,1,65,87,23,75,26,435,34,768,34,6,78,93]
sortActionTaken = True  # Set to True so that the loop will execute at least once
iterationCounter = 0    # This is used only to report on how the number of iterations

# iterate through the list until a loop completes without any sort actions being taken
print(numberList)
while sortActionTaken:
    sortActionTaken = False # Set to False so the loop will end unless a sort action is taken
    iterationCounter += 1

    # check each element of the list and move the lower values toward the left/top
    index = 0   # Lists are 0-based so always start with the first element

    # Iterate through each element of the list (leave one element at the end to compare against)
    while index < (len(numberList) - 1):

        # If the current element is larger than the next element, then they need to be swapped
        if numberList[index] > numberList[index+1]:
            # Sort action was taken so set the flag to True
            sortActionTaken = True

            # swap numbers
            tempNumber=numberList[index]
            numberList[index] = numberList[index+1]
            numberList[index+1] = tempNumber

            # print the current list
            print(numberList)

        # move to the next element in the list
        index += 1

# print the resulting list and some statistics
print(numberList)
print(f"{iterationCounter} iterations to sort {len(numberList)} elements.")