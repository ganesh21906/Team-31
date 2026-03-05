# Example 04 – Loops
# Use loops to repeat actions.

# --- for loop ---
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# --- while loop ---
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Go!")

# --- looping over a list ---
fruits = ["apple", "banana", "cherry"]
print("\nFruits:")
for fruit in fruits:
    print("-", fruit)
