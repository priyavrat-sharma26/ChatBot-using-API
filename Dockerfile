FROM python:3.7
RUN mkdir /app
WORKDIR /src/
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "/app/main.py"]