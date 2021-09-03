# Pull base image
FROM python:3.9

WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000