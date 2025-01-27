import re
import time
def censor_strings_in_file(strings_to_censor, file_name):
    """
    Replaces all occurrences of the strings in the given file with ***********.

    Args:
        strings_to_censor (list): A list of strings to be replaced.
        file_name (str): The name of the file to be processed.

    Returns:
        None: The function modifies the file in place.
    """
    try:
        # Read the content of the file
        with open(file_name, 'r') as file:
            content = file.read()

        # Compile a regular expression for all strings to censor
        pattern = re.compile('|'.join(map(re.escape, strings_to_censor)))

        # Replace all occurrences with ***********
        content = pattern.sub('***********', content)

        # Write the modified content back to the file
        with open(file_name, 'w') as file:
            file.write(content)

        print(f"Successfully censored strings in '{file_name}'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")






#
# def censor_strings_in_file_periodically(strings_to_censor, file_name, interval=5):
#     """
#     Periodically replaces strings in the file with ***********, remembering the last processed position.
#
#     Args:
#         strings_to_censor (list): A list of strings to be replaced.
#         file_name (str): The name of the file to be processed.
#         interval (int): The interval in seconds to wait before reprocessing the file.
#
#     Returns:
#         None
#     """
#     last_position = 0
#
#     while True:
#         try:
#             with open(file_name, 'r+') as file:
#                 # Move to the last processed position
#                 file.seek(last_position)
#
#                 # Read from the last position onwards
#                 content = file.read()
#                 print('doing it now!!!!!!!!!')
#                 # Replace each string in the list with ***********
#                 for string in strings_to_censor:
#                     content = content.replace(string, '*******')
#
#                 # Update the file starting from the last position
#                 file.seek(last_position)
#                 file.write(content)
#                 file.truncate()
#
#                 # Update the last position
#                 last_position = file.tell()
#
#             print(f"Processed file up to position {last_position}.")
#
#         except FileNotFoundError:
#             print(f"Error: The file '{file_name}' does not exist.")
#             break
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             break
#
#         time.sleep(interval)


import time
# from filelock import FileLock

def censor_strings_in_file_periodically(strings_to_censor, file_name, interval=30):
    """
    Periodically replaces strings in the file with ***********, processing only newly added content.

    Args:
        strings_to_censor (list): A list of strings to be replaced.
        file_name (str): The name of the file to be processed.
        interval (int): The interval in seconds to wait before reprocessing the file.

    Returns:
        None
    """
    last_position = 0  # Start processing from the beginning of the file initially
    while True:
        try:
           with open(file_name, 'r+') as file:
                # Move to the last processed position
                file.seek(0, 2)  # Move to the end of the file to capture its size
                file_size = file.tell()
                print(f'current file size is {file_size}')
                # Check if there's new content
                if file_size > last_position:
                    file.seek(last_position)  # Move to the last processed position
                    new_content = file.read()
                    print('here is the new content')
                    print('')
                    print(new_content)
                    print('')
                    print('end of new content')
                    # Replace each string in the list with ***********
                    for string in strings_to_censor:
                        new_content = new_content.replace(string, 'goodword123')

                    # Write the updated new content back to the file
                    file.seek(last_position)
                    file.write(new_content)
                    file.truncate()

                    # Update the last position to the current end of the file
                    last_position = file_size
                    print('the updated content is ')
                    print(new_content)
                    print(f'now i will sleep for no reason before upload and last_position is {last_position}')
                    print(f"Processed new content up to position {last_position}.")
                else:
                    print("No new content to process.")

        except FileNotFoundError:
            print(f"Error: The file '{file_name}' does not exist.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

        time.sleep(interval)
# Example usage
strings = ["badword", "Badword"]
print('do i get here i wait for you')
censor_strings_in_file_periodically(strings, "example.txt")