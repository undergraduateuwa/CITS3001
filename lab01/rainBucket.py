import sys


def count_raindrops_per_bucket():
    """
    Computes the raindrop count for each bucket using the bucket index formula:
    bucket_index = floor(x * k / L) implemented via integer division (x * k) // L.
    """
    # Read input tokens from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    L = int(input_data[1])
    k = int(input_data[2])

    # Drop positions
    positions = [int(x) for x in input_data[3:3 + n]]

    # Frequency array to store counts for each of the k buckets
    bucket_counts = [0] * k

    # Compute bucket index for each drop and increment the corresponding counter
    for x in positions:
        # Integer arithmetic equivalent to floor(x * k / L)
        bucket_index = (x * k) // L
        bucket_counts[bucket_index] += 1

    # Output the result: count for bucket 0 to bucket k - 1
    for count in bucket_counts:
        print(count)


if __name__ == '__main__':
    count_raindrops_per_bucket()