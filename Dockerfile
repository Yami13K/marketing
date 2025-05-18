# Build Stage
FROM python:3.10.6-alpine as builder
LABEL maintainer='Maher'

# Env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# User home dir
RUN adduser -D kad-dev
WORKDIR /home/kad-dev

# Install build dependencies
RUN apk --no-cache add \
    build-base \
    libffi-dev \
    libressl-dev \
    git \
    postgresql-client \
    gettext

# Reqs Installation
COPY --chown=kad-dev:kad-dev requirements.txt .
RUN python -m pip install --no-cache-dir --disable-pip-version-check --requirement requirements.txt


# Final Stage
FROM python:3.10.6-alpine
LABEL maintainer='Maher'

# Recreate the kad-dev user
RUN adduser -D kad-dev

# Copy the installed dependencies and Gunicorn from the builder stage
COPY --from=builder --chown=kad-dev:kad-dev /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY --from=builder --chown=kad-dev:kad-dev /usr/local/bin/celery /usr/local/bin/celery
COPY --from=builder --chown=kad-dev:kad-dev /usr/bin/git /usr/bin/git
COPY --from=builder --chown=kad-dev:kad-dev /usr/lib/libpq.so.* /usr/lib/
COPY --from=builder --chown=kad-dev:kad-dev /usr/lib/libintl.so.* /usr/lib/
COPY --from=builder --chown=kad-dev:kad-dev /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the rest of the application
WORKDIR /home/kad-dev
COPY --chown=kad-dev:kad-dev . .
USER root
RUN chown -R kad-dev:kad-dev /home/kad-dev/
USER kad-dev
