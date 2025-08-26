@REM create network
docker network create 20news-net

@REM create volume
docker volume create mongo_data

@REM run Kafka
docker run -d --name kafka --hostname kafka --network 20news-net `
  -e KAFKA_CFG_NODE_ID=1 `
  -e KAFKA_CFG_PROCESS_ROLES=broker,controller `
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093 `
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 `
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 `
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER `
  -e KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE=true `
  -p 9092:9092 bitnami/kafka:3.7

@REM  MongoDB
docker run -d --name my_mongo --hostname mongo --network 20news-net `
  -p 27017:27017 -v mongo_data:/data/db mongo:7

@REM build images
docker build -t pub:latest .\pub
docker build -t sub:latest .\sub

@REM run Subscriber
docker run -d --name sub --network 20news-net `
  -e KAFKA_BOOTSTRAP=kafka:9092 `
  -e MONGO_URI=mongodb://mongo:27017 `
  -e MONGO_DB=twenty_news `
  -e COLL_INTERESTING=interesting `
  -e COLL_NOT_INTERESTING=not_interesting `
  -p 8001:8000 sub:latest

#  Publisher
docker run -d --name pub --network 20news-net `
  -e KAFKA_BOOTSTRAP=kafka:9092 `
  -p 8000:8000 pub:latest


Write-Output "curl http://localhost:8000/health"
Write-Output "curl http://localhost:8001/health"