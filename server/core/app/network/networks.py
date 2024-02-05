import docker

class Network:
    
    def __init__(self, client: docker.DockerClient) -> None:
        self.client = client
        
    
    def get_networks(self):
        networks = self.client.networks.list()
        networks = [network.attrs for network in networks]
        return networks