FROM python:3.7-buster

WORKDIR /workdir

# Installing other needed components
COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

# Copy the algorithms
COPY scripts /workdir/

# Installing the APP
RUN pip install -e .

# Copying the data
COPY data /data/

# Run Bash
CMD ["/bin/bash"]
