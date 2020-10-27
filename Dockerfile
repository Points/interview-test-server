FROM python:3.6-slim

ENV APP_GROUP=app \
    APP_USER=app

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \
    && apt-get install -qq ca-certificates gettext git libxmlsec1-dev gcc gnupg2 libpq-dev \
    && pip install 'pipenv>=8.3.0,<8.4.0' \
    && groupadd ${APP_GROUP} \
    && useradd -m -g ${APP_GROUP} ${APP_USER} \
    && echo -n "America/Toronto" > /etc/timezone

# Cache `pipenv install` separately from project src changes.
COPY ["Pipfile.lock", "/tmp/"]

RUN cd /tmp \
    && pipenv install --ignore-pipfile --dev --system

RUN mkdir /app
WORKDIR /app
ADD . /app

EXPOSE 5000

CMD gunicorn wsgi:app -w 2 -b :5000