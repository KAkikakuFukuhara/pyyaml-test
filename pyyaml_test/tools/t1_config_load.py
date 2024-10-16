import yaml

if __name__ == "__main__":
    with open('config.yaml') as file:
        config = yaml.safe_load(file.read())


