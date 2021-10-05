FROM python:3.7

ENV HOME /root

WORKDIR /application

ADD src/requirements/requirements_api.txt /application/requirements.txt

RUN pip3 install -r requirements.txt



ENTRYPOINT ["python3", "application.py"]
