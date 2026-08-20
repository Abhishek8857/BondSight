import argparse
import yaml
from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/train_config.yaml")
    parser.add_argument("--name", default="exp001")
    
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)
        cfg["name"] = args.name

    model = YOLO(cfg.pop("model"))
    model.train(**cfg)


if __name__ == "__main__":
    main()
