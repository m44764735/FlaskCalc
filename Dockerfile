FROM python:3.5-alpine

EXPOSE 5000

RUN mkdir -p /usr/src/main1
WORKDIR /usr/src/main1

COPY requirements.txt /usr/src/main1/
RUN pip install --no-cache-dir -r requirements.txt

COPY main1.py /usr/src/main1/main1.py

CMD [ "python3", "main1.py" ]
