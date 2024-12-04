import threading

def sort_array(arr, index):
    global sorted_parts
    sorted_parts[index] = sorted(arr)

def merge_two_sorted_arrays(arr1, arr2):
    merged = []
    i1, i2 = 0, 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            merged.append(arr1[i1])
            i1 += 1
        else:
            merged.append(arr2[i2])
            i2 += 1
    if i1 == len(arr1):
        merged.extend(arr2[i2:])
    else:
        merged.extend(arr1[i1:])
    return merged


array = list(map(int, input('Введите числа массива через пробел: ').split()))
array_length = len(array)
threads_count = int(input('Введите количество потоков: '))
part = array_length // threads_count
sorted_parts = [[]] * threads_count
threads = []

for i in range(threads_count):
    if i != threads_count - 1:
        thread = threading.Thread(target=sort_array, args=(array[i * part:(i + 1) * part], i))
        thread.start()
        threads.append(thread)
    else:
        thread = threading.Thread(target=sort_array, args=(array[i * part:array_length], i))
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()

while len(sorted_parts) > 1:
    merged_array = []
    for i in range(0, len(sorted_parts), 2):
        if i + 1 < len(sorted_parts):
            merged = merge_two_sorted_arrays(sorted_parts[i], sorted_parts[i + 1])
        else:
            merged = sorted_parts[i]
        merged_array.append(merged)
    sorted_parts = merged_array


print('Результат:', ' '.join([str(i) for i in sorted_parts[0]]))
# пример: 384 829 102 395 384 125 309 476 145 992 625 742 983 285 374 109 276 193 921 156