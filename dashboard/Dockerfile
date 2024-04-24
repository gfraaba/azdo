# Use an official Node.js runtime as a parent image
FROM node:20 AS base

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# ---- Dependencies ----
FROM base AS dependencies
# Install the application dependencies
RUN npm ci --omit=dev || exit 1

# ---- Copy Files/Build ----
FROM dependencies AS build
# WORKDIR /app
# Copy the rest of the application code to the working directory
COPY . .
RUN npm run build || exit 1
RUN ls -la

# This isn't working for some strange reason!! The original project folder ends up in this 'release' image!! 
# As a workaround, I built it inside the Docker container using Visual Studio Code's Dev Container feature. So, the build folder is already there. And nothing to do with the actual build folder copied from the 'build' image
# --- Release with Alpine ----
FROM node:20-alpine AS release
WORKDIR /app
COPY --from=build /app/build/ /app/build/
RUN ls -la
RUN npm install -g serve
RUN ls -la
EXPOSE 3000
CMD ["serve", "-s", "/app/build", "-l", "3000"]