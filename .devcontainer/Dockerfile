# Start from a latest Python 3 base image (3.12.3 as of 2024-04-20)
# 3-slim-bookworm uses latest Debian 12 (Bookworm) slim image and isn't supported by PowerShell v7.4.2 yet as of 2024-04-20
# Visual Studio Code: Cmd + Shift + P -> Dev Containers: Reopen in Container
# docker ps -all # run this on host
FROM python:3-slim-bookworm

# Install Node.js
# Looks like gnupg and apt-transport-https are already available in the base image
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

# # Install PowerShell
RUN apt-get install -y wget \
    && wget https://github.com/PowerShell/PowerShell/releases/download/v7.4.2/powershell-7.4.2-linux-arm64.tar.gz \
    && mkdir pwsh-7.4.2 \
    && tar -xvf powershell-7.4.2-linux-arm64.tar.gz -C pwsh-7.4.2 \
    && rm powershell-7.4.2-linux-arm64.tar.gz \
    && mv pwsh-7.4.2 /usr/local/bin/pwsh7.4.2 \
    && ln -s /usr/local/bin/pwsh7.4.2/pwsh /usr/bin/pwsh \
    # libicu is required for PowerShell; alternatively: export DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1
    && apt-get install -y libicu-dev \
    # Verify that PowerShell was installed correctly
    && pwsh --version
    
    # PowerShell v7.4.2 is not available for Debian 12 (Bookworm) as of 2024-04-20 for arm64
    # && wget https://github.com/PowerShell/PowerShell/releases/download/v7.4.2/powershell_7.4.2-1.deb_amd64.deb \
    # Register the Microsoft repository GPG keys
    # && dpkg -i powershell_7.4.2-1.deb_amd64.deb \
    # Update the package list after adding packages.microsoft.com
    # && apt-get update \
    # Finally, install PowerShell
    # && apt-get install -y powershell
    # && apt-get install -f
# RUN curl -fsSL https://aka.ms/install-powershell.sh | bash -

# Verify that Node.js and npm were installed correctly
RUN node --version
RUN npm --version

# Verify that Python was installed correctly
RUN python --version

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r api/requirements.txt