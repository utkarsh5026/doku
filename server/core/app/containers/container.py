import docker 

class Container:
    
    def __init__(self, client: docker.DockerClient) -> None:
        self.client = client
        
        
    def get_containers(self):
        containers = self.client.containers.list(
            all=True
        )
        # convert to dict
        containers = [container.attrs for container in containers]
        return containers
    
    
    def get_container_detail(self, container_id: str):
        try:
            container = self.client.containers.get(container_id)
            container = container.attrs
            return container
        except docker.errors.NotFound:
            return None
    
    
    
print(Container(docker.from_env()).get_containers())