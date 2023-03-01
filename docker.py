import os
import docker
from typing import List

class DockerContainer:
    def __init__(self, image: str, command: str):
        self.image = image
        self.command = command

    def run(self, sripe):
        client = docker.from_env()
        return client.containers.run(self.image, self.command, detach=True)

class DockerServer:
    def __init__(self, containers: List[DockerContainer]):
        self.containers = containers

    def create_containers(self):
        for container in self.containers:
            container.run()

    def create_web_server(self, sripe):
        # logic for creating a web server goes here
        pass

if __name__ == "__main__":
    containers = [
        DockerContainer('rancher/docs', ''),
        DockerContainer('docker/mobywebsite:latest', ''),
        DockerContainer('docker/mobywebsite:staging', ''),
        DockerContainer('hashicorp/nomad-website:latest', ''),
        DockerContainer('hashicorp/nomad-website:ce7c882dc8895d17f281fd8744c4666da052ca976f4a9825b82422ff5caf78ea', ''),
        DockerContainer('drupal:9.5.3-php8.1-fpm-buster', ''),
        DockerContainer('drupal:9.5.3-php8.1-fpm-alpine3.17', ''),
    ]
    server = DockerServer(containers)
    server.create_containers()
    server.create_web_server('')
