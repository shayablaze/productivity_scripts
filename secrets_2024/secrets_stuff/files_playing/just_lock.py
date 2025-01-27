import fcntl
import time

with open("example.txt", "r+") as file:
    fcntl.flock(file, fcntl.LOCK_EX)  # Acquire exclusive lock
    print("Lock acquired")
    time.sleep(10)  # The lock is still held during this sleep
    print("Finished sleeping")
    fcntl.flock(file, fcntl.LOCK_UN)  # Explicitly release the lock