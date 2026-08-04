# dockerfile-skills

## Set ARG versions for image

**Description**: Specify the base image version via ARG so that CI can override it with --build-arg without editing the Dockerfile.

### Debian Linux

**Bad:**

```dockerfile
FROM debian:trixie
```

**Good:**

```dockerfile
ARG DEBIAN_VERSION=13.6
FROM debian:${DEBIAN_VERSION}
```

### Alpine Linux

**Bad:**

```dockerfile
FROM alpine:3.24.1
```

**Good:**

```dockerfile
ARG ALPINE_TAG=3.24.1
FROM alpine:${ALPINE_TAG}
```

## Set SHA-256 digest using image

**Description**: To ensure reproducibility of the build, as tags may appear in different images.

### Debian Linux

**Bad:**

```dockerfile
FROM debian:13.6-slim
```

**Good:**

```dockerfile
ARG DEBIAN_VERSION=13.6
FROM debian:${DEBIAN_VERSION}-slim@sha256:020c0d20b9880058cbe785a9db107156c3c75c2ac944a6aa7ab59f2add76a7bd
```

### Alpine Linux

**Bad:**

```dockerfile
FROM alpine:3.24.0
```

**Good:**

```dockerfile
ARG ALPINE_TAG=3.24.0
FROM alpine:${ALPINE_TAG}@sha256:a2d49ea686c2adfe3c992e47dc3b5e7fa6e6b5055609400dc2acaeb241c829f4
```

## Set labels for image

**Description**: Use labels to organize your images.

### Debian Linux

**Bad:**

```dockerfile
CMD ["python", "-OO", "-m", "application"]
```

**Good:**

```dockerfile
CMD ["python", "-OO", "-m", "application"]

LABEL \
    org.opencontainers.image.title="My Business Application" \
    org.opencontainers.image.vendor="My Best Company" \
    org.opencontainers.image.source="https://github.com/zsxoff/dockerfile-skills"
```

### Alpine Linux

**Bad:**

```dockerfile
CMD ["python", "-OO", "-m", "application"]
```

**Good:**

```dockerfile
CMD ["python", "-OO", "-m", "application"]

LABEL \
    org.opencontainers.image.title="My Business Application" \
    org.opencontainers.image.vendor="My Best Company" \
    org.opencontainers.image.source="https://github.com/zsxoff/dockerfile-skills"
```

## Set own mirrors for packages

**Description**: Override mirrors to fetch packages from faster/more reliable sources (local mirror, proxy, cache).

### Debian Linux

**Bad:**

```dockerfile
...
```

**Good:**

```dockerfile
ARG DEBIAN_CODENAME=trixie
ARG DEBIAN_MIRROR=http://deb.debian.org/debian

RUN \
    rm -rf /etc/apt/sources.list /etc/apt/sources.list.d && \
    mkdir -p /etc/apt/sources.list.d && \
    { \
    echo "Types: deb" ; \
    echo "URIs: ${DEBIAN_MIRROR}/" ; \
    echo "Suites: ${DEBIAN_CODENAME}" ; \
    echo "Components: main non-free contrib non-free-firmware" ; \
    echo "Signed-By: /usr/share/keyrings/debian-archive-keyring.pgp" ; \
    echo ; \
    echo "Types: deb" ; \
    echo "URIs: ${DEBIAN_MIRROR}/" ; \
    echo "Suites: ${DEBIAN_CODENAME}-updates" ; \
    echo "Components: main non-free contrib non-free-firmware" ; \
    echo "Signed-By: /usr/share/keyrings/debian-archive-keyring.pgp" ; \
    echo ; \
    echo "Types: deb" ; \
    echo "URIs: ${DEBIAN_MIRROR}-security/" ; \
    echo "Suites: ${DEBIAN_CODENAME}-security" ; \
    echo "Components: main non-free contrib non-free-firmware" ; \
    echo "Signed-By: /usr/share/keyrings/debian-archive-keyring.pgp" ; \
    } > /etc/apt/sources.list.d/mirror.sources
```

### Alpine Linux

**Bad:**

```dockerfile
...
```

**Good:**

```dockerfile
ARG ALPINE_VERSION=v3.24
ARG ALPINE_MIRROR=https://dl-cdn.alpinelinux.org/alpine

RUN \
    { \
    echo "${ALPINE_MIRROR}/${ALPINE_VERSION}/main" ; \
    echo "${ALPINE_MIRROR}/${ALPINE_VERSION}/community" ; \
    } > /etc/apk/repositories
```

## Set slim image

**Description**: Use the slim image version to get a smaller target image with fewer packages and a reduced attack surface.

### Debian Linux

**Bad:**

```dockerfile
FROM debian:13.6
```

**Good:**

```dockerfile
ARG DEBIAN_VERSION=13.6
FROM debian:${DEBIAN_VERSION}-slim
```

### Alpine Linux

**Bad:**

```dockerfile
...
```

**Good:**

```dockerfile
ARG ALPINE_TAG=3.24.1
FROM alpine:${ALPINE_TAG}
```

## Set TERM for image

**Description**: TERM tells programs what escape codes/colors the terminal supports, so colors and TUIs work.

### Debian Linux

**Bad:**

```dockerfile
...
```

**Good:**

```dockerfile
ENV TERM=xterm-256color
```

### Alpine Linux

**Bad:**

```dockerfile
...
```

**Good:**

```dockerfile
ENV TERM=xterm-256color
```

## Set time zone for image

**Description**: If your application works with time (at least logging), let it determine the time at least in UTC.

### Debian Linux

**Bad:**

```dockerfile
...
```

**Good:**

```dockerfile
ARG TZ=UTC
ENV TZ=${TZ}
RUN cp --remove-destination /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone
```

### Alpine Linux

**Bad:**

```dockerfile
...
```

**Good:**

```dockerfile
RUN apk add tzdata

ARG TZ=UTC
ENV TZ=${TZ}
RUN ln -s /usr/share/zoneinfo/${TZ} /etc/localtime
```
