FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3 python3-pip libgl1-mesa-glx libxml2 


COPY ./* /opt/
RUN pip3 install ibm_db


CMD python3 /opt/connector.py
