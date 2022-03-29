import os
from django.core.exceptions import ValidationError
from mutagen.mp3 import MP3
from numpy import True_

def validate_isaudio(file):
    try:
        audio = MP3(file)
        if not audio:
            raise TypeError()
        file_check = True
    except Exception as e:
        file_check = False
    if not file_check:
        raise ValidationError('Unsupported File Formate')
    valid_file_formate = ['.mp3']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_formate:
        raise ValidationError('Unsupported File Forate')
