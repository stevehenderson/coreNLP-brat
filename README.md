# CoreNLP Server

This project contains:

1. docker commands for running the [Stanford CoreNLP Web Service](https://stanfordnlp.github.io/CoreNLP/corenlp-server.html#docker)
2. docker commands for tunning an API that translates Standford CoreNLP output to brat (see [API](api) subfolder)

An effective tagging workflow requires both service to be running.

### Stanford CoreNLP Web Service

## Start

To start the web service:

```
./start.sh
```

## Usage

You can send wget command using the [CoreNLP Api](https://stanfordnlp.github.io/CoreNLP/corenlp-server.html#api-documentation).

An example is contained in the `test-json.sh` and `test-xml.sh` bash files.

```
./test-json.sh
```

The [corenlp-brat-api](api) accesses this service to create the format needed for brat autotagging.

## Docker Check

To see what's running

```
docker ps
```


To stop all running containers: 
```
docker stop $(docker ps -aq)
```

To remove and refresh the installation: 
```
docker rm $(docker ps -aq)
```

To remove the running coreNLP container:

```
docker stop coreNLP

docker rm coreNLP
```

To remove the brat image:
```
docker rmi [-f] coreNLP
```


