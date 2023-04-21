FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt