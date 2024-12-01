from typing import List
import os
import sys
from collections import Counter

cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
INPUT = f'{cwd}/01_input.txt'

def insert_sorted(llist: List[int], num: int):
    """Insert num into the sorted list llist."""
    llist.append(num)
    llist.sort()

def solve_p1():
    left = []
    right = []

    with open(INPUT, 'r') as f:
        for line in f:
            line = line.strip()
            nums = line.split()
            num_0 = int(nums[0])
            num_1 = int(nums[1])
            # part 1
            insert_sorted(left, num_0)
            insert_sorted(right, num_1)
    
    assert len(left) == len(right), "List length should be the same!"

    # part 1: calculate distance
    dist = sum(abs(l - r) for l, r in zip(left, right))

    # part 2: calculate similarity score
    right_counter = Counter(right)
    similarity = sum(num * right_counter[num] for num in left)

    return dist, similarity

if __name__ == "__main__":
    d, s = solve_p1()
    print(f"Distance: {d}")
    print(f"Similarity score: {s}")

# others: https://www.reddit.com/r/adventofcode/comments/1h3vp6n/2024_day_1_solutions/

"""
def aoc01():
    L = list(zip(*[map(int, line.split()) for line in open("input01.txt")]))
    print(sum(abs(a-b) for (a,b) in zip(*map(sorted, L))))
    print(sum(x*L[1].count(x) for x in L[0]))
"""