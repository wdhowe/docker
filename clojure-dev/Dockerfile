FROM ubuntu:22.04

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
RUN wget https://github.com/clojure/brew-install/releases/latest/download/linux-install.sh && \
    chmod +x linux-install.sh && \
    ./linux-install.sh && \
    rm -f ./linux-install.sh && \
    clj -P

# CLJ Tools
RUN clj -Ttools install-latest :lib io.github.seancorfield/deps-new :as new

# Leiningen installation
RUN wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && \
    mv lein /usr/local/bin/ && \
    chmod a+x /usr/local/bin/lein && \
    lein
