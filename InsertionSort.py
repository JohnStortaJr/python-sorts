# A basic implementation of an insertion sort

# An insertion sort is, perhaps, the most direct approach to sorting.
# Each value is evaluated individually and placed in the proper location
# All other values are shifted accordingly.

# NOTE: This code is meant to serve as a tutorial so it has
#       more comments than would normally be found

numberList = [54,78,23,90,1,65,87,23,75,26,43,34,68,34,6,78,93]
iterationCounter = 0    # This is only used to report on the number of iterations
unsortedIndex = 1       # The 1st element [0] is considered sorted so start at the 2nd element [1]

print(numberList)

# Starting with the second element, place each value the correct location
# Shift all values as needed and extend the end of the sorted list by incrementing the unsortedIndex
# Repeat for each subsequent element.

# Iterate sequentially through all elements of the unsorted portion of the list
while unsortedIndex < len(numberList):

    # Start at the beginning of the list and look for the correct location for value at unsortedIndex
    currentIndex = 0

    # Iterate through the list until reaching the end of the sorted values
    # or finding a value > the current unsortedIndex value
    while currentIndex < unsortedIndex and numberList[currentIndex] <= numberList[unsortedIndex]:    
        # currentIndex is still within the sorted portion and the current value is <= the unsortedIndex value we are looking for
        # Increment to the next index and iterate through the loop again
        currentIndex += 1

    # currentIndex is where the current value needs to go in the list

    # If the search reached the end of the sorted values, then there is nothing to do as the value is already in the correct location
    # Otherwise, shift all elements down and insert the unsorted value into the currentIndex location
    if currentIndex < unsortedIndex:
        # Make note of where the unsorted portion begins and the value at that location
        # This is the value that will be placed in the list at the currentIndex
        tempIndex = unsortedIndex
        tempNumber = numberList[unsortedIndex]

        # Shift all elements down in the list to make room for the value to be inserted
        while tempIndex > currentIndex:
            numberList[tempIndex] = numberList[tempIndex-1]
            tempIndex -= 1
    
        # Insert current value at the currentIndex
        numberList[currentIndex] = tempNumber

    print(f"{unsortedIndex} - {currentIndex} - {numberList}")

    # Change where the unsorted portion begins
    unsortedIndex += 1
    iterationCounter += 1

# print the resulting list and some statistics
print(numberList)
print(f"{iterationCounter} iterations to sort {len(numberList)} elements.")