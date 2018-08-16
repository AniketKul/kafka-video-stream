FROM ubuntu:xenial

RUN apt-get update
RUN apt-get install -y ca-certificates
RUN apt-get install -y libssl-dev

RUN apt-get install -y python3
RUN apt-get install -y python3-pip python-dev build-essential
RUN mkdir -p /opt/exampleapp
COPY . /opt/exampleapp/
#RUN chmod +x /opt/exampleapp/producer.py
#RUN chmod +x /opt/exampleapp/consumer.py
RUN pip3 install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org -r /opt/exampleapp/requirements.txt

#ENTRYPOINT ["python3"]
#CMD ["/opt/exampleapp/producer.py"]
