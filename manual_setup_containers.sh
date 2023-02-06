# ----DATABASE---- #
docker build -t shop_db ./database/
# docker container run -p 127.0.0.1:3306:3306 -d --name shop_db -e MYSQL_ROOT_PASSWORD=1234 shop_db

# ----BACKEND---- #
docker build -t shop_backend ./backend
# docker container run -p 127.0.0.2:5000:5000 -d --name shop_backend shop_backend

docker compose up
