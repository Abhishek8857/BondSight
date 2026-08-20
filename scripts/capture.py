import argparse
import time
import cv2 
import numpy as np
import pyrealsense2 as rs

from pathlib import Path

def main(): 
    parser = argparse.ArgumentParser()
    # Add arguments 
    parser.add_argument("--out", default="data/raw", help="folder location to store captured images")
    parser.add_argument("--tag", default="capture", help="prefix for filenames")
    parser.add_argument("--count", type=int, required=True, default=0, help="start from a saved number")
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)

    args = parser.parse_args()
    
    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    pipeline = rs.pipeline()
    config = rs.config()
    
    # set the stream parameters
    config.enable_stream(rs.stream.color, args.width, args.height, rs.format.bgr8, 30)
    pipeline.start(config)
    
    print("Streaming. SPACE/ENTER to save, press q to exit")
    
    saved = args.count
    try:
        while True:
            frames = pipeline.wait_for_frames()


            color_frame = frames.get_color_frame()
            if not color_frame:
                continue
            color_image = np.asanyarray(color_frame.get_data())

            cv2.imshow("RealSense — SPACE to save, q to quit", color_image)
            key = cv2.waitKey(1) & 0xFF

            if key in (ord(" "), 13):  # space or enter
                fname = f"{args.tag}_{saved:03d}"
                cv2.imwrite(str(output_dir / f"{fname}.jpg"), color_image)
                saved += 1
                print(f"saved {fname} ({saved} total)")

            elif key in (ord("q"), 27):  # q or ESC
                break
    finally:
        pipeline.stop()
        cv2.destroyAllWindows()
        print(f"Done. {saved} frames saved to {output_dir}")
            

if __name__=="__main__":
    main()
    