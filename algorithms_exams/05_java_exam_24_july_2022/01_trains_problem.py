# https://judge.softuni.org/Contests/Practice/Index/3563#0

from collections import deque

arrival_times = deque(sorted(float(x) for x in input().split()))
departure_times = deque(sorted([float(x) for x in input().split()]))

total_trains = 0
max_trains = 0
while arrival_times and departure_times:
    current_arrival_time = arrival_times.popleft()
    current_departure_time = departure_times.popleft()

    if current_arrival_time < current_departure_time:
        departure_times.appendleft(current_departure_time)
        total_trains += 1
    else:
        arrival_times.appendleft(current_arrival_time)
        total_trains -= 1

    max_trains = max(max_trains, total_trains)

print(max_trains)
