# Procesos e hilos
from multiprocessing import Process


def task(n):
    return n * n


if __name__ == "__main__":
    processes = [Process(target=task, args=(i,)) for i in range(10)]
