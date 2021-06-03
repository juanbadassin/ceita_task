FROM selenium/standalone-chrome

USER root

RUN apt-get update && apt-get install -y python3 python3-pip

ADD . /source
WORKDIR /source
RUN pip3 install -r requirements.txt

ENTRYPOINT  python3 -m unittest test_cases.test_login