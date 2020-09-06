FROM launcher.gcr.io/google/ubuntu16_04

RUN apt-get -y update
RUN apt-get -y install gcc wget ca-certificates software-properties-common

    # Install Python 3.7
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get -y update && \
    apt-get -y install python3.7

    # Install Git >2.0.1
RUN add-apt-repository ppa:git-core/ppa && \
    apt-get -y update && \
    apt-get -y install git

    # Setup Google Cloud SDK (latest)
RUN mkdir -p /builder
RUN wget -qO- https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz | tar zxv -C /builder && \
    CLOUDSDK_PYTHON="python3.7" /builder/google-cloud-sdk/install.sh --usage-reporting=false \
        --bash-completion=false \
        --disable-installation-options
    # install crcmod: https://cloud.google.com/storage/docs/gsutil/addlhelp/CRC32CandInstallingcrcmod
RUN apt-get -y install build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev
RUN apt-get -y install python3.7-dev libpython3.7 python3-pip
RUN apt-get -y install python3.7
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
RUN update-alternatives --config python3

COPY . /app
WORKDIR /app

RUN python3 -m pip install --upgrade pip && \
    pip3 install -U crcmod && pip3 install Flask==1.1.2 tensorflow==2.2.0 stocker

    # Clean up
RUN apt-get -y remove gcc python-dev python-setuptools wget && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf ~/.config/gcloud

RUN git config --system credential.helper gcloud.sh
CMD ['main.py']
