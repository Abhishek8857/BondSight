FROM ultralytics/ultralytics:latest-python-export

# Added to ensure headless plotting 
ENV MPLBACKEND=Agg

RUN apt-get update && apt-get install -y \
    libgtk2.0-dev \ 
    pkg-config \
    v4l-utils \
    libusb-1.0-0 \ 
    && rm -rf /var/lib/apt/lists/*

# Install pytorch for GPU driven training
RUN pip uninstall -y torch torchvision torchaudio opencv-python-headless && \
    pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126 && \
    pip install opencv-python pyrealsense2 

# Added bondsight folder as workdir
WORKDIR /bondsight

CMD [ "bash" ]
