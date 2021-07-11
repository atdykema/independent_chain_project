FROM python:3

WORKDIR /$HOME/src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "./testfile.py" ]

