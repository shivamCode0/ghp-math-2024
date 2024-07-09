import numpy as np
import math
import itertools as it
from collections import Counter
from collections import defaultdict
from tqdm import tqdm, trange
import concurrent.futures


def randbool(invchance):
    return np.random.random() < (1 / invchance)


def simulate(t):
    r = 1
    c = 0
    for i in range(t):
        c += 1 if randbool(r + 1) else -1
        r += 1
    return c > 0


def worker(chunk_size):
    wins = 0
    for _ in trange(chunk_size):
        if simulate(15):
            wins += 1
    return wins


def main():
    runs = int(1e8)
    num_workers = 8
    chunk_size = runs // num_workers

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(worker, chunk_size) for _ in range(num_workers)]
        wins = sum(f.result() for f in concurrent.futures.as_completed(futures))

    print(f"{wins=}, {runs=}")
    print(f"{wins=}, {runs=}, {wins/runs=}, {runs/wins=}")


if __name__ == "__main__":
    main()
