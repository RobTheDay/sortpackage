#sortpackage
This library has two separate modules within it; recursion.py and sorting.py.

recursion.py contains functions that use recursion to solve basic problems.
The following functions can be found within recursion.py:
  1) sum_array(array) - returns the sum of all elements in an array
  2) fibonacci(n) - calculates the nth term in a fibonacci sequence
  3) factorial(n) - calculates n factorial (n!)
  4) reverse(word) - returns a word in reverse order

sorting.py contains functions that sort an array using distinct sorting algorithms.
The following functions can be found within sorting.py:
  1) bubble_sort(items) - uses the bubble sort algorithm to return an array
     ordered in ascending order
  1) merge_sort(items) - uses the merge sort algorithm to return an array
     ordered in ascending order
  1) quick_sort(items) - uses the quick sort algorithm to return an array
     ordered in ascending order

## Building this package locally
`python setup.py sdist`

## Installing this package from GitHub
`pip install git+https://github.com/RobTheDay/sortpackage.git`

## Updating this package from GitHub
`pip install --upgrade git+https://github.com/RobTheDay/sortpackage.git`

## License
[MIT](https://choosealicense.com/licenses/mit/)
