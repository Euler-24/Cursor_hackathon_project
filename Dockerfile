FROM python:3.12-slim

WORKDIR /app

COPY django/AgriSence/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY django/AgriSence/ /app/

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=AgriSence.settings
ENV DEBUG=False

RUN mkdir -p /app/staticfiles \
    && python manage.py collectstatic --noinput

CMD ["sh", "-c", "python manage.py migrate --noinput || true; python manage.py init_schema || true; python manage.py seed_agrisence || true; exec gunicorn AgriSence.wsgi:application --bind 0.0.0.0:${PORT:-8000} --timeout 120 --workers 1 --access-logfile - --error-logfile -"]
