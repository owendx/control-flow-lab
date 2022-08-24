# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
humanYears = int(input("Input a dog's age in human years: "))

# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
if humanYears <= 2:
    dogYears = humanYears * 10
else:
    dogYears = (2 * 10) + ((humanYears - 2) * 7)

# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
print(f"The dog's age in dog years is {dogYears}")

# Hint:  Use the int() function to convert the string returned from input() into an integer