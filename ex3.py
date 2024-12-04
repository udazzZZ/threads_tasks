import threading
import math


def factorial_for_part(start, end, index):
    global results
    results[index] = math.prod(range(start, end + 1))


number = int(input('Введите число: '))
threads_count = 10
part = number // threads_count
results = [1] * threads_count
threads = []

for i in range(threads_count):
    if i != threads_count - 1:
        thread = threading.Thread(target=factorial_for_part, args=(i * part + 1,
                                                                   (i + 1) * part,
                                                                   i, ))
        thread.start()
        threads.append(thread)
    else:
        thread = threading.Thread(target=factorial_for_part, args=(i * part + 1,
                                                                   number,
                                                                   i, ))
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()

print(math.prod(results))