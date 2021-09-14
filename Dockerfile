FROM python:3.9.7-slim-buster
RUN apt update && apt upgrade -y
RUN pip3 install -U pip
RUN pip install telepot
CMD python bot.py
