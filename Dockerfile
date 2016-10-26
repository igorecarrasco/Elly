# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:14.04

MAINTAINER Dockerfiles

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && apt-get install -y \
	git \
	python \
	python-dev \
	python-setuptools \
	nginx \
	libpq-dev \
	supervisor \
	libpcre3 \
	libpcre3-dev \
  && rm -rf /var/lib/apt/lists/*

RUN easy_install pip

# install uwsgi now because it takes a little while
RUN pip install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installinig (all your) dependencies when you made a change a line or two in your app. 

COPY ./requirements.txt /home/docker/code/studio3project/
RUN pip install -r /home/docker/code/studio3project/requirements.txt

# add (the rest of) our code
COPY . /home/docker/code/

# RUN python /home/docker/code/studio3project/manage.py migrate --noinput
RUN mkdir /home/docker/code/studio3project/studio3project/static
RUN python /home/docker/code/studio3project/manage.py collectstatic --noinput

EXPOSE 80
CMD ["supervisord","-n"]