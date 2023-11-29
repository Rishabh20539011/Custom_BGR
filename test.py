# Use a Node.js base image
FROM node:latest

# Install Supervisor
RUN apt-get update && apt-get install -y supervisor

# Supervisor configuration
COPY supervisord_frontend.conf /etc/supervisor/conf.d/supervisord.conf

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Start Supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]




[supervisord]
nodaemon=true

[program:frontend]
command=node app.js
directory=/usr/src/app
autorestart=true




# Use a Python base image
FROM python:latest

# Install Supervisor
RUN apt-get update && apt-get install -y supervisor

# Supervisor configuration
COPY supervisord_backend.conf /etc/supervisor/conf.d/supervisord.conf

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Start Supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]



[supervisord]
nodaemon=true

[program:backend]
command=uvicorn main:app --host 0.0.0.0 --port 8000
directory=/usr/src/app
autorestart=true



# For frontend
docker build -f Dockerfile.frontend -t myfrontend .
docker run -d -p 3000:3000 myfrontend

# For backend
docker build -f Dockerfile.backend -t mybackend .
docker run -d -p 8000:8000 mybackend












# [supervisord]
# nodaemon=true
# logfile=/var/log/supervisor/supervisord.log
# logfile_maxbytes=50MB
# logfile_backups=10
# loglevel=info

# [program:backend]
# command=uvicorn main:app --host 0.0.0.0 --port 8000
# directory=/usr/src/app
# autostart=true
# autorestart=true
# stderr_logfile=/var/log/supervisor/backend.err.log
# stdout_logfile=/var/log/supervisor/backend.out.log
# priority=1

# [program:frontend]
# command=node app.js
# directory=/usr/src/app
# autostart=true
# autorestart=true
# stderr_logfile=/var/log/supervisor/frontend.err.log
# stdout_logfile=/var/log/supervisor/frontend.out.log
# priority=2
