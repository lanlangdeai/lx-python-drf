FROM python:3.6

WORKDIR /opt/app

COPY . .

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 8080

ENTRYPOINT ["sh", "entrypoint.sh"]