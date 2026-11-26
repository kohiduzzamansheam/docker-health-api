# Docker Health API

A containerized Python REST API that provides application health status and real-time system resource metrics using Flask, Docker, and `psutil`.

## 1. Project Overview

Docker Health API exposes HTTP endpoints to monitor the application and collect system-level information from its runtime environment.

The API provides:

- Application information, including hostname, environment, and Python version.
- Application health status.
- CPU usage and logical processor count.
- Memory usage, available memory, and total memory.
- Disk usage, available space, and total disk capacity.
- System uptime information.

The application is packaged into a Docker image and runs inside an isolated container.

## 2. Technologies

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | REST API framework |
| psutil | Collecting system resource metrics |
| Docker | Containerization |
| Docker Compose | Not currently used |

## 3. Project Structure

```text
docker-health-api/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

| File | Description |
|---|---|
| `app.py` | Implements the Flask API and system monitoring endpoints. |
| `requirements.txt` | Defines the Python dependencies. |
| `Dockerfile` | Contains instructions for building the Docker image. |
| `.dockerignore` | Excludes unnecessary files from the Docker build context. |
| `.gitignore` | Prevents unnecessary files from being tracked by Git. |

## 4. API Endpoints

### `GET /`

Returns basic application information.

**Example response:**

```json
{
  "service": "Docker Health API",
  "hostname": "container-hostname",
  "environment": "containerized",
  "python_version": "3.x.x"
}
```

### `GET /health`

Checks whether the API application is responding.

**Example response:**

```json
{
  "status": "healthy"
}
```

Returns HTTP status code `200` when the endpoint responds successfully.

### `GET /system`

Collects system resource information using the `psutil` Python library.

**Metrics include:**

| Metric | Description |
|---|---|
| CPU usage | Current CPU utilization percentage |
| Logical cores | Number of logical CPU processors |
| Total memory | Total detected memory |
| Used memory | Memory currently in use |
| Available memory | Memory available for use |
| Memory usage | Memory utilization percentage |
| Total disk | Total capacity of the inspected filesystem |
| Used disk | Used filesystem space |
| Free disk | Available filesystem space |
| Disk usage | Filesystem utilization percentage |
| Uptime | Time since the detected system boot |

**Example response structure:**

```json
{
  "hostname": "container-hostname",
  "cpu": {
    "usage_percent": 12.5,
    "logical_cores": 4
  },
  "memory": {
    "total_mb": 4096.0,
    "used_mb": 2048.0,
    "available_mb": 2048.0,
    "usage_percent": 50.0
  },
  "disk": {
    "total_gb": 20.0,
    "used_gb": 8.0,
    "free_gb": 12.0,
    "usage_percent": 40.0
  },
  "uptime_seconds": 3600
}
```

*Note: The values above are illustrative. Actual values are collected at runtime and depend on the environment visible to the container.*

## 5. Docker Configuration

### Dockerfile

```dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

**Key configurations:**

- `FROM`: Uses the lightweight Python 3.13 slim image as the base image.
- `ENV PYTHONDONTWRITEBYTECODE=1`: Prevents Python from generating `.pyc` files.
- `ENV PYTHONUNBUFFERED=1`: Sends Python output directly to the container logs.
- `WORKDIR`: Sets `/app` as the working directory.
- `COPY`: Copies application files into the image.
- `RUN`: Installs the required Python dependencies.
- `EXPOSE 5000`: Documents the port used by the application.
- `CMD`: Starts the Flask application when the container runs.

### Dependencies

`requirements.txt`:

```text
Flask==3.1.2
psutil
```

`Flask` provides the API framework, while `psutil` collects system resource information.

## 6. Build and Run

### Prerequisites

- Docker Desktop or Docker Engine
- Git
- Python 3.13 or compatible Python environment for local development

### Step 1: Clone the repository

```bash
git clone https://github.com/kohiduzzamansheam/docker-health-api.git

cd docker-health-api
```

### Step 2: Build the Docker image

```bash
docker build -t status-api:1.1 .
```

This builds the application image using the instructions in the Dockerfile.

### Step 3: Run the container

```bash
docker run -d \
  --name status-api \
  -p 8080:5000 \
  -e APP_ENV=containerized \
  status-api:1.1
```

**Container configuration:**

| Option | Purpose |
|---|---|
| `-d` | Runs the container in the background. |
| `--name` | Assigns the container the name `status-api`. |
| `-p 8080:5000` | Maps host port 8080 to container port 5000. |
| `-e APP_ENV=containerized` | Sets the application environment variable. |

The API is now accessible at:

```text
http://localhost:8080
```

## 7. Test the API

Use a browser or `curl` to test the endpoints.

**Application information:**

```bash
curl http://localhost:8080/
```

**Application health:**

```bash
curl http://localhost:8080/health
```

**System resource metrics:**

```bash
curl http://localhost:8080/system
```

## 8. Container Management

**List running containers:**

```bash
docker ps
```

**View application logs:**

```bash
docker logs status-api
```

**Follow application logs:**

```bash
docker logs -f status-api
```

**Stop the container:**

```bash
docker stop status-api
```

**Remove the container:**

```bash
docker rm status-api
```

**List locally available images:**

```bash
docker images
```

## 9. Learning Outcomes

Through this project, I practised:

- Developing REST API endpoints using Flask.
- Collecting system resource metrics using Python and `psutil`.
- Creating Docker images using a Dockerfile.
- Running and managing containers.
- Mapping host ports to container ports.
- Configuring containers through environment variables.
- Inspecting container logs and testing API endpoints.