FROM frolvlad/alpine-python-machinelearning
RUN set -x

WORKDIR /app
COPY . .

RUN apk add --update --no-cache --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    pip install --upgrade pip && \
    pip install Flask requests && \
    pip install Flask-HTTPAuth python-dotenv auth0-python Flask-JWT flask_cors python-jose six psycopg2 sqlalchemy && \
    chmod a+x /app/run.py && \
    apk del build-deps

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 5000
CMD python /app/run.py --host=0.0.0.0
