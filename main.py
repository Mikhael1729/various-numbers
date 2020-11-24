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
  factors = []
  if number > 1:
    factors.append(1)

    limit = number // 2 + 1
    divisor = 2

    while divisor < limit: # Curent divisor hasn't been evaluated. Mientras no se ha terminado de evaluar cada número entre number / 2.
      quotient = number // divisor

      divisor_is_divisible_by_number = number == divisor * quotient
      if divisor_is_divisible_by_number:
        factors.append(divisor)

        quotient_hasnt_been_evaluated = divisor < quotient # At this point quotient is a divisible number candidate
        if quotient_hasnt_been_evaluated:
          factors.append(quotient)

        limit = quotient - 1 # Is always divisor + 1

      divisor += 1

  return factors

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

def is_friend_number(a, a_factors_sum, b, b_factors_sum):
  return a_factors_sum == b and b_factors_sum == a

def print_friend_numbers_in_range(start, end):
  amicable_numbers = []
  perfect_numbers = []
  sociable_numbers = []

  serie = list(range(start, end))
  size = len(serie)

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

      is_a_friend_number = is_friend_number(a, a_factors_sum, b, b_factors_sum)
      if is_a_friend_number:
        amicable_numbers.append(a)
        amicable_numbers.append(b)
        del serie[i]
        del serie[j]
        continue
      # TODO: Coninue writing the step 6
      elif:

      
      


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

