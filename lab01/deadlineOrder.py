import sys


# Read input and print the requested result.
def main():
    lines = sys.stdin.read().splitlines()

    if not lines:
        return

    n = int(lines[0])
    dates = lines[1:n + 1]

    # 鍏堟寜 day 鎺掑簭
    dates.sort(key=lambda date: int(date[0:2]))

    # 鍐嶆寜 month 鎺掑簭
    dates.sort(key=lambda date: int(date[3:5]))

    # 鏈€鍚庢寜 year 鎺掑簭
    dates.sort(key=lambda date: int(date[6:10]))

    sys.stdout.write('\n'.join(dates))


if __name__ == '__main__':
    main()
