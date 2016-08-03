FROM python:2.7.11
ENV PYTHONBUFFERED 1
RUN mkdir -p /usr/src/app/hodor
WORKDIR /usr/src/app
COPY server.py /usr/src/app/
COPY hodor/__init__.py /usr/src/app/hodor/
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
