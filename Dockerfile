FROM ultralytics/ultralytics:latest-python-export

WORKDIR /proki

COPY config/ /config
COPY data/ /data
COPY scripts/ /scripts

CMD [ "bash" ]
