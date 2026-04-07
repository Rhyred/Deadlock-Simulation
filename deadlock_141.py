import os
import threading
import time

def background(index, locks):
    first_lock = locks[index]
    second_lock = locks[(index + 1) % len(locks)]

    with first_lock:
        print(f"    Thread {index + 1}: first lock acquired")
        time.sleep(1)
        with second_lock:
            print(f"    Thread {index + 1}: second lock acquired")


if __name__ == "__main__":
    print(f"Process ID: {os.getpid()}")
    locks = [threading.Lock() for _ in range(3)]

    threads = []
    for i in range(3):
        thread = threading.Thread(target=background, args=(i, locks))
        threads.append(thread)

    for i, thread in enumerate(threads):
        print(f"Starting Thread {i + 1}")
        thread.start()

    for thread in threads:
        thread.join()

    print("Finished execution")