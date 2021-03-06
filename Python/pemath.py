import math
import operator
import itertools

# Given a value N, this class precalculates all the prime numbers
# up to N and keeps a boolean table for quick lookup of if a number is prime or not.
class PrimeNumbers:
	def __init__(self,N):
		self.limit = N
		self._precalc_primes(N)

	def _precalc_primes(self,N):
		self.sieve = [True]*(N+1)
		for d in range(2,int(N**0.5+1)):
			if self.sieve[d]:
				for i in range(2*d,N+1,d):
					self.sieve[i] = False
		self.primes = [i for i in range(2,N+1) if self.sieve[i]]

	def is_prime(self,n):
		if n > self.limit:
			raise IndexError
		return self.sieve[n]

	def get_primes(self):
		return iter(self.primes)

	def get_first_primes(self,n):
		return self.primes[:n]

	def get_nth_prime(self,n):
		return self.primes[n]

class Factorials:
	def __init__(self,up_to=None,n=None):	
		if up_to != None:
			self.factorials = [1]
			x = 1
			while(self.factorials[-1]*x <= up_to):
				self.factorials.append(self.factorials[-1]*x)
				x+=1
		elif n != None:
			self.factorials = [1]
			for x in range(1,n+1):
				self.factorials.append(self.factorials[-1]*x)
		else:
			raise ValueError	

	def get_factorials(self):
		return self.factorials
	def get_nth_factorial(self,n):
		return self.factorials[n]
	def comb(self,n,k):
		return self.factorials[n]/(self.factorials[k]*self.factorials[n-k])

# Returns the greatest common divisor of the numbers a and b
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

# Return the lowest common multiple of the numbers a and b
def lcm(a,b):
	return (a*b)/gcd(a,b)

# Returns a list of the digits of the number in reverse order
def get_digits(nr):
	digits = []
	while nr != 0:
		digits.append(nr%10)
		nr/=10
	return digits

# Returns the sum of the digits of a number
def digit_sum(n):
	return reduce(operator.add,(c for c in get_digits(n)))

def is_binary_palindrome(x) :
	s = bin(x)[2:]
	if len(s) % 2:
		return s[:len(s)/2][::-1] == s[len(s)/2+1:]
	else:
		return s[:len(s)/2][::-1] == s[len(s)/2:]

def is_palindrome(x) :
	s = str(x)
	if len(s) % 2:
		return s[:len(s)/2][::-1] == s[len(s)/2+1:]
	else:
		return s[:len(s)/2][::-1] == s[len(s)/2:]

def triangle_numbers():
	for i in itertools.count(1):
		yield i*(i+1)/2

def is_triangle(t):
    n = ((1 + 4*2*t)**0.5 - 1) / 2
    return n == int(n)

# Iterative prime test.
# If the limit in which the numbers to be checked is known and it is within 
# reasonable bounds (< 10^7), then the PrimeNumbers class is to be used
def is_prime(n):
	    '''check if integer n is a prime'''
	    # make sure n is a positive integer
	    n = abs(int(n))
	    # 0 and 1 are not primes
	    if n < 2:
	        return False
	    # 2 is the only even prime number
	    if n == 2: 
	        return True    
	    # all other even numbers are not primes
	    if not n & 1: 
	        return False
	    # range starts with 3 and only needs to go up the squareroot of n
	    # for all odd numbers
	    for x in range(3, int(n**0.5)+1, 2):
	        if n % x == 0:
	            return False
	    return True

# Returns a list of the prime factors of a number, each element of the list
# being a pair of the form (factor,power)
def get_prime_factors(n):
	d = 2
	factors = []
	while n != 1:
		if n%d == 0:
			k = 0
			while n%d == 0:
				n /= d;
				k+=1
			factors.append((d,k))
		d += 1
	return factors


def is_pandigital(nr):
	nr = str(nr)
	found = set()
	for n in nr:
		if n == '0':
			return False
		if int(n) in found:
			return False
		else:
			found.add(int(n))
	return True

def reverse_number(n):
	digits = get_digits(n)
	result = 0
	for d in digits:
		result = result*10 + d
	return result

def pentagonal_numbers():
	for i in itertools.count(1):
		yield i*(3*i-1)/2

def is_pentagonal(x):
	n = ((24*x +1)**0.5 + 1)/6
	return n == int(n)

def hexagonal_numbers():
	for i in itertools.count(1):
		yield i*(2*i - 1)