FROM ubuntu:20.04

# Development packages
RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" \
    apt-get install -y \
    curl \
    git \
    httpie \
    make \
    openjdk-11-jdk \
    rlwrap \
    wget

# Clojure installation
ENV CLJ_VERSION=1.10.3.822
RUN wget https://download.clojure.org/install/linux-install-${CLJ_VERSION}.sh && \
    chmod +x linux-install-${CLJ_VERSION}.sh && \
    ./linux-install-${CLJ_VERSION}.sh && \
    rm -f ./linux-install-${CLJ_VERSION}.sh && \
    clj -P

# Leiningen installation
RUN wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && \
    mv lein /usr/local/bin/ && \
    chmod a+x /usr/local/bin/lein && \
    lein
