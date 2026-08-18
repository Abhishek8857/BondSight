import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", required=True)
    parser.add_argument("--data", default="configs/data.yaml")
    parser.add_argument("--split", default="test", choices=["val", "test"])
    parser.add_argument("--project", default="/proki/models/eval")
    parser.add_argument("--name", default="exp001")
    args = parser.parse_args()
    
    model = YOLO(model=args.weights)
    metrics = model.val(data=args.data, 
                        split=args.split,
                        plots=True, 
                        name=args.name,
                        project=args.project)
    
    print(f"\nPrecision:{metrics.results_dict['metrics/precision(B)']:.3f}")
    print(f"Recall:{metrics.results_dict['metrics/recall(B)']:.3f}")
    print(f"mAP50:{metrics.results_dict['metrics/mAP50(B)']:.3f}")
    print(f"mAP50-95:{metrics.results_dict['metrics/mAP50-95(B)']:.3f}")
    print(f"\nPlots and prediction images saved to: {args.project}/{args.name}")

if __name__ == "__main__":
    main()