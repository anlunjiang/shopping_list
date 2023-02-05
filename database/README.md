# Shopping List Database Service

The Shopping List Database Service hosts the mysql db that will hold the list of items.

It will also hold various other persistent data required by future features and iterations


## Deployment
```bash
 docker build -t shop_db .
 docker image list
 docker container run -p 127.0.0.1:3306:3306 -d --name shop_db -e MYSQL_ROOT_PASSWORD=1234 shop_db
 # user and db created at db init in dockerfile
 
 # Login to SQL
 docker exec -it shop_db /bin/bash
 mysql -h 127.0.0.1 -P 3306 -u root -p1234
```
