# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Set the working directory to /app
WORKDIR /app

#Copy sample dictionary and input files  
COPY dictionary.txt /app/

COPY input.txt /app/

COPY api.py /app

COPY scrmabled-strings.py /app

#Copy the testing data to run tests 
COPY testing_data /app/testing_data

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the command to execute the Python script
CMD [ "python", "api.py","scrmabled-strings.py","test.py"]

