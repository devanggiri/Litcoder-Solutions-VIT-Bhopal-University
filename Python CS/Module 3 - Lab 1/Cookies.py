def min_steps_to_target_sweetness(target, candies):
    candies.sort()  # Sort the candies in ascending order
    steps = 0

    while candies[0] < target:
        # Combine the two least sweet candies
        new_candy = candies[0] + 2 * candies[1]

        # Remove the two least sweet candies and add the new candy
        candies = [new_candy] + candies[2:]

        steps += 1

    return steps

# Exercise-1
target_1 = 7
candies_1 = [1, 2, 3, 4, 5]
output_1 = min_steps_to_target_sweetness(target_1, candies_1)
print(output_1)

# Exercise-2
target_2 = 11
candies_2 = [2, 5, 3, 7, 6, 1]
output_2 = min_steps_to_target_sweetness(target_2, candies_2)
print(output_2)
