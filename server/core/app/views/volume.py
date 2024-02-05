from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from app.client import docker_client
from app.volume.volume import Volume as DockerVolume


class VolumeView(APIView):
    
    
    def get(self, request: Request, *args, **kwargs):        
        volumes = DockerVolume(client=docker_client).get_volumes()
        return Response(volumes, status=status.HTTP_200_OK)
    
    
    def post(self, request: Request, *args, **kwargs):
        data = request.data
        volume = DockerVolume(client=docker_client).create_volume(name=data.get("name"))
        return Response(volume, status=status.HTTP_201_CREATED)
    
    
    def delete(self, request: Request, *args, **kwargs):
        volume_id = request.query_params.get("id")
        force = request.query_params.get("force", False)
        volume = DockerVolume(client=docker_client).remove_volume(volume_id=volume_id, force=force)
        return Response(volume, status=status.HTTP_200_OK)