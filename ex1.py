import threading


def function():
    pass


threads = []
for i in range(3):
    thread = threading.Thread(target=function)
    threads.append(thread)

for i in threads:
    print(i.name)
