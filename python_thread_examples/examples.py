import threading

'''
Write a Python program to create multiple threads and print their names.


def print_thread_names():
    print("Current thread name : ", threading.current_thread().name)

threads = []
for i in range(7):
    thread = threading.Thread(target=print_thread_names)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
'''

'''
Write a Python program to download multiple files concurrently using threads.


import urllib.request

def download_files(url, filename):
    urllib.request.urlretrieve(url, filename)

# Create a list of files to download
files_to_download = [
    {"url": "https://en.wikipedia.org/wiki/British_logistics_in_the_Normandy_campaign", "filename": "D:\\Projects\\multiplayer-game\\python_thread_examples\\1.html"},
    {"url": "https://en.wikipedia.org/wiki/Graph_(abstract_data_type)", "filename": "D:\\Projects\\multiplayer-game\\python_thread_examples\\2.html"},
    {"url": "https://example.com/", "filename": "D:\\Projects\\multiplayer-game\\python_thread_examples\\3.html"}
]


threads = []
for i in range(len(files_to_download)):
    t = threading.Thread(target=download_files, args=(files_to_download[i]["url"], files_to_download[i]["filename"]))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
'''
'''
Write a Python program that creates two threads to find and print even and odd numbers from 30 to 50.
def print_even():
    even_list = []
    for i in range(30, 51, 2):
        even_list.append(i)
    print("Even List : ", even_list)

def print_odd():
    odd_list = []
    for i in range(31, 50, 2):
        odd_list.append(i)
    print("Odd List : ", odd_list)

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

t1.start()
t2.start()

t1.join()
t2.join()
'''

