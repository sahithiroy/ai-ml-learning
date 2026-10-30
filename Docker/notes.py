'''
What is Docker? Why do we use it?
Docker is a platform that allows us to package an application along with all its dependencies into a container so that it can run consistently on any machine.

In simple words, Docker ensures that an application works the same way on your laptop, another developer's laptop, a testing server, or a production server.

Let's understand it with an example.
1. Why do we need Docker?
Imagine you developed a Python Machine Learning application.

Your application requires:
- Python 3.12
- Pandas
- NumPy
- Scikit-learn
- MLflow
- MySQL
You developed everything on your laptop, and it works perfectly.

Now, you send your application to another developer or deploy it on a server.

But they encounter errors:
- Their Python version is different.
- They have different library versions.
- Some dependencies are missing.
- Environment configurations are different.
You might hear:

"But it works on my machine!"

This is one of the main problems Docker solves.

Docker packages your application, Python version, libraries, dependencies, and configurations into a container.







medium.com


Now the application can run consistently across different environments.
2. What are the main concepts in Docker?
There are four important concepts you should understand.









1. Docker

A platform used to build, run, and manage containers.












2. Docker Image

A blueprint or template containing everything required to run an application.

Example: Python 3.12 + application code + required libraries.












3. Docker Container

A running instance of a Docker image.

Example: Your Python ML application running inside a container.












4. Dockerfile

A text file containing instructions to build a Docker image.



Understand the relationship
Dockerfile

Instructions to build the application environment

Docker Image

Application + dependencies + environment

Docker Container

Running application


3. How do we use Docker? Practical example
Let's say you have a Python application.

Step 1: Create a Python file

app.py
import pandas as pddata = {    "Name": ["John", "Alice", "Bob"],    "Age": [25, 30, 35]}df = pd.DataFrame(data)print(df)



Step 2: Create a requirements.txt file
pandas==2.2.3


This file contains the Python libraries required by your application.

Step 3: Create a Dockerfile

Create a file named Dockerfile (without an extension).
# Use Python base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY app.py .

# Execute application
CMD ["python", "app.py"]


Step 4: Build a Docker image

Open your terminal in the project directory.
docker build -t my-python-app .


Here:
- docker build → Builds an image.
- -t → Assigns a name to the image.
- my-python-app → Image name.
- . → Current directory.
Step 5: Run the Docker container
docker run my-python-app


Your Python application executes inside the Docker container.

That's it!
4. When do we use Docker in real-world projects?
Docker is widely used in software development, Data Science, Machine Learning, and deployment.

Here are some practical examples:
Scenario	Why Docker is useful
Python applications	Maintain consistent Python environments
Machine Learning	Package ML models and dependencies
MLflow	Run MLflow tracking servers consistently
MySQL	Run databases without manually installing them
FastAPI	Deploy APIs in containers
Microservices	Run different services independently
Cloud deployment	Deploy applications consistently

5. How Docker helps in a Machine Learning project
Let's take a Machine Learning project as an example.

Suppose you developed a model to predict solar power generation.

Your architecture might look like this:







github.com


You might have:
1. MLflow container: Tracks experiments and stores model information.
2. MySQL container: Stores experiment metadata.
3. FastAPI container: Exposes your ML model through REST APIs.
4. Model container: Runs your prediction application.
Each component can run in its own container.

You can use Docker Compose to manage multiple containers together.

For example:
services:
  mysql:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: example
    ports:
      - "3306:3306"

  mlflow:
    image: python:3.12
    ports:
      - "5000:5000"


You can start the services using:
docker compose up -d


This starts the configured services.

Note: This is a simplified example; a complete MLflow setup also needs MLflow installation, server configuration, and persistent storage.
6. Important Docker commands
Command	Purpose
docker --version	Check Docker version
docker images	List available images
docker ps	List running containers
docker ps -a	List all containers
docker build -t app .	Build an image
docker run app	Run a container
docker stop container_id	Stop a container
docker start container_id	Start a stopped container
docker rm container_id	Remove a container
docker rmi image_name	Remove an image


7. Docker vs Virtual Machine
You might wonder: Why do we need Docker when virtual machines already exist?









Virtual Machine
- Includes a complete guest OS.
- Uses more resources.
- Generally takes longer to start.










Docker Container
- Shares the host OS kernel.
- Generally lightweight.
- Starts quickly.


8. What should you remember?
- Docker: Platform for containerization.
- Dockerfile: Instructions for creating an image.
- Docker Image: Blueprint of an application.
- Docker Container: Running application created from an image.
- Docker Compose: Tool to manage multiple containers.
The main purpose of Docker is to make applications portable, consistent, isolated, and easier to deploy.




















Excellent question! This is one of the main reasons we use Docker. You can build your application on Laptop 1 and run the exact same application on Laptop 2 without manually installing all the Python dependencies.

There are two ways to transfer your Docker application to another laptop.
1. Understand the workflow
Imagine:
- Laptop 1: You develop your Python application and build a Docker image.
- Laptop 2: Another developer wants to run the same application.
Laptop 1
Development machine
Python project

app.py + requirements.txt + Dockerfile

Docker build

docker build -t my-python-app .

Docker Image

my-python-app



Transfer image

Docker Hub or save as a TAR file
Laptop 2
Docker Image

my-python-app

docker run my-python-app

Application runs!



2. Method 1: Using Docker Hub (recommended)
Docker Hub is an online repository where you can store and share Docker images.







wiz.io


Laptop 1: Build and upload the image
Step 1. Build your image
docker build -t my-python-app .


Step 2. Login to Docker Hub

Create a Docker Hub account at Docker Hub.

Then execute:
docker login


Step 3. Tag your image

Replace yourusername with your Docker Hub username.
docker tag my-python-app yourusername/my-python-app:v1


Step 4. Push your image
docker push yourusername/my-python-app:v1


Now your image is uploaded to Docker Hub.
Laptop 2: Download and run the image
Install Docker Desktop on Laptop 2 and make sure Docker is running.

Step 1. Download the image
docker pull yourusername/my-python-app:v1


Step 2. Run the application
docker run yourusername/my-python-app:v1


That's it! Your application runs on Laptop 2.

You don't need to manually install Python, Pandas, or other dependencies on Laptop 2. Docker provides the environment packaged in the image.

Note: Docker itself must be installed, and the image must be compatible with the second laptop's CPU architecture.

3. Method 2: Save Docker image as a TAR file
Suppose you don't have internet access or don't want to use Docker Hub.

You can save your image as a file and transfer it using a USB drive.
Laptop 1
Step 1. Build your image
docker build -t my-python-app .


Step 2. Save the image
docker save -o my-python-app.tar my-python-app


This creates:
my-python-app.tar


Copy this file to a USB drive.
Laptop 2
Step 1. Copy the TAR file to Laptop 2.

Step 2. Load the image into Docker
docker load -i my-python-app.tar


Step 3. Run the application
docker run my-python-app


No need to rebuild the image!

4. Docker Hub vs TAR file
Feature	Docker Hub	TAR file
Internet required	Yes, for transfer	No
Sharing	Online	USB/file transfer
Upload/download	Push and pull	Save and load
Multiple developers	Easy	Manual
Best use	Team projects	Offline transfer

5. One important concept: Image vs Project
There is a difference between transferring a Docker image and transferring your project source code.
Docker Image	Project Source Code
Contains application and dependencies	Contains your Python files and Dockerfile
Used to run the application	Used to modify the application
Does not normally include editable source files outside the image	Editable by developers

If Laptop 2 only needs to run your application, transfer the image















his is a very important Docker concept. Once you understand this, you'll understand why companies use multiple Docker containers in real-world applications instead of putting everything into one container.

Your question is:

Why can't we put Python, Machine Learning, MLflow, MySQL, FastAPI, and everything else into one Docker container? Why do we create separate containers?

The answer is: We can put everything into one container, but separating services into different containers makes applications easier to manage, scale, maintain, deploy, and troubleshoot.

Let's understand this with a real-world example.
1. Can we put everything into one container?
Yes!

Imagine you are building a Machine Learning application.

Your project requires:
- Python for application logic.
- Pandas and Scikit-learn for data processing and ML.
- FastAPI to expose prediction APIs.
- MLflow to track experiments.
- MySQL to store experiment metadata.
You could install all these components in one Docker image and run them inside one container.
Approach 1: Everything in one container
One Docker container
Combined services

Python application

Pandas + Scikit-learn

FastAPI server

MLflow server

MySQL database


All services share the same container lifecycle and environment.

It can work, but it creates several problems.
Problems with one container
1. Scaling becomes difficult

Suppose your FastAPI application receives 10,000 prediction requests, but MySQL only needs to handle a normal amount of database traffic.

You want to increase FastAPI instances without creating unnecessary MySQL instances.

If everything is in one container, scaling becomes difficult.

2. Different dependencies can conflict

Imagine:
- Application A requires Python 3.10.
- Application B requires Python 3.12.
- Another service requires a different version of a library.
Putting everything into one environment can create dependency conflicts.

3. Failure of one service affects the whole container

Suppose MySQL crashes.

If all services are running together, managing the failure and restarting only MySQL becomes difficult.

4. Deployment becomes complicated

Suppose you update only your FastAPI code.

You don't want to rebuild and redeploy your entire MySQL and MLflow setup unnecessarily.

5. Resource management becomes difficult

You may want:
- More CPU for ML inference.
- More memory for MySQL.
- Different resource limits for MLflow.
Separate containers give you more flexibility.

2. Approach 2: Separate containers
Instead of putting everything into one container, we create different containers for different services.
Multiple Docker containers
Container 1
Python + FastAPI

Processes incoming API requests and makes predictions

Container 2
MLflow

Tracks experiments, parameters, metrics and models

Container 3
MySQL

Stores relational database records and metadata

Container 4
ML training worker

Trains models independently when needed

Docker network

Containers communicate with each other


Notice something important:

Each container has its own responsibility.

This is called the single responsibility principle in application architecture: give each service a clearly defined job.

It doesn't mean every Python library needs its own container. Pandas, NumPy and Scikit-learn can all be installed together in your Python application container.
3. What are the actual advantages of separate containers?
Let's understand through practical situations.
Reason	Real-world example
Independent scaling	Increase FastAPI containers from 2 to 5 without scaling MySQL
Independent deployment	Update FastAPI without rebuilding MySQL
Isolation	MySQL and Python have separate environments
Fault isolation	Restart a failed API without restarting the database
Resource management	Give ML training more memory and CPU
Reusability	Multiple applications can connect to the same MySQL service
Maintenance	Upgrade MySQL without rebuilding the Python application

One important point: containers are isolated processes, not separate physical computers. They can communicate through a Docker network.
4. How do we create multiple containers?
Let's build an actual project using Docker Compose.

We'll use your familiar Python, MLflow and MySQL workflow.

Our architecture:







github.com


Step 1. Create the project structure
Docker/
│
└── ml-project/
    │
    ├── app/
    │   ├── main.py
    │   ├── requirements.txt
    │   └── Dockerfile
    │
    ├── docker-compose.yml
    └── .env


Step 2. Create the Python application
app/main.py
from fastapi import FastAPIimport mysql.connectorapp = FastAPI()@app.get("/")def home():    return {"message": "Docker application running"}@app.get("/insert")def insert_data():    connection = mysql.connector.connect(        host="mysql",        user="root",        password="root123",        database="ml_database"    )    cursor = connection.cursor()    cursor.execute("""        CREATE TABLE IF NOT EXISTS predictions (            id INT AUTO_INCREMENT PRIMARY KEY,            prediction FLOAT        )    """)    cursor.execute(        "INSERT INTO predictions (prediction) VALUES (%s)",        (250.5,)    )    connection.commit()    cursor.close()    connection.close()    return {"message": "Data inserted into MySQL"}



Notice:
host="mysql"



This is the MySQL service name in Docker Compose.
Step 3. Create requirements.txt
fastapi
uvicorn
mysql-connector-python


Step 4. Create Dockerfile
Inside the app folder:
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


This Dockerfile creates an image for your Python/FastAPI application.
Step 5. Create docker-compose.yml
This is where we define multiple containers.
services:

  # Container 1: MySQL
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root123
      MYSQL_DATABASE: ml_database
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  # Container 2: Python + FastAPI
  fastapi:
    build: ./app
    ports:
      - "8000:8000"
    depends_on:
      - mysql

volumes:
  mysql_data:


Notice that we haven't created two Dockerfiles.

We use:
- An existing MySQL image from Docker Hub.
- Our own Dockerfile to build the FastAPI application.
Docker Compose creates a network automatically, allowing both services to communicate using their service names.
Step 6. Start both containers
Open PowerShell inside the ml-project directory.

Execute:
docker compose up --build -d


What happens?
1. Docker downloads the MySQL image if needed.
2. Docker builds your FastAPI image.
3. Docker creates a network.
4. Docker creates the MySQL container.
5. Docker creates the FastAPI container.
Check the running containers:
docker ps


You should see two containers.
Container	Responsibility
MySQL	Database
FastAPI	Python application and API

For a reliable production setup, configure a MySQL health check and make FastAPI wait until MySQL is ready before accepting database requests.
Step 7. Test the application
Open your browser:
http://localhost:8000/Expected response:
{
    "message": "Docker application running"
}


Now open:
http://localhost:8000/insertExpected response:
{
    "message": "Data inserted into MySQL"
}


You have now used two separate containers to run one application!
Step 8. Verify MySQL data
Execute:
docker exec -it <mysql_container_name> mysql -uroot -p


Then:
USE ml_database;

SELECT * FROM predictions;


You should see the inserted prediction.

5. How do we scale individual containers?
This is one of the biggest advantages.

Suppose your application receives more prediction requests.

You can increase the number of FastAPI containers:
docker compose up -d --scale fastapi=3


Now you can run three FastAPI instances instead of one, while keeping MySQL as one service.







brianchristner.io


In production, you would also configure a load balancer to distribute requests among the API instances.

Note: With this particular Compose example, the fixed host port mapping must be adjusted or replaced by a reverse proxy/load balancer before running multiple FastAPI replicas.
6. Should every component have a separate container?
No! This is an important distinction.

You should separate services, not individual libraries.

For example:
Component	Separate container?	Reason
Python	No, usually part of application container	Runtime
Pandas	No	Python library
NumPy	No	Python library
Scikit-learn	No	Python library
FastAPI	Usually with Python application	API service
MLflow tracking server	Yes, often	Independent tracking service
MySQL	Yes, often	Database service
Redis	Yes, often	Caching service
Model training worker	Often	Independent compute workload

For example, your Python application can contain Python, Pandas, NumPy, Scikit-learn, and FastAPI together.

But MySQL can run separately because it has its own database lifecycle, storage requirements, and resource needs.
7. Useful Docker commands for managing multiple containers
Command	Purpose
docker compose up -d	Start all services
docker compose down	Stop and remove containers and network
docker compose ps	View services
docker compose logs	View logs
docker compose logs -f fastapi	View FastAPI logs
docker compose restart mysql	Restart MySQL
docker compose build	Build application images
docker compose exec mysql mysql -uroot -p	Open MySQL CLI

Remember: docker compose down does not remove named volumes by default. Your MySQL data remains in its volume.
8. When should you use one container versus multiple containers?
Use one container when:
- You have a simple Python script.
- You are building a small standalone application.
- All components share the same lifecycle.
- You don't need independent scaling or deployment.
Use multiple containers when:
- You have a Python application and a database.
- You have FastAPI and MLflow.
- You have multiple microservices.
- Different services require different environments.
- You need independent scaling and deployment.

For larger applications, teams often use Kubernetes to orchestrate containers across multiple machines. Docker Compose is an excellent starting point for learning multi-container applications on your laptop.

9. What I recommend you learn next
Since you're learning Docker alongside Python, MLflow and MySQL, follow this order:
1. Docker fundamentals
   
   Images, containers, Dockerfiles and volumes.
2. Docker networking
   
   How Python connects to MySQL using container service names.
3. Docker Compose
   
   Running Python, MySQL and MLflow together.
4. Container scaling
   
   Running multiple API instances.
5. Cloud deployment
   
   Deploying your containerized application to AWS.
One concept to remember throughout your Docker learning:

A project can have one application but multiple services. Each service can run in its own container, and Docker Compose brings all those containers together to work as one system.

This is the architecture you'll frequently encounter in real-world MLflow, MySQL, FastAPI and machine learning deployment projects.'''