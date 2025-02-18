from collections import namedtuple
from copy import deepcopy

def main():
    # Empty list
    empty = []

    # Non-empty list
    # Lists are dynamic + mutable by default
    my_list = [1, 2, 3, 4, 5]
    print(f"list: {my_list}\n")

    # Heterogeneous list
    heterogeneous_list = [1, "cat", 0.5, True]
    print(f"heterogeneous list: {heterogeneous_list}\n")

    # Filled array
    zeros = [0] * 5
    print(f"zeros: {zeros}\n")

    # List comprehension
    result = [val ** 2 for val in my_list]
    print(f"all values in {my_list} squared: {result}\n")

    # Access
    value = my_list[0]
    print(f"value at 0 in {my_list}: {value}\n")

    # Length
    length = len(my_list)
    print(f"length of {my_list}: {length}\n")

    # Prepend (insert 1 at index 0)
    my_list.insert(0, 1)
    print("my_list.insert(0, 1)")
    print(f"list: {my_list}\n")

    # Append
    my_list.append(6)
    print("my_list.append(6)")
    print(f"list: {my_list}\n")

    # Insert at index (insert 2 at index 2)
    my_list.insert(2, 2)
    print("my_list.insert(2, 2)")
    print(f"list: {my_list}\n")

    # Pop last
    last = my_list.pop()
    print("my_list.pop()")
    print(f"last element: {last}")
    print(f"list: {my_list}\n")

    # Remove at index
    removed = my_list.pop(2)
    print("my_list.pop(2)")
    print(f"removed element: {removed}")
    print(f"list: {my_list}\n")

    # Remove at index using del statement
    del my_list[0]
    print("del my_list[0]")
    print(f"my_list: {my_list}\n")

    # Bulk append to list
    my_list += [6, 7, 8]
    print("my_list += [6, 7, 8]")
    print(f"my_list: {my_list}\n")

    # Delete slice from list
    del my_list[5:8]
    print("del my_list[5:8]")
    print(f"list {my_list}\n")

    # Shallow copy
    shallow_copy = [val for val in my_list]
    print(f"shallow copy: {shallow_copy}\n")
    # Alternative: shallow_copy = my_list[:]

    # Deep copy
    deep_copy = deepcopy(my_list)
    print(f"deep copy: {deep_copy}\n")

    # Merge
    merged = my_list + [6, 7, 8]
    print(f"{my_list} merged with {[6, 7, 8]}: {merged}\n")
    # Altnerative (use unpacking): merged = [*my_list, *[6, 7, 8]]

    # Map using list comprehension
    mapped = [val * 2 + index for index, val in enumerate(my_list)]
    print(f"mapped list (each value multiplied by 2 + index): {mapped}\n")

    # Filter using list comprehension
    filtered = [val for val in my_list if val % 2 == 0]
    print(f"filtered list (keep only even numbers): {filtered}\n")

    # Find 
    found = 5 in my_list
    print(f"found 5 in {my_list}: {found}\n")

    # Find index
    target_index = my_list.index(5) # Throws ValueError if value is not in list
    print(f"index of 5 in {my_list}: {target_index}\n")

    # Sort in place
    my_list.sort()

    # Return sorted list
    sorted_list = sorted(my_list)
    print(f"sorted list: {sorted_list}\n")

    # Sort list with complex objects
    people = [("Tom", 24), ("Jane", 22), ("John", 42)]
    print(f"people: {people}")
    sorted_people = sorted(people, key = lambda person: person[1])
    print(f"sorted people: {sorted_people}\n")

    # Move k indices from start index.
    # If k is < 0, move left. Otherwise, move right
    def hop(start, k, arr):
        if k == 0:
            return start

        if k < 0: # move backwards (left)
            k = abs(k)
            if start - k >= 0:
                return start - k
            else:
                return len(arr) - (abs(start - k) % len(arr))
        
        # k > 0, move forwards (right)
        return (start + k) % len(arr)

    print("hop(1, 12, my_list)")
    print(f"index: {hop(1, 12, my_list)}\n")

    print("hop(4, 0, my_list)")
    print(f"index: {hop(4, 0, my_list)}\n")

    print("hop(1, -8, my_list)")
    print(f"index: {hop(1, -8, my_list)}\n")

    print("hop(3, -3, my_list)")
    print(f"index: {hop(3, -3, my_list)}\n")

    # All pairs
    pairs = []
    for i in range(0, len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            pairs.append([my_list[i], my_list[j]])
    print(f"all pairs in {my_list}: {pairs}\n")

    # All triplets
    triplets = []
    for i in range(0, len(my_list) - 2):
        for j in range(i + 1, len(my_list) - 1):
            for k in range(j + 1, len(my_list)):
                triplets.append([my_list[i], my_list[j], my_list[k]])
    print(f"all triplets in {my_list}: {triplets}\n")

    # Subsequences with length k
    k = 4
    result = []

    def subsequences(index, k, subsequence):
        if len(subsequence) == k:
            result.append([*subsequence])
            return

        if index == len(my_list):
            return

        # Include elem at index
        subsequence.append(my_list[index])
        subsequences(index + 1, k, subsequence)

        # Exclude elem at index
        subsequence.pop()
        subsequences(index + 1, k, subsequence)

    subsequences(0, k, [])
    print(f"all subsquences in {my_list} with length {k}: {result}\n")

    # Tuples
    # tuple vs list in python:
    # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

    # Empty tuple
    empty = ()
    print(f"Empty tuple: {empty}\n")

    # Singleton tuple
    singleton = (1,)
    print(f"Singleton tuple: {singleton}\n")

    # Heterogenous tuple
    my_tup = (0, 1365, "hello!")
    print(f"Heterogeneous tuple: {my_tup}\n")

    # Nested tuple
    nested_tup = my_tup, (1, 2, 3, 4)
    print(f"Nested tuple: {nested_tup}\n")

    # Unpacking a tuple
    person_tup = ("John", 24)
    name, age = person_tup
    print(f"{person_tup} unpacked: {name}, {age}\n")

    # Named Tuples
    Person = namedtuple("Person", ["name", "age"])
    john = Person(name = "John", age = 24) # name is accessible via john[0] or john.name
    jane = Person(name = "Jane", age = 22) 

    print(f"Hi, my name is {john.name} and I'm {john.age} years old!\n")
    print(f"Hi, my name is {jane.name} and I'm {jane.age} years old!")

if __name__ == "__main__":
    main()




