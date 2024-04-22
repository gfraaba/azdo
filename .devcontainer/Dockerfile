# Start from a latest Python 3 base image (3.12.3 as of 2024-04-20)
# 3-slim-bookworm uses latest Debian 12 (Bookworm) slim image and isn't supported by PowerShell v7.4.2 yet as of 2024-04-20
# Visual Studio Code: Cmd + Shift + P -> Dev Containers: Reopen in Container
# docker ps -all # run this on host
FROM python:3-slim-bookworm

# Install Node.js
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

# Install PowerShell
# RUN apt-get install -y wget \
    # Get the version of Debian (e.g., 10 or 11)
    # && source /etc/os-release
    # Download the Microsoft repository GPG keys
    # && wget -q https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb \
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

# Verify that PowerShell was installed correctly
# RUN pwsh --version

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r api/requirements.txt