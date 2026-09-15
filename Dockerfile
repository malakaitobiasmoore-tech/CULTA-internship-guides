FROM python:3.10.4-bullseye

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r ./requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app

ENV HOME=/tmp
ENV TMPDIR=/tmp

CMD ["gunicorn", "website.wsgi:application", "--bind", "0.0.0.0:5000", "--worker-tmp-dir", "/tmp"]