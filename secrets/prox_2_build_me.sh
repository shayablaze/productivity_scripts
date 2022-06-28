docker build . -t second_prox_thing
docker run --network="host" second_prox_thing