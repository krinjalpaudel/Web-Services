FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip \
    && pip install django djangorestframework pillow

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
