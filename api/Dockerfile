# Use an official Python runtime as a parent image
FROM python:3-slim-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5500 available to the world outside this container; 5000 is used AirPlay!!
EXPOSE 5500

# Run app.py when the container launches
CMD ["python", "run.py"]