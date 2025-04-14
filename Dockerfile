# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside the container (Optional if you plan to expose a web service)
EXPOSE 80

# Run dustsentry.py when the container launches
CMD ["python", "./dustsentry.py"]
