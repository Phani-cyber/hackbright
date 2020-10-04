"""SKILLS: LISTS

Complete the following functions.
"""


def print_indices(items):
    """Print each item in the list, followed by its index.

    Do this without using a "counting variable" --- in other words,
    DON'T do this:

        >>> count = 0
        >>> for item in list:
        ...     print(count)
        ...     count = count + 1
        ...

    The output should look like this:

        >>> print_indices(['apple', 'berry', 'cherry'])
        apple 0
        berry 1
        cherry 2
    """
    for i, item in enumerate(items):
        print(f'{item} {i}')

print_indices(['apple', 'berry', 'cherry'])   


def words_in_common(words1, words2):
    duplicates = []
    for items in words1:
        if items in words2:
            if(items not in duplicates):
                duplicates.append(items)
    
    return (sorted(duplicates))
    """

    The returned words are sorted alphabetically.

    NOTE: For this problem, feel free to use other data structures we've
    learned about in this class.

    For example:

        >>> words_in_common(
        ...     ['Python', 'Python', 'Python'],
        ...     ['Lizard', 'Turtle', 'Python']
        ... )
        ['Python']

    The returned list should not have any duplicates:

        >>> words_in_common(
        ...     ['cheese', 'cheese', 'cheese', 'cake'],
        ...     ['cheese', 'hummus', 'beets', 'cake']
        ... )
        ['cake', 'cheese']

    If there are no words in common, return an empty list:

        >>> words_in_common(
        ...     ['lamb', 'chili', 'cheese'],
        ...     ['cake', 'ice cream']
        ... )
        []
    """

word1 = ['Python', 'Python', 'Python']
word2 = ['Lizard', 'Turtle', 'Python']
words_in_common(word1, word2)

word1 = ['cheese', 'cheese', 'cheese', 'cake']
word2 = ['cheese', 'hummus', 'beets', 'cake']
words_in_common(word1, word2)

word1 = ['lamb', 'chili', 'cheese'],
word2 = ['cake', 'ice cream']
words_in_common(word1, word2)


# items1 = ['cheese', 'cheese', 'cheese', 'cake'] 
# items2 = ['cheese', 'humus', 'beets', 'cake']


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example:

       >>> every_other_item(['a', 400, True, 'b', 0])
       ['a', True, 0]
    """
    list_output = items[::2]
    return list_output

a_list = ['a', 400, True, 'b', 0]
print(every_other_item(a_list))


def smallest_n_items(items, n):
    """Return the `n` smallest integers in list in descending order.

    You can assume that `n` will be less than the length of the list.

    For example:

        >>> smallest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [42, 6, 2]

    If `n` is 0, return an empty list:

        >>> smallest_n_items([3, 4, 5], 0)
        []

    Duplicates are OK:

        >>> smallest_n_items([1, 1, 1, 1, 1, 1], 2)
        [1, 1]
    """
    sorted_data = sorted(items)
    answer = sorted_data[0:n:1]
    return (answer[::-1])

print(smallest_n_items([1, 1, 1, 1, 1, 1], 2))
print(smallest_n_items([3, 4, 5], 0))
print(smallest_n_items([2, 6006, 700, 42, 6, 59], 3))

#items = ['apple', 'berry', 'cherry']
#print_indices(items)















