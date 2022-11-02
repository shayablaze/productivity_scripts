import os

file_name = 'tests_to_migrate_list.txt'
os.remove(file_name)
f = open(file_name, "a")
count_tests = 0
for i in [1,2,3,7]:
    f.write(f'{str(i)}, ')
    count_tests+=1
f.close()
print(count_tests)