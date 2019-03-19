def sum_array(array):
    '''
    Return sum of all elements in an array

    Args:
        array (list): elements of array should be int or float type,
            function will fail if elements are of str type.

    Returns:
        int: sum of all elements in the list,
            uses recursive addition to calculate sum of elements

    Examples:
        >>> sum_array([1,2])
        3
        >> sum_array([1,2,3])
        6
        >> sum_array([1,2,3,4,5,6,7,8,9,10])
        55
    '''

    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    '''
    Calculates the nth term in a fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    '''

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    '''
    Calculates n factorial (n!)
    n! is the number n * (n-1) * (n-1-1) * (n-1-1-1) ...* 2 * 1

    Args:
        n (int): the number that should be taken as the factorial

    Returns:
        int: the product of the n!

    Examples:
        >>> factorial(1)
        1
        >> factorial(3)
        6
        >> factorial(10)
        3628800
    '''

    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):
    '''
    Returns word in reverse order

    Args:
        word (str): the word/string that is to be reversed,
            function will fail if word is of int or float type

    Returns:
        str: word in reverse order,
            all unique cases will be maintained through reversal

    Examples:
        >>> reverse('Yeah')
        'haeY'
        >> factorial('swallow')
        'wollaws'
        >> factorial('Whats the story, Ballimore?')
        '?eromillaB ,yrots eht stahW'
    '''

    if len(word)==0:
        return ''
    else:
        return word[-1] + reverse(word[:-1])
