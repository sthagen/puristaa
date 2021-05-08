FROM python:3.9.5-slim-buster
RUN export DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y --no-install-recommends \
    tini && \
apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade --no-cache-dir pip && \
pip install --upgrade --no-cache-dir setuptools && \
pip install --no-cache-dir wheel && \
pip install --no-cache-dir -r requirements.txt
RUN useradd --create-home action
USER action
COPY prefix_compression /app/prefix_compression
ENV PYTHONFAULTHANDLER=1
ENTRYPOINT ["tini", "--", "python", "-m", "prefix_compression"]
ARG BUILD_TS
ARG REVISION
ARG VERSION
LABEL org.opencontainers.image.created=$BUILD_TS \
    org.opencontainers.image.authors="Stefan Hagen <mailto:stefan@hagen.link>" \
    org.opencontainers.image.url="https://hub.docker.com/repository/docker/shagen/prefix-compression/" \
    org.opencontainers.image.documentation="https://sthagen.github.io/python-prefix_compression/" \
    org.opencontainers.image.source="https://github.com/sthagen/python-prefix_compression/" \
    org.opencontainers.image.version=$VERSION \
    org.opencontainers.image.revision=$REVISION \
    org.opencontainers.image.vendor="Stefan Hagen <mailto:stefan@hagen.link>" \
    org.opencontainers.image.licenses="MIT License" \
    org.opencontainers.image.ref.name="shagen/prefix-compression" \
    org.opencontainers.image.title="Prefix Compression." \
    org.opencontainers.image.description="Shared prefix compression of ordered string sequences."
