# A basic implementation of a bubble sort
# These sorts are very simple, but also very slow as list size increases
# since the list must be iterated through completely multiple times

numberList = [54,78,23,900,1,65,87,23,75,26,435,34,768,34,6,78,93]
sortActionTaken = True
iterationCounter = 0

# iterate through the list until a loop completes without any sort actions being taken
print(numberList)
while sortActionTaken:
    sortActionTaken = False
    iterationCounter += 1

    # check each element of the list and move the lower values toward the left/top
    index = 0
    while index < (len(numberList) - 1):
        if numberList[index] > numberList[index+1]:
            sortActionTaken = True

            # swap numbers
            tempNumber=numberList[index]
            numberList[index] = numberList[index+1]
            numberList[index+1] = tempNumber
            print(numberList)

        index += 1

print(numberList)
print(f"{iterationCounter} iterations to sort {len(numberList)} elements.")