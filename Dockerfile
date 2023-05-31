FROM python:3.9.7
EXPOSE 5000
COPY . /app
WORKDIR /app

RUN chgrp -R 0 logs && \
    chmod -R g=u logs
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install quickfix-1.15.1-cp39-cp39-linux_x86_64.whl
#RUN echo "deb http://ftp.debian.org/debian sid main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN apt-add-repository -yu 'deb http://ftp.debian.org/debian sid main'
RUN apt-get update
RUN apt-get -t sid -y install libc6 libc6-dev libc6-dbg
RUN apt install -y gcc
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org

ENV FLASK_APP /app/app.py
#RUN flask db migrate
#RUN flask db upgrade
CMD ["flask", "run", "--host", "0.0.0.0"]


