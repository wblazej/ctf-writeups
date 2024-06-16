FROM python:3.9-alpine
WORKDIR /app

COPY . .

RUN apk update && apk add socat
RUN pip install -r requirements.txt

USER nobody

EXPOSE 1337
CMD ["socat", "tcp-listen:1337,reuseaddr,fork", "exec:python3 /app/task.py,stderr"]