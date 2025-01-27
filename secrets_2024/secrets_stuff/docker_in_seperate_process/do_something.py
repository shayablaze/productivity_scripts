# run_subprocess_async.py
import asyncio
import subprocess
import time


async def run_subprocess():
    # Run the 'prox_now.py' script asynchronously
    process = await asyncio.create_subprocess_exec(
        'python', 'prox_stam.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    # Do not wait for the subprocess to finish here, just continue running
    # If you want to check when it finishes, you can use process.returncode later

    print("Subprocess is running asynchronously...")

# Run the subprocess asynchronously without waiting for it to complete
asyncio.run(run_subprocess())

# Continue with the rest of your program, which will not be blocked
print("Main program continues running while subprocess is executing.")
time.sleep(150)