ARG PYTHON
FROM docker.io/python:${PYTHON}

COPY requirements_dev.txt /tmp/
RUN pip install -r /tmp/requirements_dev.txt

VOLUME /src
WORKDIR /src
ENV PYTHONPATH=/src
CMD ["pytest", "--force-regen"]
