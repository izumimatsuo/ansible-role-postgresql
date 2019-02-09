FROM williamyeh/ansible:centos7

RUN yum update -y && yum install -y docker git
RUN pip install -U pip setuptools && pip install docker-py testinfra

WORKDIR /root
CMD ["/bin/bash"]
