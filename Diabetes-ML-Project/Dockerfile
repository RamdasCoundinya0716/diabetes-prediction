# Use an official Python image as a parent image
FROM python:3.10.11

# Set the working directory to /app
WORKDIR /app

# Copy the Flask app files into the container at /app
COPY . /app

# Install Flask and other dependencies using pip
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["python", "flask_app.py"]
