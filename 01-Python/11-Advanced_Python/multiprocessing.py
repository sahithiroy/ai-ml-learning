"""Day 23: Multiprocessing

Topics:
- Process
- Pool
- CPU-bound tasks

Multiprocessing is useful for CPU-bound work because it runs separate processes
on multiple cores instead of sharing the same GIL like threads.
"""

import math
import os
import sys
import sysconfig

stdlib_path = sysconfig.get_paths()["stdlib"]
sys.path = [p for p in sys.path if p not in ("", os.getcwd())]
sys.path.insert(0, stdlib_path)

import multiprocessing as mp


# 1. Process
print("Example 1: Process")

def worker():
    print("Worker process running")


if __name__ == "__main__":
    p = mp.Process(target=worker)
    p.start()
    p.join()
print()


# 2. Pool
print("Example 2: Pool")

def square(n):
    return n * n


if __name__ == "__main__":
    with mp.Pool(processes=3) as pool:
        result = pool.map(square, [1, 2, 3, 4])
    print("Squares:", result)
print()


# 3. CPU-bound tasks
print("Example 3: CPU-bound tasks")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(limit):
    return sum(1 for n in range(2, limit + 1) if is_prime(n))


if __name__ == "__main__":
    print("Prime count up to 100:", count_primes(100))
print()


# Practice 1: Parallel image processing
print("Practice 1: Parallel image processing")

def brighten_pixel(pixel_value):
    return min(255, pixel_value + 50)


if __name__ == "__main__":
    pixels = [10, 20, 30, 40, 50]
    with mp.Pool(processes=2) as pool:
        bright_pixels = pool.map(brighten_pixel, pixels)
    print("Brightened pixels:", bright_pixels)
print()


# Practice 2: Projects
print("Practice 2: Projects")

def project_score(value):
    return value * 2


if __name__ == "__main__":
    scores = [5, 10, 15]
    with mp.Pool(processes=2) as pool:
        project_scores = pool.map(project_score, scores)
    print("Project scores:", project_scores)
print()


# Practice 3: Image processing
print("Practice 3: Image processing")

def grayscale(value):
    return value // 2


if __name__ == "__main__":
    values = [100, 150, 200]
    with mp.Pool(processes=2) as pool:
        grayscale_values = pool.map(grayscale, values)
    print("Grayscale values:", grayscale_values)
print()


# Practice 4: Prime number generator
print("Practice 4: Prime number generator")

def generate_primes(limit):
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    return primes


if __name__ == "__main__":
    with mp.Pool(processes=2) as pool:
        prime_chunks = pool.map(generate_primes, [10, 20, 30])
    print("Prime chunks:", prime_chunks)
print()


# Practice 5: Matrix multiplication
print("Practice 5: Matrix multiplication")

def multiply_row(row):
    return [value * 2 for value in row]


if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    with mp.Pool(processes=2) as pool:
        doubled_matrix = pool.map(multiply_row, matrix)
    print("Doubled matrix:", doubled_matrix)
