"""Day 22: Multithreading

Topics:
- Thread
- Lock
- Race conditions
- ThreadPoolExecutor

Multithreading allows multiple tasks to run concurrently, which is useful for
I/O-bound work such as downloading files or making network requests.
"""

import threading
import time


# 1. Thread
print("Example 1: Thread")

def print_message():
    print("Thread running")

thread = threading.Thread(target=print_message)
thread.start()
thread.join()
print()


# 2. Lock
print("Example 2: Lock")

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(1000):
        with lock:
            global counter
            counter += 1

threads = [threading.Thread(target=increment_counter) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter value:", counter)  # Output: Counter value: 5000
print()


# 3. Race conditions
print("Example 3: Race conditions")

race_counter = 0


def risky_increment():
    global race_counter
    for _ in range(1000):
        race_counter += 1

threads = [threading.Thread(target=risky_increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Race counter value:", race_counter)  # Output may be less than 5000
print()


# 4. ThreadPoolExecutor
print("Example 4: ThreadPoolExecutor")


def square(n):
    time.sleep(0.1)
    return n * n

# Simulate a pool with a few threads
threads = []
results = []

for number in [1, 2, 3, 4]:
    thread = threading.Thread(target=lambda value=number: results.append(square(value)))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Squares:", results)  # Output: Squares: [1, 4, 9, 16]
print()


# Practice 1: Download multiple files simultaneously
print("Practice 1: Download multiple files simultaneously")

files = ["file1", "file2", "file3"]


def download_file(file_name):
    time.sleep(0.1)
    return f"Downloaded {file_name}"

threads = []
completed = []

for file_name in files:
    thread = threading.Thread(target=lambda name=file_name: completed.append(download_file(name)))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for item in completed:
    print(item)
print()


# Practice 2: Download manager
print("Practice 2: Download manager")

class DownloadManager:
    def __init__(self):
        self.lock = threading.Lock()
        self.completed = []

    def download(self, file_name):
        result = download_file(file_name)
        with self.lock:
            self.completed.append(result)
        return result

manager = DownloadManager()
threads = []
for file_name in files:
    thread = threading.Thread(target=lambda name=file_name: manager.download(name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Completed downloads:", manager.completed)
print()


# Practice 3: Image downloader
print("Practice 3: Image downloader")

image_files = ["image1.png", "image2.png"]


def download_image(image_name):
    time.sleep(0.1)
    return f"Image {image_name} downloaded"

threads = []
image_results = []

for image_name in image_files:
    thread = threading.Thread(target=lambda name=image_name: image_results.append(download_image(name)))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for item in image_results:
    print(item)
print()


# Practice 4: Web scraper
print("Practice 4: Web scraper")

pages = ["page1", "page2"]


def scrape_page(page_name):
    time.sleep(0.1)
    return f"Scraped {page_name}"

threads = []
scraped_pages = []

for page_name in pages:
    thread = threading.Thread(target=lambda name=page_name: scraped_pages.append(scrape_page(name)))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for item in scraped_pages:
    print(item)
