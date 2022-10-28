FROM accetto/ubuntu-vnc-xfce-g3:latest-fugo
USER root
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive
RUN DEBIAN_FRONTEND="noninteractive" apt-get install tzdata -y
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# Test OpenGL by running "glxgears"
RUN apt update && apt-get install -y mesa-utils



## Install python3.8.
#RUN apt-get install software-properties-common -y
#RUN add-apt-repository ppa:deadsnakes/ppa -y
#RUN apt-get install python3.8 -y
#
## Make python3.8 the default python.
#RUN rm /usr/bin/python3
#RUN ln -s /usr/bin/python3.8 /usr/bin/python3
#RUN ln -s /usr/bin/python3.8 /usr/bin/python
#RUN apt-get install python3-distutils -y
#
## Install pip.
#RUN wget https://bootstrap.pypa.io/get-pip.py
#RUN python get-pip.py
#RUN rm get-pip.py
#
#
#RUN apt-get install software-properties-common -y
#RUN add-apt-repository ppa:deadsnakes/ppa
#RUN apt-get update && apt-get install -y \
#    python3.8 \
#    python3-pip
#
#
############################################
## Dependencies
############################################
#WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#
#############################################
### Entry point
#############################################
##COPY entrypoint.sh /code/
##RUN chmod +x entrypoint.sh
##ENTRYPOINT ["/code/entrypoint.sh"]
##
##CMD [ "/bin/bash" ]
#
#
## Setup SSH with secure root login
#RUN apt-get update \
# && apt-get install -y openssh-server netcat \
# && mkdir /var/run/sshd \
# && echo 'root:password' | chpasswd \
# && sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
#
#EXPOSE 22
#CMD ["/usr/sbin/sshd", "-D"]
