import numpy as np

sample = list(map(list, """
.###..#..###.###.#.#.###.###.###.###.###.
.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.
.#.#..#..###.###.###.###.###...#.###.###.
.#.#..#..#.....#...#...#.#.#...#.#.#...#.
.###.###.###.###...#.###.###...#.###.###.
""".split()))

sample = np.array(sample)
samples = []

for c in range(10):
    samples.append(sample[:, 4*c:4*c+4])

def to_num(num_arr):
    for i, sample in enumerate(samples):
        if (sample == num_arr).all():
            return i

# print('input >>')
N = int(input())
board = []

for _ in range(5):
    board.append(list(input()))

board = np.array(board)

for c in range(N):
    num = board[:, 4*c:4*c+4]
    print(to_num(num), end='')

# print('-----output-----')