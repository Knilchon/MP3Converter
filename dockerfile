FROM python:3.10

EXPOSE 5000

RUN mkdir /Flask

WORKDIR /Flask

COPY . .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg

ENV FLASK_APP=main.py

CMD ["flask", "run", "--port", "5000","--host","0.0.0.0"]


