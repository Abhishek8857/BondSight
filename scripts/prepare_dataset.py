import argparse
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    # define the location folder for the CVAT export
    parser.add_argument("--source", required=True)
    # output folder for the processed dataset
    parser.add_argument("--destination", default="data/processed/all")

    args = parser.parse_args()
    source = Path(args.source)

    names = source / "obj.names"
    data = source / "obj_train_data"

    if not names.exists():
        print("Source file location does not exist")
        return

    names = [line.strip() for line in names.read_text().splitlines() if line.strip()]
    print(f"Found {len(names)} classes in obj.names:")
    for i, n in enumerate(names):
        print(f"  {i}: {n}")

    images_out = Path(args.destination) / "images"
    labels_out = Path(args.destination) / "labels"
    images_out.mkdir(parents=True, exist_ok=True)
    labels_out.mkdir(parents=True, exist_ok=True)

    image_exts = {".jpg", ".jpeg", ".png", ".bmp"}
    # CVAT exports sometimes nest images under an extra
    # <task_name>/obj_train_data/ subfolder instead of putting them
    # directly in obj_train_data/. rglob handles both layouts.
    images = [p for p in data.rglob("*") if p.is_file() and p.suffix.lower() in image_exts]
    print(f"Found {len(images)} images in {data}")

    copied = 0
    missing_labels = []
    for img_path in images:
        label_path = img_path.with_suffix(".txt")
        out_img = images_out / img_path.name
        out_label = labels_out / label_path.name
        if out_img.exists() or out_label.exists():
            print(f"  warning: duplicate filename {img_path.name}, overwriting in destination")
        shutil.copy2(img_path, out_img)
        if label_path.exists():
            shutil.copy2(label_path, out_label)
            copied += 1
        else:
            missing_labels.append(img_path.name)

    print(f"\nCopied {copied} image+label pairs to {args.destination}")
    if missing_labels:
        print(f"{len(missing_labels)} images missing labels:")
        print(missing_labels)


if __name__ == "__main__":
    main()