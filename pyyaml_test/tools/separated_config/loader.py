from argparse import ArgumentParser
from pathlib import Path
import pprint

import yaml


if __name__ == "__main__":
    ### Argparse
    parser = ArgumentParser()
    parser.add_argument("--config", type=str, default='root-config.yaml')
    args = parser.parse_args()

    ### path checking
    config_path = Path(args.config)
    assert config_path.exists()
    assert config_path.suffix == ".yaml"

    ### load yaml
    with config_path.open("r") as f:
        config = yaml.safe_load(f.read())
    pprint.pprint(config)
    """出力結果
    {'module1': {'path': 'pyyaml_test/tools/separated_config/module1-config.yaml'},
     'name': 'config'}
    """

    ### load yaml in writed path in yaml
    # /pyyaml_test/tools/separated_config
    file_dir = Path(__file__).absolute().parent
    # /
    root_dir = file_dir.parent.parent.parent
    mod1_path = root_dir.joinpath(config['module1']['path'])
    assert mod1_path.exists()
    with mod1_path.open("r") as f:
        config2 = yaml.safe_load(f.read())
    config['module1'] = config2
    pprint.pprint(config)
    """出力結果
    {'module1': {'name': 'mod1'}, 'name': 'config'}
    """
