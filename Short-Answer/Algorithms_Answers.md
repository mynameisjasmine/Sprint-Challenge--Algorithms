#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0   <----- O(1) this is a constant 
    while (a < n * n * n): <----- O(n) 
      a = a + n * n <----- O(1) this is a constant 
  The runtime is O(n)

b) sum = 0  <----- O(1) this is a constant 
    for i in range(n):  <----- O(n)  
      j = 1  <----- O(1) this is a constant 
      while j < n: <----- O(log(n)) 
        j *= 2  
        sum += 1  
  The runtime is O(nlog(n))
      

c) def bunnyEars(bunnies):
      if bunnies == 0: 
        return 0

      return 2 + bunnyEars(bunnies-1) <----- O(n) 
    The runtime is O(n)

## Exercise II


def egg_drop(n):

I would iterate through n using in range()
divide the array .
have a left half and a right half
use a binary search 
check to see at which floor the eggs get broken
run time is O(log(n))
    
<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution. -->