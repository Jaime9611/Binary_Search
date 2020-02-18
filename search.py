"""Binary Search Script"""


def binary_search(target, sample):
    """Function to search a item in the sample list."""
    min = 0
    max = len(sample) - 1
    found_position = None

    while True:
        if max < min:
            found_position = -1
            break

        guess = (min + max ) // 2

        if sample[guess] == target:
            found_position = guess
            break
        elif sample[guess] < target:
            min = guess + 1
        elif sample[guess] > target:
            max = guess - 1

    if found_position == -1:
        return "Number wasn't found in the list."
    else:
        return found_position


if __name__ == "__main__":
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
         43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] # lista de prueba
    res = binary_search(83, l)
    print(res)
    if type(res) == int:
        print(l[res])