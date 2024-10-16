import yaml
from pathlib import Path
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--config", type=str, default='config.yaml')
    args = parser.parse_args()
    config_path = Path(args.config)
    assert config_path.exists()
    assert config_path.suffix == ".yaml"

    with config_path.open("r") as f:
        config = yaml.safe_load(f.read())

    dst_path = Path("config-dst.yaml")
    with dst_path.open("w") as f:
        yaml.safe_dump(config, f)