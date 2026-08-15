import sys


def solve():
    # Read all input from standard input
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return

    n = int(raw_data[0])

    rooms = []
    total_students = 0
    idx = 1

    # Read room positions and student counts
    for _ in range(n):
        pos = int(raw_data[idx])
        students = int(raw_data[idx + 1])
        rooms.append((pos, students))
        total_students += students
        idx += 2

    # Sort rooms by their positions on the walkway
    rooms.sort(key=lambda item: item[0])

    # Target weight threshold for the weighted median
    target = (total_students + 1) // 2

    current_weight = 0
    best_p = 0

    # Find the first room where cumulative student count reaches target
    for pos, students in rooms:
        current_weight += students
        if current_weight >= target:
            best_p = pos
            break

    # Calculate total distance to best_p
    total_distance = 0
    for pos, students in rooms:
        dist = abs(pos - best_p)
        total_distance += students * dist

    print(f"{best_p} {total_distance}")


if __name__ == '__main__':
    solve()