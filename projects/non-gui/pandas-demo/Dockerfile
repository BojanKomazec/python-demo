# Use the official Python image from the Docker Hub
FROM python:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY ./requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#
# Copying the project's source code and setting the CMD is NOT necessary if
# we're mounting the volume and set command attribute in docker-compose.yaml.
#

# Copy the rest of your application code into the container
# We do this after installing dependencies because this layer will be
# changing more frequently.
# COPY . .

# Specify the command to run your script
# CMD ["python", "main.py"]
