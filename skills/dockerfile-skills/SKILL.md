# dockerfile-skills

## Set SHA-256 digest using image

**Description**: To ensure reproducibility of the build, as tags may appear in different images.

### Debian Linux

**Bad:**

```dockerfile
FROM debian:13.5-slim
```

**Good:**

```dockerfile
FROM debian:13.5-slim@sha256:4e401d95de7083948053197a9c3913343cd06b706bf15eb6a0c3ccd26f436a0e
```

### Alpine Linux

**Bad:**

```dockerfile
FROM alpine:3.24.0
```

**Good:**

```dockerfile
FROM alpine:3.24.0@sha256:a2d49ea686c2adfe3c992e47dc3b5e7fa6e6b5055609400dc2acaeb241c829f4
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
