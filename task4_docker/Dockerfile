# Base image
FROM ubuntu:22.04

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update + install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Entrypoint – show ffmpeg version
ENTRYPOINT ["ffmpeg", "-version"]
