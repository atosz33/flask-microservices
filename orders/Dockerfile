FROM python:latest

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /


WORKDIR src
CMD  [ "/bin/bash", "run_gunicorn.sh" ]
