docker build --tag test_app test_app/
docker build --tag nginx nginx/

docker run -d -p 8000:8502 test_app
docker run -d -p 9000:8502 nginx