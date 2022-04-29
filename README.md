# Chat

## Overview

This uses `docker-compose` to create a small network of containers:

```
    |--> chat-node-1 (UDP Chat)
    |
    |--> chat-node-2 (UDP Chat)
           .
           .
           .
    |--> chat-node-X (UDP Chat)
```

Each container runs a UDP chat application.

## Build

To launch, just open a terminal, go to the same level with
'docker-compose.yml', and execute:

`docker-compose up -d --scale node=X`

Where 'X' is the number of chat nodes wanted - 2 is recommended at
least.

This will spin up the Docker architecture.

### Test

Login to each container:

`docker exec -it chat-node-X /bin/sh`

And run in each container:

`./chatapp.py`

You will be prompted for the remote to chat with.  In a 2-node exmample, 
the nodes will be named:

```
chat-node-1
chat-node-2
```

Enter "chat-node-2" in the prompt on 'chat-node-1' and vice versa.  Begin 
chatting.

### Cleanup

To quit (`CTRL+C` in the terminal if not called with `-d` option)

`docker-compose down`
