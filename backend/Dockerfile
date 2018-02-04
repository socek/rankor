FROM python:3.6

RUN useradd -U user

ENV PYTHONUNBUFFERED 1
ENV APP_DIR /code
WORKDIR $APP_DIR
RUN mkdir -p /cashflow.egg-info && ln -s ../cashflow.egg-info cashflow.egg-info

COPY code/requirements.txt $APP_DIR
RUN pip install -r requirements.txt --no-cache-dir

COPY --chown=user:user code $APP_DIR
RUN python setup.py develop

ARG IS_DEV
ENV IS_DEV=$IS_DEV
RUN ./scripts/install_dev

CMD ./entrypoint.sh

USER user
EXPOSE 8000

