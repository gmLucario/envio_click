#!/bin/bash
docker-compose \
 -f docker-compose.yml \
kill $@
docker-compose \
 -f docker-compose.yml \
down $@