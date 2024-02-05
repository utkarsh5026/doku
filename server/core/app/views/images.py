from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app.client import docker_client

from app.images.image import Image as DockerImage


class ImageView(APIView):

    def get(self, request: Request, *args, **kwargs):
        print(request.query_params)
        image_id = request.query_params.get("id")
        # print the url
        print(request.build_absolute_uri())
        if image_id:
            print("help")
            image = DockerImage(client=docker_client).get_image_info(
                image_id=image_id)
            return Response(image, status=status.HTTP_200_OK)

        images = DockerImage(client=docker_client).get_all_images()
        return Response(images, status=status.HTTP_200_OK)
