FROM node:8.1.3
RUN mkdir -p /code
RUN mkdir -p /data/node_modules
ENV PATH="/data/node_modules/.bin:${PATH}"

WORKDIR /code
RUN apt-get update && apt-get install apt-transport-https
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install yarn

RUN ln -s /data/node_modules
ADD code/package.json .
RUN yarn install -g
