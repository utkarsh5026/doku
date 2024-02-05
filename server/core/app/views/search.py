from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from app.client import docker_client
from app.containers.container import Container as DockerContainer
from app.images.image import Image as DockerImage
from app.network.networks import Network as DockerNetwork
from app.volume.volume import Volume as DockerVolume


class SearchView(APIView):
    
    def get(self, request: Request) -> Response:
        # path /search/:id
        search_id = request.query_params.get("id")
        results = self.fetch_results(id=search_id)
        return Response(data=results, status=status.HTTP_200_OK)
    
    
    def fetch_results(self, id: str) -> dict[str, list]:
        containers = self.find_item_by_id(id=id,
                                        items=DockerContainer(
                                            client=docker_client).get_containers())
        
        images = self.find_item_by_id(id=id,
                                    items=DockerImage(
                                        client=docker_client).get_all_images())
        
        networks = self.find_item_by_id(id=id,
                                        items=DockerNetwork(
                                            client=docker_client).get_networks())
        
        volumes = self.find_item_by_id(id=id,
                                    items=DockerVolume(
                                        client=docker_client).get_volumes(),
                                    key='Name')
        
        return {
            "containers": containers,
            "images": images,
            "networks": networks,
            "volumes": volumes
        }
        
        
    @classmethod
    def find_item_by_id(cls, id: str, items: list, key = 'Id') -> list[str]:
        filtered =  [{"item": item, "index": index} for index, item in enumerate(items) if id in item[key]]
        
        filtered = [{"item": item["item"], "start": item["index"], "end": item["index"] + len(id)} for item in filtered]
        return filtered