# Andrew Li
# 1824794

# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        # Find index of largest remaining element
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_largest]:
                index_largest = j

        # Swap numbers[i] and numbers[index_largest]
        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp
        print(*numbers, sep=' ')


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = input().split(" ")
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    selection_sort_descend_trace(numbers)



