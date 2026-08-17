import sys


def main():
    lines = sys.stdin.read().splitlines()

    if not lines:
        return

    n = int(lines[0])
    dates = lines[1:n + 1]

    # Sort by day first using stable sorting.
    dates.sort(key=lambda date: int(date[0:2]))

    # Then sort by month.
    dates.sort(key=lambda date: int(date[3:5]))

    # Finally sort by year, the most significant date component.
    dates.sort(key=lambda date: int(date[6:10]))

    sys.stdout.write('\n'.join(dates))


if __name__ == '__main__':
    main()
