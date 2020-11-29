# Andrew Li
# 1824794

# Global variable
num_calls = 0


def partition(user_ids, i, k):
    midpoint = i + (k-i) // 2
    pivot = user_ids[midpoint]

    # initialize variables
    done = False
    l = i
    h = k
    while not done:
        # Increment 1 while user_ids[l] < pivot
        while user_ids[l] < pivot:
            l = l + 1
        # Decrement h while pivot < user_ids[h]
        while user_ids[h] > pivot:
            h = h - 1
            if l >= h:
                done = True
            else:
                """ Swap numbers[l] and numbers[h],
                update l and h """
                temp = user_ids[l]
                user_ids[l] = user_ids[h]
                user_ids[h] = temp
                l = l + 1
                h = h - 1
            return h


def quicksort(user_ids, i, k):
    j = 0

    if i >= k:
        return

    j = partition(user_ids, i, k)

    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        print(user_id)
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
