# Task 4 – Dockerfile with ffmpeg

## Description
This task implements a Dockerfile that installs `ffmpeg` on an Ubuntu base image.
The Dockerfile sets an entrypoint to verify the installation by printing the ffmpeg version.

## How to Build

```bash
docker build -t task4-docker .
