import yaml

def get_tokens(key):
    config = yaml.safe_load(open("tokens.yaml"))
    return config[key]
