FROM ubuntu:20.04
ADD . /myretailapp
WORKDIR /myretailapp
RUN apt-get update && \
apt-get install -yq --no-install-recommends \
automake \
autoconf \
bison \
curl \
flex \
libtool \
make \
wget \
python3-pip \
python3-dev
RUN pip3 install -r requirements.txt
