FROM python:3.9.13-alpine3.15
WORKDIR /app
COPY . /app 
RUN pip install -r ./requirements.txt
EXPOSE 8000
CMD python /app/app.py







