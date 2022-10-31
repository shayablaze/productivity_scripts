import fileinput
import io
import os
import re
import time
import zipfile
import shutil

class SecretsEncryptor:

    def is_zip(self, bytes_under_test):
        begg = bytes_under_test[:2]
        return begg == b'PK'

    def search_and_replace(self, filename, secrets):
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                # new_line = line.replace('', '')

                new_line = None
                for key,value in secrets.items():
                    # print(key)
                    # print(value)
                    if not new_line:
                        new_line = line.replace(key, value)
                    else:
                        new_line = new_line.replace(key, value)
                print(new_line, end='')
    def _zip_file(self, zipf, path, exclude_dirs=(), exclude_files=None):
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

    def encrypt_data_content(self, bytes_to_encrypt, secrets, more_info = ''):
        print(f'starting encrypt with {more_info}')
        if self.is_zip(bytes_to_encrypt):
            print(f'is a zip {more_info}')
            z = zipfile.ZipFile(io.BytesIO(bytes_to_encrypt))
            temp_folder = f'temphere_{time.time()}'
            zip_file_thing = f'temp_zip{time.time()}.zip'
            z.extractall(temp_folder)
            z.close()
            file_list = os.listdir(f'./{temp_folder}')
            for file_name in file_list:
                print(f'printing file {file_name} info: {more_info}')
                self.search_and_replace(f'./{temp_folder}/{file_name}', secrets)
            zip_file = zipfile.ZipFile(zip_file_thing, 'w', zipfile.ZIP_DEFLATED)

            self._zip_file(zip_file, temp_folder)
            zip_file.close()
            with open(zip_file_thing, 'rb') as file_data:
                bytes_content = file_data.read()
            os.remove(zip_file_thing)
            shutil.rmtree(temp_folder)
            return bytes_content
        else:
            # return bytes_to_encrypt
            print(f'not a zip {more_info}')
            content_string = bytes_to_encrypt.decode("latin-1")
            for key,value in secrets.items():
                content_string = content_string.replace(key, value)
            return str.encode(content_string)
