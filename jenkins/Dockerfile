FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    rpm \
    dpkg-dev \
    debhelper \
    build-essential \
    curl \
    git \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    alien \
    && rm -rf /var/lib/apt/lists/*

RUN usermod -aG docker jenkins

USER jenkins

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

EXPOSE 8080
EXPOSE 50000

ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
