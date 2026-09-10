FROM python:3.12-slim

WORKDIR /app

COPY django/AgriSence/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY django/AgriSence/ /app/

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=AgriSence.settings
ENV DEBUG=False

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py init_schema && python manage.py seed_agrisence || true; exec gunicorn AgriSence.wsgi:application --bind 0.0.0.0:${PORT:-8000} --timeout 120 --workers 2"]
