import sys


def main():
    lines = sys.stdin.read().splitlines()

    if not lines:
        return

    n = int(lines[0])
    dates = lines[1:n + 1]

    # 先按 day 排序
    dates.sort(key=lambda date: int(date[0:2]))

    # 再按 month 排序
    dates.sort(key=lambda date: int(date[3:5]))

    # 最后按 year 排序
    dates.sort(key=lambda date: int(date[6:10]))

    sys.stdout.write('\n'.join(dates))


if __name__ == '__main__':
    main()