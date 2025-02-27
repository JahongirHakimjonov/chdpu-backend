import multiprocessing
import time


def compute_range(start, end):
    for i in range(start, end):
        _ = i * 2


if __name__ == "__main__":
    start_time = time.time()

    cpu_count = multiprocessing.cpu_count()
    chunk_size = 1_000_000 // cpu_count
    processes = []

    for i in range(cpu_count):
        p = multiprocessing.Process(
            target=compute_range, args=(i * chunk_size, (i + 1) * chunk_size)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Python execution time: {execution_time:.2f} ms")
