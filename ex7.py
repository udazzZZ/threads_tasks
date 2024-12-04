from concurrent.futures import ThreadPoolExecutor

def read_words(file, words):
    for string in [i.rstrip() for i in file.readlines()]:
        for word in string.split():
            words.append(word)

def count_frequency_of_words(chunk):
    frequency_of_the_words = dict()
    for word in chunk:
        if word.lower() in frequency_of_the_words.keys():
            frequency_of_the_words[word.lower()] += 1
        else:
            frequency_of_the_words[word.lower()] = 1
    return frequency_of_the_words


threads_count = int(input('Введите количество потоков: '))

with open('file_for_ex7') as file:
    words = []
    read_words(file, words)


chunks_for_threads = []
for i in range(threads_count):
    chunks_for_threads.append(words[i::threads_count])

print(chunks_for_threads)

with ThreadPoolExecutor() as executor:
    result = dict()
    counted_words_for_chunks = executor.map(count_frequency_of_words, chunks_for_threads)
    for chunk in counted_words_for_chunks:
        for key in chunk.keys():
            if key in result.keys():
                result[key] += chunk[key]
            else:
                result[key] = chunk[key]
    for key in sorted(result, key=lambda k: -result[k]):
        print(key, result[key])




