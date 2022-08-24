# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
fibonacci = [0, 1]
for i in range(50):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
for i in range(len(fibonacci)-1):
    print(f"term: {i} / number: {fibonacci[i]}")

# Hint: The next number is found by adding the two numbers before it
