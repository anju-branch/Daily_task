def can_attend_meetings(intervals):
    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Check for overlaps
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False   # overlap found

    return True   # no overlap

# Example usage given in question
intervals = [[0, 30], [5, 10], [15, 20]]
print(can_attend_meetings(intervals))

intervals = [[7, 10], [2, 4]]
print(can_attend_meetings(intervals))

intervals = [[9, 10], [10, 11], [11, 12]]
print(can_attend_meetings(intervals))

intervals = [[1, 5], [6, 8], [7, 10]]
print(can_attend_meetings(intervals))
