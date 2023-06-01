FROM image-registry.openshift-image-registry.svc:5000/openshift/python
EXPOSE 5000
COPY . /app
WORKDIR /app
USER 0
#RUN chgrp -R 0 temp && \
#    chmod -R g=u temp
RUN subscription-manager register --username bmt2000gg@gmail.com --password 12345678910 --auto-attach
RUN subscription-manager attach --pool=rhel-8-for-x86_64-appstream-rpms
RUN /opt/app-root/bin/python3.9 -m pip install --upgrade pip
RUN pip install quickfix-1.15.1-cp39-cp39-linux_x86_64.whl
RUN yum install yum-utils
RUN yum config-manager --enable ubi-8-appstream-rpms
RUN yum update -y
RUN yum install gcc-toolset-11
RUN scl enable gcc-toolset-11 gcc
RUN scl enable gcc-toolset-11 g++
RUN scl enable gcc-toolset-11 bash
#RUN apt-get -y install software-properties-common
#RUN apt-add-repository -yu 'deb http://ftp.debian.org/debian sid main'
#RUN apt-get update

#RUN yum install -y gcc
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org

ENV FLASK_APP /app/app.py
#RUN flask db migrate
#RUN flask db upgrade
CMD ["flask", "run", "--host", "0.0.0.0"]


