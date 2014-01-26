"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

# 6 digits at most, 999 * 999 = 998,001

def is_palindrome(n):
	string_version = str(n)
	return string_version[:] == string_version[::-1]

def finder():
	max_palindrome = 0
	for x in range(100, 999):
		for y in range(100, 999):
			z = x * y
			if (is_palindrome(z)) and (z > max_palindrome):
				max_palindrome = z
	return max_palindrome

print(finder())
