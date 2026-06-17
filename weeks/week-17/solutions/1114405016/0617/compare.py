from timing import timeit
from search import linear_search, binary_search
import random


@timeit(repeat=10)
def bench_linear(data, target):
    return linear_search(data, target)


@timeit(repeat=10)
def bench_binary(data, target):
    return binary_search(data, target)


n = 100000
data = list(range(n))
target = n - 1

bench_linear(data, target)
bench_binary(data, target)

print(f"n = {n}")
print(f"linear_search: avg = {bench_linear.last_elapsed:.6f}s, records = {bench_linear.records}")
print(f"binary_search: avg = {bench_binary.last_elapsed:.6f}s, records = {bench_binary.records}")
ratio = bench_linear.last_elapsed / bench_binary.last_elapsed
print(f"linear / binary = {ratio:.2f}x")
