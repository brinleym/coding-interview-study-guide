def main():

    # Empty set
    empty_set = set()
    print(f"empty set: {empty_set}\n")

    # Non-empty set
    my_set = {1, 2, 3, 4, 4, 4}
    print(f"set: {my_set}\n") # Duplicates will be removed

    # Heteregeneous set
    heterogeneous_set = {1, 0.5, True, "cat"}
    print(f"heterogeneous set: {heterogeneous_set}\n")

    # Length of set
    length = len(my_set)
    print(f"length of {my_set}: {length}\n")

    # Add to set
    my_set.add(5)
    print("my_set.add(5)")
    print(f"set: {my_set}\n")

    # Remove from set
    my_set.remove(5)
    print("my_set.remove(5)")
    print(f"set: {my_set}\n")

    # Check membership
    found = 1 in my_set
    print(f"1 in my_set: {found}\n")

    # Shallow copy
    shallow_copy = my_set.copy()
    print(f"shallow copy of {my_set}: {shallow_copy}\n")

    # Set comprehensions
    new_set = {char for char in "banana"}
    print(f"set comprehension: {new_set}\n")

    a = {1, 2, 3, 5}
    b = {2, 3, 4}
    print(f"difference (elements in {a} that are not in {b}): {a - b}")
    print(f"intersection (elements in both {a} and {b}): {a & b}")
    print(f"union (elements in {a} or {b}): {a | b}")
    print(f"symmetric difference (elements in {a} or {b}, but not in both): {a ^ b}\n")

    print(f"{a} is subset of {b}: {a <= b}\n")

    # Iterate over a set
    print(f"items in my_set:")
    for item in my_set:
        print(item)

main()