import docker

class Volume:
    
    def __init__(self, client: docker.DockerClient) -> None:
        self.client = client
        
    def get_volumes(self):
        volumes = self.client.volumes.list()
        volumes = [volume.attrs for volume in volumes]
        return volumes