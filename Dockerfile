FROM gautambaghel/flask

COPY . /work

WORKDIR /work

CMD ["python3", "server.py"]
