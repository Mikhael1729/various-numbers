from time import time

def compute_divisors(number):
  divisors = []

  start_point = number // 2 + 1
  for n in range(start_point - 1, 0, -1):
    is_divisible = number % n == 0
    # print(f"n: {n}")
    if is_divisible == True:
      print(f"is_divisible: {n}")
      divisors.append(n)

  return divisors

def compute_factors(number):
  return []

def compute_sum(factors):
  sum = 0
  for factor in factors:
    sum = sum + factor

  return sum

def compute_factors_sum(number):
  factors = compute_factors(number)
  factors_sum = compute_sum(factors)

  return factors_sum

def is_perfect_number(number, factors_sum):
  return True if factors_sum == number else False

def compute_amicability(a, a_factors_sum, b, b_factors_sum):
  return a_factors_sum == b and b_factors_sum == a

def print_friend_numbers_in_range(start, end):
  amicable_numbers = []
  perfect_numbers = []
  sociable_numbers = {}
  

  serie = list(range(start, end))
  size = len(serie)

  period_size = 3
  for i in range(0, len(size)):
    a = serie[i]
    a_factors_sum = compute_factors_sum(a)# Sum of the factors of a number

    # Perfect number evaluation.
    a_is_perfect_number = is_perfect_number(a, a_factors_sum)
    if a_is_perfect_number:
      perfect_numbers.append(a)
      del serie[i]
      continue

    for j in range(0, len(size)):
      b = serie[j]
      b_factors_sum = compute_factors_sum(b) # Sum of the factors of b number

      are_amicable = compute_amicability(a, a_factors_sum, b, b_factors_sum)
      if are_amicable:
        amicable_numbers.append(a)
        amicable_numbers.append(b)
      elif a_factors_sum == b and b_factors_sum is not a: # It's a candidate number of a sociable secuence of period n = 3
	if period_size in sociable_numbers:
	  sociable_numbers[period_size].append(a)
	  sociable_numbers[period_size].append(b)
	else:
	  sociable_numbers[period_size] = []
      
      # TODO: Check where the following instructions are not true for the rest of cases.
      del serie[i]
      del serie[j]
      continue

"""
- Amicable numbers
- Perfect numbers
- Other sociable numbers of n + 2 periods

A = [a, b], # Amicable numbers
P = [], # Perfect numbers
S = [[3], [4], [5], [n]]


P = [1, 2, 3, 4, 5, 6, 7, 8, 9]

1. Tomo el primero número 
2. 
2. Empi
"""

n = 3
start, end = 10**(n-1), 10**n
print_friend_numbers_in_range(start, end)

