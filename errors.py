"""Errors Script"""

# Exception classes
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotOrderedListError(Error):
    """Exception raised for an error of unordered list."""
    pass

class NotSameTypeError(Error):
    """Exception raised for an error of unordered list."""
    pass


def check_sample(sample):
    """Function for test if it is a ordered list."""

    options = [_check_if_equal_types, _check_if_sorted]

    for f in options:
        f(sample)


def _check_if_sorted(sample):
    """Raise an error if the list is not ordered."""

    if sorted(sample) != sample:
        raise NotOrderedListError("The list given isn't ordered.")


def _check_if_equal_types(sample):
    """Raise an error if the list has items of different type."""

    type_sample = type(sample[0])

    test = all(isinstance(item, type_sample) for item in sample)

    if test == False:
        raise NotSameTypeError("List of elements with different type.")
