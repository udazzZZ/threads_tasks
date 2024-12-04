import threading

def is_prime(number):
    if number < 2:
        return False
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
            return False
    return True


def find_primes_in_range(start, end, lock):
    global result
    local_primes = [num for num in range(start, end + 1) if is_prime(num)]
    with lock:
        result.extend(local_primes)


result = []
diapason_start = int(input('Первое число диапазона: '))
diapason_end = int(input('Второе число диапазона: '))
threads_count = 10
lock = threading.Lock()

part = (diapason_end - diapason_start + 1) // threads_count
threads = []

for i in range(threads_count):
    if i != threads_count - 1:
        thread = threading.Thread(target=find_primes_in_range, args=(diapason_start + i * part,
                                                                     diapason_start + (i + 1) * part,
                                                                     lock, ))
        thread.start()
        threads.append(thread)
    else:
        thread = threading.Thread(target=find_primes_in_range, args=(diapason_start + i * part,
                                                                     diapason_end,
                                                                     lock, ))
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()

print(result)