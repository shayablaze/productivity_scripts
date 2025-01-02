import re

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

# Example usage
strings = ["sit", "deafness"]
censor_strings_in_file(strings, "example.txt")