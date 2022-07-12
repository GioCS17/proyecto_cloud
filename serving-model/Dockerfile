FROM ubuntu:20.04

# Dont use COPY * /app/ , * will lead to lose of folder structure in /app
COPY . /app/

# Change WORKDIR
WORKDIR /app

RUN apt-get update && yes | apt-get upgrade
RUN apt-get install -y git python3-pip

# Install dependencies
# use --proxy http://<proxy host>:port if you have proxy
RUN pip3 install -r requirements.txt

# In Docker, the containers themselves can have applications running on ports. To access these applications, we need to expose the containers internal port and bind the exposed port to a specified port on the host.
# Expose port and run the application when the container is started
EXPOSE 9999:9999
ENTRYPOINT python3 server.py 9999
