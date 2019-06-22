# Inherit our image from an official Python 3.6.8 image
FROM python:3.6.8-jessie

# Set the working directory
WORKDIR /app

# Copy the files from Host OS to container's file system
COPY . /app

# Install required pip dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run the entry application when the container launches
CMD ["python3", "src/app.py"]
