"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum."""

def square(x):
	return x * x

sum_of_squares = sum(map(square, range(1, 101)))
square_of_sum =  square(sum(range(1, 101)))
print(square_of_sum - sum_of_squares)
