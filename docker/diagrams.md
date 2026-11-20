# Docker: diagrams

## Image vs container: layers

Two containers share the same read-only image layers. Each gets its own thin writable layer.
Overlay filesystem stacks them into one view, which becomes the container's `/`.

```mermaid
flowchart TB
    subgraph IMG["nginx image (read-only, shared)"]
        L1["layer 1: Debian base files"]
        L2["layer 2: nginx installed"]
        L3["layer 3: config files"]
        CFG["config: Cmd, Env, ExposedPorts"]
        L1 --> L2 --> L3
    end

    W1["web: writable layer<br/>(/hello.txt lives here)"]
    W2["web2: writable layer<br/>(empty)"]

    L3 --> W1
    L3 --> W2

    W1 --> V1["web sees: / = layers 1-3 + its writes"]
    W2 --> V2["web2 sees: / = layers 1-3 only"]
```

## Copy-on-write: what happens when a container edits a file from the image

```mermaid
sequenceDiagram
    participant P as process in container
    participant O as overlay filesystem
    participant R as image layer (read-only)
    participant W as container writable layer

    P->>O: open /etc/nginx/nginx.conf for writing
    O->>R: file found in image layer
    O->>W: copy file up into writable layer
    P->>W: write goes to the copy
    Note over R: image layer never changes,<br/>so other containers are unaffected
```

## Container lifecycle

```mermaid
stateDiagram-v2
    [*] --> Created: docker create (writable layer made, no process)
    Created --> Running: docker start (process starts in new namespaces)
    Running --> Exited: process exits / docker stop
    Exited --> Running: docker start (same writable layer, files kept)
    Exited --> [*]: docker rm (writable layer deleted)
    note right of Exited
        no process, but the container
        and its files still exist
    end note
```
