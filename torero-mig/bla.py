import sys

# total arguments
n = len(sys.argv)
# print("Total arguments passed:", n)

account_ids = []
if n <2:
    print('no account ids provided')
else :
    print('and i say')
    for i in range(1, n):
        account_ids.append(sys.argv[i])
print('result')
print(account_ids)