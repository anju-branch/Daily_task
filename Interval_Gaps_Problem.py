#Traverse sorted array from left to right.(DSA algorithm)

def find_missing_ranges(arr, lower, upper):
    result = []              # List to store all missing ranges
    prev = lower - 1         # Initialize previous number just before lower bound
    nums = arr + [upper + 1] # Append a virtual number (upper + 1) to handle the last missing range

    # Traverse through each number in the array + virtual number
    for num in nums:
        # Check if there is a gap between prev and current number
        # If difference >= 2, it means there are missing numbers
        if num - prev >= 2:
            # Missing range is from (prev + 1) to (num - 1)
            result.append([prev + 1, num - 1])
        # Update prev to current number for next iteration
        prev = num

    # Return the list of all missing ranges
    return result


#Testing Senario Example1

arr = [14, 15, 20, 30, 31, 45]
lower = 10
upper = 50
print(find_missing_ranges(arr, lower, upper))


