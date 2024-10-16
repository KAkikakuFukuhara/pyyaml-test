import yaml
from pathlib import Path
from argparse import ArgumentParser
import pprint


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("config", type=str, help="config.yaml")
    args = parser.parse_args()
    config_path = Path(args.config)
    assert config_path.suffix == ".yaml"
    assert config_path.exists()

    with config_path.open("r") as f:
        config = yaml.safe_load(f.read())

    pprint.pprint(config)