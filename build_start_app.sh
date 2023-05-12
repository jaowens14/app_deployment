docker build --tag test_app test_app/
docker build --tag nginx nginx/

docker network create app-net

docker run --net app-net --name test_app --hostname test_app -d -p 8502:8502 test_app
docker run --net app-net --name nginx --hostname nginx -d -p 8000:8000 nginx
