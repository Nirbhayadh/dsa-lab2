from random import sample
from sort import mergesort, insertionsort
from time import time_ns


# def run(n):
#     data = [i for i in range(n, 0, -1)]
#     # data = [i for i in range(0, n, 1)]
#     start_time = time_ns()
#     output = insertionsort(data)
#     end_time = time_ns()
#     time_taken = end_time - start_time
#     return time_taken

# if __name__ == "__main__":
#     # for i in range(10000000, 100000001, 10000000):
#     #     print(f"Number of sample data: {i}, Time Taken: {run(i)} nanosecond")
#     for i in range(1000, 10001, 1000):
#         print(run(i))

def run(n):
    data = [i for i in range(n, 0, -1)]
    start_time = time_ns()
    output = mergesort(data, 0, len(data)-1)
    end_time = time_ns()
    time_taken = end_time - start_time
    return time_taken


if __name__ == "__main__":
    for i in range(10000, 100001, 10000):
        print(f"Number of sample data: {i}, Time Taken: {run(i)} nanosecond")
