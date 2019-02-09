#!/bin/sh

docker-compose up -d
docker-compose exec runner bash -c "cd /root/build/tests &&\
                                    ansible-playbook test.yml --syntax-check &&\
                                    ansible-playbook test.yml &&\
                                    py.test -v test.py --hosts="docker://localhost""
docker rm -f localhost
docker-compose down
# docker-compose up -d && docker-compose exec runner bash -c "cd /root/build/tests && ansible-playbook test.yml" && docker-compose down && docker exec -it localhost bash
