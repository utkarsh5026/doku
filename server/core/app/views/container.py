from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from app.client import docker_client
from app.containers.container import Container as DockerContainer

class ContainerView(APIView):
    
    def get(self, request: Request) -> Response:
        
        container = DockerContainer(client=docker_client)
        containers = container.get_containers()
        return Response(containers, status=status.HTTP_200_OK)
        
        
        
        