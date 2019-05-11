FROM gliderlabs/alpine:3.3

RUN apk update
RUN apk upgrade
RUN apk add bash
RUN apk add --update 
RUN apk add python3 

COPY get-pip.py /get-pip.py 

RUN python3 /get-pip.py
RUN python3 -m pip install --upgrade pip 
RUN pip install virtualenv 

WORKDIR /app

COPY . /app 
# RUN virtualenv /env 
RUN pip install -r /app/requirements.txt

RUN apk add build-base 
RUN rm -rf /var/cache/apk/*

# EXPOSE 5000

CMD ["python3", "/app/app.py"]