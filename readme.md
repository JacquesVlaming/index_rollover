docker build -t my-python-app .
docker run -e ES_HOST=<**> -e ES_USER=<**> -e ES_PASSWORD=<**> my-python-app


docker run --env-file .env my-image my-python-app 