"""
This is a problem from Algorithms with Java course.
Python to Java converter used for testing the code in judge system
"""

def monkey_job(vect, idx, solution):
    if idx == len(vect):
        if sum(solution) == 0:
            print(*["+" + str(solution[i]) if solution[i] > 0 else str(solution[i]) for i in range(len(solution))])
            return 1
        return 0

    counter = 0
    solution[idx] = vect[idx]
    counter += monkey_job(vect, idx + 1, solution)

    solution[idx] = -vect[idx]
    counter += monkey_job(vect, idx + 1, solution)

    return counter


# This code do not pass some judge tests, because the ordering output
# def monkey_job(vect, idx, limit):
#     if idx == limit:
#         # print(*["+" + str(vect[i]) if vect[i] > 0 else str(vect[i]) for i in range(len(vect))])
#
#         if sum(vect) == 0:
#             print(*["+" + str(vect[i]) if vect[i] > 0 else str(vect[i]) for i in range(len(vect))])
#             return 1
#         return 0
#     count = 0
#     for sign in [1, -1]:
#         vect[idx] *= sign
#         count += monkey_job(vect, idx + 1, limit)
#     return count

n = int(input())
numbers = [x for x in range(1, n + 1)]
solution = [0] * n
total_solutions = monkey_job(vect=numbers, idx=0, solution=solution)
print(f"Total Solutions: {total_solutions}")
