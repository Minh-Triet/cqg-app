FROM image-registry.openshift-image-registry.svc:5000/openshift/python:latest
EXPOSE 5000
COPY . /app
WORKDIR /app
USER 0
#RUN chgrp -R 0 temp && \
#    chmod -R g=u temp
RUN /opt/app-root/bin/python3.9 -m pip install --upgrade pip
RUN pip install quickfix-1.15.1-cp39-cp39-linux_x86_64.whl
# Install GCC 11 from the Red Hat Developer Toolset
RUN yum install -y centos-release-scl-rh && \
yum-config-manager --enable rhel-server-rhscl-8-rpms && \
yum install -y devtoolset-11-gcc devtoolset-11-gcc-c++

# Enable GCC 11 for the rest of the commands
ENV PATH=/opt/rh/devtoolset-11/root/usr/bin:$PATH

# Copy your application code to the /opt/app-root/src directory
COPY . /opt/app-root/src
##RUN yum install yum-utils
##RUN yum config-manager --enable ubi-8-appstream-rpms
#RUN sudo yum module install -y python39/build
#RUN sudo yum update -y
#RUN sudo yum -y install libc6 libc6-dev libc6-dbg
##RUN pip install quickfix
##RUN apt-get -y install software-properties-common
##RUN apt-add-repository -yu 'deb http://ftp.debian.org/debian sid main'
##RUN apt-get update

#RUN yum install -y gcc
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org

ENV FLASK_APP /app/app.py
#RUN flask db migrate
#RUN flask db upgrade
CMD ["flask", "run", "--host", "0.0.0.0"]



