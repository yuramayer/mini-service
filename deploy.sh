#!/bin/bash
git pull
docker-compose pull
docker-compose up --build -d
