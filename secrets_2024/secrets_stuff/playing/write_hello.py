# write_hello.py
import time
# Open the file in write mode, and write "Hello" to it
time.sleep(10)
print('hey from sub proc')
with open('abbccccddddnnnnnnn.txt', 'w') as file:
    file.write('Hello')
