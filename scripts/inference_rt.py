import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", required=True)
    parser.add_argument("--source", default="6")
    parser.add_argument("--confidence", type=float ,default=0.6)
    
    args = parser.parse_args()
    
    source = args.source
    model = YOLO(model=args.weights)
    results = model.predict(source=source, conf=args.confidence, show=True, stream=True)

    for r in results:
        pass
    
if __name__=="__main__":
    main()