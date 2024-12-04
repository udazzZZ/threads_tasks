import threading
import math


def factorial_for_part(start, end, index):
    global results
    global thread_result_string
    res = math.prod(range(start, end + 1))
    results[index] = res
    thread_result_string[index] = (f"Поток номер {index + 1}: "
                                   f"произведение диапазона чисел от {start} до {end + 1} включительно. "
                                   f"Результат: {res}")


number = int(input('Введите число: '))
threads_count = int(input('Введите количество потоков: '))
part = number // threads_count
results = [1] * threads_count
thread_result_string = [''] * threads_count
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

print('Результат:', math.prod(results))
for i in thread_result_string:
    print(i)