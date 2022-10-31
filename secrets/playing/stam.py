import fileinput

files_list = ['/tmp/artifacts/bzt.log' , '/tmp/artifacts/bzt.log.tail.bz']
# print(files_list)

under_switch = '/tmp/artifacts/bzt.log'

def search_and_replace(filename):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('Taurus CLI Tool', 'SIGUR_ROS'), end='')

if under_switch in files_list:
    search_and_replace(under_switch)