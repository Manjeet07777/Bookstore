Bookstore Application

A simple Bookstore web application built using Django, Python, HTML, and CSS. The app uses SQLite as the database, implements CSRF protection, and is containerized with Docker. Continuous deployment is set up using GitHub Actions, and the application is hosted on AWS EC2.

Features

View available books and search by title

Add new books to the inventory

User authentication and authorization

CSRF protection for secure forms

Fully containerized with Docker

Automated CI/CD using GitHub Actions

Hosted on AWS EC2

(Optional) Free domain and SSL support

Tech Stack

Backend: Python, Django

Frontend: HTML, CSS

Database: SQLite

Containerization: Docker

CI/CD: GitHub Actions

Hosting: AWS EC2

Domain & SSL: InfinityFree / Freenom (optional)

Getting Started
1. Clone the repository
git clone https://github.com/Manjeet07777/Bookstore.git
cd Bookstore

2. Build Docker image
docker build -t bookstore-app:latest .

3. Run Docker container locally
docker run -d --name bookstore -p 8000:8000 bookstore-app:latest


Open your browser at http://localhost:8000.

Deployment

This project uses GitHub Actions for CI/CD:

Push changes to the main branch

GitHub Actions builds the Docker image and pushes it to Docker Hub

EC2 instance pulls the latest image and runs the container

Make sure to configure GitHub Secrets:

DOCKER_HUB_USERNAME

DOCKER_HUB_ACCESS_TOKEN

EC2_HOST

EC2_USER

EC2_KEY

AWS EC2 Setup

Launch an EC2 instance (Ubuntu recommended)

Install Docker:

sudo apt update
sudo apt install docker.io -y
sudo systemctl enable --now docker
sudo usermod -aG docker $USER


Pull and run the Docker image:

docker pull manjeet271199/bookstore-app:latest
docker run -d --name bookstore -p 80:8000 manjeet271199/bookstore-app:latest


Optional: Configure domain and SSL via InfinityFree / Freenom and Route 53.

Directory Structure
Bookstore/
│
├── store/                 # Django app
│   ├── templates/
│   ├── static/
│   └── models.py, views.py, etc.
├── Bookstore/             # Project settings
│   └── settings.py
├── Dockerfile             # Docker image configuration
├── requirements.txt       # Python dependencies
└── .github/workflows/     # GitHub Actions CI/CD
    └── main.yml

Notes

The app is containerized to simplify deployment and scalability.

CI/CD automates build and deploy, ensuring the latest version runs on EC2.

Domain and SSL can be configured later for production readiness.

Author

Manjeet Singh
GitHub-https://github.com/Manjeet07777
LinkedIn-https://www.linkedin.com/in/manjeetsingh2001/
