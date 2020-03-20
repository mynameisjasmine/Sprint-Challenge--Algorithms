#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0   <----- O(1) this is a constant 
    while (a < n * n * n): <----- O(1) this is a constant 
      a = a + n * n <----- O(1) this is a constant 
  The runtime is constant

b) sum = 0  <----- O(1) this is a constant 
    for i in range(n):  <----- O(n)  
      j = 1  <----- O(1) this is a constant 
      while j < n: <----- O(n) 
        j *= 2  <----- O(1) this is a constant 
        sum += 1 <----- O(1) this is a constant 
  The runtime is O(n)
      

c) def bunnyEars(bunnies):
      if bunnies == 0: <----- O(n) 
        return 0

      return 2 + bunnyEars(bunnies-1)
    The runtime is O(log(n))

## Exercise II


def egg_drop(n):
    if n <= 7:
      return print(f"You the egg! It was dropped from floor {n}")

    else
