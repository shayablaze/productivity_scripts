import configparser

def load_credentials():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read("../the_keys/config.ini")

    # Access the 'Credentials' section
    try:
        key = config['Credentials']['key']
        secret = config['Credentials']['secret']
        return key, secret
    except KeyError as e:
        print(f"Missing expected configuration: {e}")
        return None, None

if __name__ == "__main__":
    # Path to the configuration file

    # Load the credentials
    key, secret = load_credentials()

    if key and secret:
        print("Key:", key)
        print("Secret:", secret)
    else:
        print("Failed to load credentials.")