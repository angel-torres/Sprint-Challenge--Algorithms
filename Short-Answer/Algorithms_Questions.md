# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n): O(n*n*n)
      a = a + n * n 
```


```
b)  sum = 0
    for i in range(n): # O(n)
      j = 1
      while j < n: # O(n)
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) # O(n)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


** ANSWER **

	For this problem I would do a binary search. This means I would split the number of floors in half and frop the egg from the middle floor. If the egg breaks, it means f is lower so I wold split the bottom floors in half and drop from the middle floor of the bottom floors. If the egg doesn't break then it means that f is higher. I will continue this process until I find floor f. 

1. Find middle floor
2. Drop egg to see if it breaks
3.1 If it doesn't break, find the middle floor of top half
3.2 If it breaks then find the middle floor of bottom half
4. Drop egg from whichever half got selected
5. Repeat process until f is found

The runtime complexity would be log(n) because everytime the floors are split in half therefore reducing the times the process by half each time. 
