FROM ubuntu:16.04
MAINTAINER graboskyc

ENV PORT=22
ENV CONTAINER_SHELL=bash
ENV CONTAINER=

# Install all packages
RUN apt-get clean && apt-get update && apt-get install -y git whois python2.7 openssh-server vim
RUN ln /usr/bin/python2.7 /usr/bin/python
RUN apt-get install -y python-pip

# download extra files
RUN rm -rf /opt/BasicCloudShellRobot
RUN git clone https://github.com/graboskyc/BasicCloudShellRobot.git /opt/BasicCloudShellRobot
RUN chmod +w /opt/BasicCloudShellRobot/CES/*
RUN chmod +w /opt/BasicCloudShellRobot/Robot/*

# configure SSH server
RUN rm -rf /etc/ssh/ssh*key
RUN dpkg-reconfigure openssh-server
RUN yes | ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ""
RUN yes | ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ""
RUN mv -f /opt/BasicCloudShellRobot/sshd_config /etc/ssh/
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN service ssh start

# add a quali user for debug
RUN useradd qualisystems -d /opt/BasicCloudShellRobot -M -s /bin/bash -p `mkpasswd Password1`

# configure robot and Quali Libraries
RUN pip install robotframework
RUN pip install requests
RUN pip install cloudshell-automation-api

# run container
CMD service ssh start;/usr/bin/python /opt/BasicCloudShellRobot/CES/ces.py register;/usr/bin/python /opt/BasicCloudShellRobot/CES/ces.py;bash
EXPOSE 22
