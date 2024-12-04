import os
import threading
from queue import Queue

def find_files(queue, pattern, results, lock):
    while not queue.empty():
        try:
            directory = queue.get_nowait()
        except Exception:
            break

        matched_files = []
        for dir_path, dirs, files in os.walk(directory):
            for file in files:
                if pattern in file:
                    matched_files.append(os.path.join(dir_path, file))

        with lock:
            results.extend(matched_files)

        queue.task_done()


directories = [
    "C:\Program Files (x86)"
]
pattern = ".txt"
threads_count = 5

queue = Queue()
results = []
lock = threading.Lock()

for directory in directories:
    queue.put(directory)

threads = []
for i in range(threads_count):
    thread = threading.Thread(target=find_files, args=(queue, pattern, results, lock))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Найденные файлы:")
for file in results:
    print(file)


