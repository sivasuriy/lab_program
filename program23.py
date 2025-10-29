# Activity Selection Problem using Greedy Algorithm

def activity_selection(start, finish):
    n = len(finish)

    # Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = [activities[0]]  # Always select first activity

    # Select subsequent activities
    for i in range(1, n):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])

    return selected


# ----- MAIN PROGRAM -----
print("Activity Selection Problem using Greedy Algorithm\n")

n = int(input("Enter number of activities: "))

start = list(map(int, input("Enter start times : ").split()))
finish = list(map(int, input("Enter finish times: ").split()))

selected = activity_selection(start, finish)

print("\nSelected activities:")
for s, f in selected:
    print(f"Start: {s}, Finish: {f}")
