FROM jenkins/jenkins:lts

USER root

# Install dependencies for building RPM and DEB packages
RUN apt-get update && apt-get install -y \
    rpm \
    dpkg-dev \
    debhelper \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install RPM build tools
RUN apt-get update && apt-get install -y \
    alien \
    && rm -rf /var/lib/apt/lists/*

# Switch back to jenkins user
USER jenkins

# Skip initial setup wizard
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

# Expose Jenkins port
EXPOSE 8080
EXPOSE 50000

# Start Jenkins
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
