FROM python:3.12-slim

COPY requirements.txt /app/requirements.txt

WORKDIR /app/

EXPOSE 8000

RUN pip install -r requirements.txt

COPY . .

RUN cd /insurance

CMD python manage.py runserver 0.0.0.0:8000