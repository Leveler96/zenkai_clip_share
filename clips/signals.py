import subprocess
from fileinput import filename

import ffmpeg
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

from ffmpeg import output, overwrite_output

from .models import Clip


@receiver(post_save, sender=Clip)
def transcode_video(sender, instance, created, **kwargs):
    if created and instance.video_file:
        raw_file_path = instance.video_file.path

        # path for converted video file
        converted_dir = os.path.join(os.path.dirname(raw_file_path), 'converted')
        os.makedirs(converted_dir, exist_ok=True)

        filename = os.path.basename(raw_file_path)
        output_file_path = os.path.join(converted_dir, f'converted_{filename}')

        # use ffmpeg to transcode video
        try:
            (
                ffmpeg
                .input(raw_file_path)
                .output(output_file_path, vcodec='libx264', acodec='aac', movflags='faststart', vf='scale=-2:720')
                .run(overwrite_output=True, quite=True)
            )

            instance.converted_video_file.name = f'clips/converted/converted_{filename}'
            instance.save(update_fields=['converted_video_file'])

        except ffmpeg.Error as e:
            print(f"FFmpeg error: {e.stderr.decode('utf8')}")

            # optional, delete original raw upload to save space
            # os.remove(raw_file_path)
