# This is a way of separating static files from other files such as 
# product images, for fear of overwriting static files. So 
# static files will be in one directory on S3 and product images in another

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# Create a class that inherits from S3Boto3Storage, and give it the location
# of static files, which is set in settings.py
# This tells s3 where to store the static files (s3/static)

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    
# Create a class that inherits from S3Boto3Storage, and give it the location
# of media files, which is set in settings.py
# This tells s3 where to store the media files (s3/media)

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION