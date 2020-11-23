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

def get_sum(factors):
  sum = 0
  for factor in factors:
    sum = sum + factor

  return sum

def print_friend_numbers_in_range(start, end):
  serie = range(start, end)
  for a in serie:
    a_factors = compute_factors(a)
    sum1 = get_sum(a_factors)# Sum of the factors of a number
    for b in serie:
      b_factors = compute_factors(b)
      sum2 = get_sum(b_factors) # Sum of the factors of b number

      is_a_friend_number = sum1 == b and sum2 == a
      if is_a_friend_number:
        print(f"Friends: a: {a}, b: {b}")

n = 3
start, end = 10**(n-1), 10**n
print_friend_numbers_in_range(start, end)

