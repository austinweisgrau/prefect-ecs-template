FROM prefecthq/prefect:2-python3.10
RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /opt/prefect

COPY setup.py .
COPY requirements.txt .
COPY flows/ /opt/prefect/flows/
COPY blocks/ /opt/prefect/blocks/
COPY utilities/ /opt/prefect/utilities/
COPY flows/ /opt/prefect/flows/

# Install parsons with minimal dependencies
ENV PIP_NO_BINARY=parsons
ENV PARSONS_LIMITED_DEPENDENCIES=true

RUN pip install .