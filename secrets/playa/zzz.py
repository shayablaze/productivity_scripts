import fileinput
import os
import re
import zipfile
import shutil

def search_and_replace(filename):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('Taurus CLI Tool v1', 'cccc'), end='')

def _zip_file( zipf, path, exclude_dirs=(), exclude_files=None):
    print('Zipping path {}'.format(path))
    excl_files = "(?:^" + "$)|(?:^".join(exclude_files) + "$)" if exclude_files else "(!.*)"
    handled_fnames = set()
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in set([f for f in files if not re.match(excl_files, f) and f not in handled_fnames]):
            # print('Adding file [{}] to zip'.format(os.path.join(root, file)))
            try:
                zipf.write(os.path.join(root, file), arcname=file)
                handled_fnames.add(file)
            except FileNotFoundError as err:
                # We shouldn't be here (as we are doing an os.walk)
                # but I've seen us here before, so we will just move on
                print('File is missing; Not including in the zip (error: {})'.format(err))


path_to_zip_file = 'artifacts - 2022-06-28T160220.133.zip'
directory_to_extract_to = 'target'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

file_list = os.listdir('./target')
for file_name in file_list:
    search_and_replace(f'./target/{file_name}')
zip_file = zipfile.ZipFile('artifacts - 2022-06-28T160220.133.zip', 'w', zipfile.ZIP_DEFLATED)

_zip_file(zip_file, 'target')
zip_file.close()
shutil.rmtree('target', ignore_errors=True)

