from django.core.exceptions import ValidationError
import os

# this is validation to stop uploading junk file like -pdf in image filed

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1] # in cover-image.jpg 2 extensions one is cover-image and 2nd is jpg, and value is image name
    print(ext)
    valid_extensions = ['.png', '.jpg', '.jpeg'] #these extensions we will accept
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions: ' +str(valid_extensions))