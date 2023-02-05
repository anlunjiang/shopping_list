# Backend Flask App

The backend app will host an API layer for the frontend and the database to talk to each other. 

# Deployment
```bash
 docker build -t shop_backend .
 docker image list
 docker container run -p 127.0.0.2:5000:5000 -d --name shop_backend shop_backend

