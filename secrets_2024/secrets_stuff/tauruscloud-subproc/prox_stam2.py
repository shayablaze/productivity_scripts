import logging
import sys
import time
from multiprocessing import Process

# Define the function containing the code
def run_subprocess_code():
    logging.info('I AM IN ************ run_subprocess_code ')
    with open("3cellos.txt", "w") as file:
        # Write the desired text to the file
        file.write("in 3 cellos for proxy stam\n ")
        time.sleep(10)
    logging.info('Woke up after 10 seconds ')
    with open("after 10 seconds.txt", "w") as file:
        # Write the desired text to the file
        file.write("in 3 cellos for proxy stam\n ")

# Create and start the subprocess
if __name__ == "__main__":
    process = Process(target=run_subprocess_code)
    process.daemon = False
    process.start()
    time.sleep(5)

    print('do something')
    sys.exit()
    print('do ddddwfwdfwdfwedf')
    # process.join()  # Wait for the subprocess to finish