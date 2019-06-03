import yaml

def load(path):
    document = open(path, 'r')
    parsed = yaml.safe_load(document)
    return parsed
