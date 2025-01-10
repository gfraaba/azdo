# Start from the latest Python 3 base image (3.12.5 as of 2024.09.09 | 3.12.3 as of 2024-04-20)
# 3-slim-bookworm uses latest Debian 12 (codename: bookworm) slim image
#   Issues: arm64 flavor isn't supported by PowerShell v7.4.5 yet as of 2024-10-20
#     Workaround: Use the latest version of PowerShell from GitHub that supports arm64
# Visual Studio Code: Cmd + Shift + P -> Dev Containers: Reopen in Container
# run this on host: "docker container ls -a" # to see all containers # previously: docker ps -all 

# Use build arguments for flexibility
ARG PYTHON_IMAGE_TAG="3-slim-bookworm"
ARG NODE_VERSION="20"
ARG PWSH_VERSION
ARG PLATFORM

# Start from the Debian version specific latest Python base image
FROM python:${PYTHON_IMAGE_TAG}

# Verify Python version
RUN python --version

# Install Node.js
RUN apt-get update && apt-get install -y curl wget apt-transport-https software-properties-common
RUN curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash -
RUN apt-get install -y nodejs npm

# Conditionally install PowerShell based on the platform
# Bug Fix: Had to declare the ARG PWSH_VERSION again here to use it in the RUN command!
ARG PWSH_VERSION
ARG PLATFORM
RUN if [ "$PLATFORM" = "linux/amd64" ]; then \
      wget -q "https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb" \
      && dpkg -i packages-microsoft-prod.deb \
      && apt-get update \
      # && apt-get install -y powershell=${PWSH_VERSION}-1.deb \ # If a specific version is needed
      && apt-get install -y powershell \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*; \
    elif [ "$PLATFORM" = "linux/arm64" ]; then \
        wget https://github.com/PowerShell/PowerShell/releases/download/v${PWSH_VERSION}/powershell-${PWSH_VERSION}-linux-arm64.tar.gz \
        && mkdir /usr/local/bin/pwsh${PWSH_VERSION} \
        && tar -xvf powershell-${PWSH_VERSION}-linux-arm64.tar.gz -C /usr/local/bin/pwsh${PWSH_VERSION} \
        && chmod +x /usr/local/bin/pwsh${PWSH_VERSION}/pwsh \
        && rm powershell-${PWSH_VERSION}-linux-arm64.tar.gz \
        && ln -s /usr/local/bin/pwsh${PWSH_VERSION}/pwsh /usr/local/bin/pwsh \
        # libicu is required for PowerShell; alternatively: export DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1
        && apt-get install -y libicu-dev \
        # Verify that PowerShell was installed correctly
        && echo "echoing Node.js version: $(node --version)" \
        && sleep 10 \
        && echo "echoing npm version: $(npm --version)" \
        && sleep 10 \
        && echo "PWSH_VERSION: $PWSH_VERSION" \
        && pwsh --version || echo "PowerShell installation failed" \
        && echo "echoing PowerShell version: $(pwsh --version)" \
        && sleep 10; \
    else \
      echo "PowerShell is not supported on $PLATFORM" \
      && sleep 20 \
      && exit 1; \
    fi

ENV PLATFORM="$PLATFORM"

# ARG ARCH
# ARG PLATFORM
# RUN if [ "$PLATFORM" = "linux/arm64" ]; then \
#       ARCH="linux-arm64"; \
#     else \
#       ARCH="linux-x64"; \
#     fi \
#     && echo "PLATFORM: $PLATFORM" \
#     && sleep 10 \
#     && echo "Architecture: $ARCH" \
#     && sleep 10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r api/requirements.txt