# CITS3001 Algorithms

This repository contains Python algorithm exercises for CITS3001, including weekly coursework, lab problems, and a collection of LeetCode Hot 150 solutions.

The code is intended to practise algorithmic thinking, complexity analysis, and competitive-programming input/output patterns. Some files represent work in progress, so the implementations are not necessarily the only or final optimal solutions.

## Repository Structure

```text
.
+-- lab01/                  # Lab 01: standard input/output problems
|   +-- classRank.py        # Median of Medians and k-th smallest element
|   +-- deadlineOrder.py    # Date sorting
|   +-- leaderBoard.py      # Dynamic k-th fastest time tracking
|   +-- rainBucket.py       # Bucket counting
|   +-- waterStation.py     # Weighted median and minimum distance
+-- week1/
|   +-- Week1_1.py          # Basic exercises
|   +-- sort.py             # Merge, bucket, counting, and radix sort
+-- week2/
|   +-- Week2_2.py          # Quicksort and distribution-sort exercises
+-- week3/
|   +-- order_statistics.py # Randomized Quickselect
|   +-- Week3_2.py          # Sorting and selection exercises
+-- week4/
|   +-- Lecture2.py         # BFS, DFS, timing, and Kosaraju's algorithm
+-- week5/
|   +-- lecture1.py         # Bottom-up and top-down coin-change exercises
+-- leetcode_hot150.py      # Ongoing LeetCode Hot 150 solutions
```

## Topics Covered

- Comparison and linear sorting: merge sort, quicksort, bucket sort, counting sort, and radix sort
- Order statistics: Quickselect, randomized partitioning, and Median of Medians
- Graph algorithms: breadth-first search (BFS), depth-first search (DFS), and Kosaraju's algorithm for strongly connected components
- Common LeetCode techniques: two pointers, sliding windows, hash tables, greedy algorithms, dynamic programming, matrix traversal, and interval processing
- Competitive-programming techniques: heaps, weighted medians, standard input/output, and efficient data processing

## Requirements

- Python 3.9 or later
- The project currently uses only the Python standard library and has no third-party dependencies.

You can use the repository's virtual environment or create a new one:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Running the Code

Most files can be run directly. The lab programs with an `if __name__ == '__main__'` entry point read from standard input. For example:

```bash
python lab01/classRank.py < input.txt
python lab01/leaderBoard.py < input.txt
python lab01/rainBucket.py < input.txt
python lab01/waterStation.py < input.txt
```

Sorting, searching, and LeetCode functions can also be imported and tested directly:

```python
from week3.order_statistics import find_kth_smallest

print(find_kth_smallest([14, 3, 9, 1, 22, 8, 5], 3))
```

## Notes

- The `Solutions` class in `leetcode_hot150.py` groups solutions by problem number. Method names generally follow the `leetcode<problem_number>` pattern.
- Programs in `lab01` follow the standard online-judge pattern: they read input from `stdin` and write results to `stdout`.
- Some coursework files retain learning-stage implementations and comments. Tests, complexity notes, and further refinements may be added over time.
