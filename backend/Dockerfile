FROM python:alpine
WORKDIR /src
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV SECRET_KEY=abc123
ENV DEBUG=True

COPY . .
RUN python manage.py makemigrations && python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "my_server.wsgi:application"]