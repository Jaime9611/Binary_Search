"""Binary Search Script"""

from errors import check_sample as check


def binary_search(target, sample):
    """Function to search a item in the sample list."""

    check(sample)
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