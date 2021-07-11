FROM python:3

WORKDIR /$HOME/independent_chain_project

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "./testfile.py"]