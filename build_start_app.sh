docker build --tag test_app test_app/
docker build --tag nginx nginx/

docker network create app-net

docker run --net app-net --name test_app -d test_app
docker run --net app-net --name nginx -d -p 80:80 nginx