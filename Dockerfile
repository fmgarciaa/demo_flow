# Use a base Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Command to execute the ETL process
CMD ["python", "main.py"]
