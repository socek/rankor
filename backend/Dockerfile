FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV APP_DIR /code
WORKDIR $APP_DIR
RUN mkdir -p /project.egg-info && ln -s /project.egg-info sapp.egg-info

COPY code/requirements.txt $APP_DIR
RUN pip install -r requirements.txt --no-cache-dir

COPY code $APP_DIR
RUN python setup.py develop

CMD ./entrypoint.sh

EXPOSE 8000

