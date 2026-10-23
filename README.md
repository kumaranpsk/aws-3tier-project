cat > README.md <<'EOF'
# AWS Employee Management Application

A beginner-friendly cloud deployment project built with Python Flask and hosted on an AWS EC2 Ubuntu instance.

## Project Status

**In progress** — the web and application components are deployed. PostgreSQL integration and further tier separation are planned next.

## Architecture

Browser
   |
   | HTTP
   v
Nginx (Reverse Proxy)
   |
   v
Gunicorn (Application Server)
   |
   v
Flask Application

Currently, these components run on one EC2 instance. This is a learning deployment, not a fully isolated production three-tier architecture.

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Python
- Flask
- Gunicorn
- Nginx
- systemd
- Git and GitHub

## Features

- Employee directory web page
- JSON API endpoint at `/api/employees`
- Health-check endpoint at `/health`
- Gunicorn application server
- Nginx reverse proxy
- systemd service for startup and restart management
