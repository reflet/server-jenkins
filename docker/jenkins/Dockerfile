FROM jenkins
USER root

# system update
RUN apt-get -y update && apt-get -y upgrade

# locale
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

# add tools to work.
RUN apt-get install -y vim less

# fabric
RUN apt-get install -y python-pip python-setuptools
RUN pip install setuptools --no-use-wheel --upgrade
RUN pip install fabric
