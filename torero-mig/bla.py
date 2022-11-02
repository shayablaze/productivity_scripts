import os

# file_name = 'tests_to_migrate_list.txt'
# os.remove(file_name)
# f = open(file_name, "a")
# count_tests = 0
# for i in [1,2,3,7]:
#     f.write(f'{str(i)}, ')
#     count_tests+=1
# f.close()
# print(count_tests)


arr = [1,2,3,7]

bbb = [2,3,4,5,6]

arr = list(set(arr) | set(bbb))
print(arr)