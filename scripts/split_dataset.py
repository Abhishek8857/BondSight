import argparse
import random
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="folder with images/ and labels/ subfolders to split")
    parser.add_argument("--destination", default="data/processed")
    parser.add_argument("--train", type=float, default=0.7)
    parser.add_argument("--val", type=float, default=0.2)
    parser.add_argument("--test", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    source_images = Path(args.source) / "images"
    source_labels = Path(args.source) / "labels"
    images = sorted(source_images.glob("*.*"))

    random.seed(args.seed)
    random.shuffle(images)

    n = len(images)
    n_train = int(n * args.train)
    n_val = int(n * args.val)
    splits = {
        "train": images[:n_train],
        "val": images[n_train:n_train + n_val],
        "test": images[n_train + n_val:],
    }

    for split, files in splits.items():
        output_images = Path(args.destination) / "images" / split
        output_labels = Path(args.destination) / "labels" / split
        output_images.mkdir(parents=True, exist_ok=True)
        output_labels.mkdir(parents=True, exist_ok=True)
        for img_path in files:
            label_path = source_labels / (img_path.stem + ".txt")
            shutil.copy2(img_path, output_images / img_path.name)
            if label_path.exists():
                shutil.copy2(label_path, output_labels / label_path.name)
        print(f"{split}: {len(files)} images")


if __name__ == "__main__":
    main()