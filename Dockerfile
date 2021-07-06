FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD ["testfile.py"]

ENTRYPOINT ["python3]