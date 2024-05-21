# A basic implementation of a selection sort

# A selection sort splits the list into a sorted and unsorted portion
# As each element is checked, it is moved from the unsorted portion to
# the sorted portion. With each iteration, the size of the sorted portion
# grows and the unsorted shrinks until the list is completely sorted.

# Where a selection sort differes from a bubble sort is that the
# selection sort always works with the next lowest element and places
# it in the correct position in the sorted side of the list.

# A selection sort will iterate once for each element in the list
# Big O: O(n^2) where n is the number of elements in the list

# NOTE: This coded is meant to serve as a tutorial so it has
#       more comments than would normally be found

numberList = [54,78,23,900,1,65,87,23,75,26,435,34,768,34,6,78,93]
iterationCounter = 0    # This is used only to report on how the number of iterations
unsortedIndex = 0       # The entire list is presumed to be unsorted
currentIndex = 0        # Start at the beginning of the list

print(numberList)

# Keep iterating until the unsorted portion of the list no longer exists
while unsortedIndex < len(numberList):

    # Find the lowest unsorted value
    currentIndex = unsortedIndex
    while currentIndex < len(numberList)-1:
    
        # swap the lower value with the value at the start of the
        # unsorted portion. This ensures that the lowest unsorted
        # value will be at the top when this iteration is complete
        if numberList[unsortedIndex] > numberList[currentIndex+1]:
            tempNumber=numberList[unsortedIndex]
            numberList[unsortedIndex] = numberList[currentIndex+1]
            numberList[currentIndex+1] = tempNumber

        currentIndex += 1

    print(f"{unsortedIndex} - {numberList}")

    # Change where the unsorted portion begins
    unsortedIndex += 1
    iterationCounter += 1

# print the resulting list and some statistics
print(numberList)
print(f"{iterationCounter} iterations to sort {len(numberList)} elements.")