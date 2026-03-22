#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples element-wise and returns a new tuple.

    Args:
        tuple_a (tuple): The first tuple to add. Defaults to an empty tuple.
        tuple_b (tuple): The second tuple to add. Defaults to an empty tuple.

    Returns:
        tuple: A new tuple containing the element-wise sum of the input tuples.
    """
    # Ensure both tuples have at least 2 elements by padding with zeros if necessary
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Return a new tuple with the element-wise sum
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
