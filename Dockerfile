# Use a base image with Python 3.12.3
FROM python:3.12.3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port that Django runs on
EXPOSE 8000

# Run database migrations and create a superuser automatically
CMD ["sh", "-c", "python manage.py migrate && \
    echo \"from django.contrib.auth.models import User; \"\
    \"User.objects.filter(username='admin').exists() or \"\
    \"User.objects.create_superuser('admin', 'admin@example.com', 'admin')\" | python manage.py shell && \
    python manage.py runserver 0.0.0.0:8000"]
