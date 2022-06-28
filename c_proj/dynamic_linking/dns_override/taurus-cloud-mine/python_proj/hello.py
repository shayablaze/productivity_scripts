

import subprocess, os
print ('in_shayas_bitcin_project11111111222')

file_name="/app/aaa"
# if os.path.exists(file_name):
#     os.remove(file_name)
f= open(file_name,"w+")
f.write("127.0.0.1 www.blazedemo.com\r\n")
f.write("127.0.0.1 blazedemo.com\r\n")
f.write("127.0.0.1 www.israelhayom.co.il\r\n")
f.close()

my_env = env=os.environ
my_env["LD_PRELOAD"] = "/usr/lib/libhostspriv.so"
my_command="bash i_run_in_sub.sh"

subprocess.Popen(my_command, env=my_env, shell=True)