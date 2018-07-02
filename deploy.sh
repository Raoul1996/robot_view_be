#!/usr/bin/env bash
git checkout prod
git reset --hard origin/prod
sudo docker-compose stop
sudo docker-compose build
#sudo docker-compose up -d
sudo docker image prune -f && sudo docker container prune -f