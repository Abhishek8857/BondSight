FROM ultralytics/ultralytics:latest-python-export

# Added to ensure headless plotting 
ENV MPLBACKEND=Agg

# Added proki folder as workdir
WORKDIR /proki

# Install pytorch for GPU driven training
RUN pip uninstall -y torch torchvision torchaudio && \
    pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

CMD [ "bash" ]
