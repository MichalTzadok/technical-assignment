import docker

# Create a Docker client
client = docker.from_env()

# Run a BusyBox container and keep it alive using sleep
container = client.containers.run(
    "busybox",
    "sleep 3600",  # Keep the container running for 1 hour
    detach=True,
    name="task5_busybox"
)

print(f"Container {container.name} started with ID: {container.id}")

# Execute a command inside the container to get the hostname
exec_result = container.exec_run("hostname")
hostname = exec_result.output.decode().strip()
print(f"Container hostname: {hostname}")

# Stop the container after checking
container.stop()
print(f"Container {container.name} stopped.")
