#!/bin/sh

docker exec -it RC-psql bash -c 'psql -h localhost -U postgres RC'