import docker 
from docker.errors import ImageNotFound

class Image:
    
    def __init__(self, client: docker.DockerClient):
        self.client = client
        
        
    def get_all_images(self, all: bool = True):
        images = self.client.images.list(all=all)
        images = [image.attrs for image in images]
        return images
    
    
    def get_image_info(self, image_id: str):
        image = self.get_image(image_id=image_id)
        if image is not None:
            return image.attrs
        return image
    
    
    def remove_image(self, image_id: str, force: bool):
        image = self.client.images.remove(image_id)
        return image
    
    
    def get_image(self, image_id: str):
        try:
            image = self.client.images.get(image_id)
            return image
        except ImageNotFound:
            return None