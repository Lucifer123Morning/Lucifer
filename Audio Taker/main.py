import moviepy.editor
from pathlib import Path

video_file = Path('my_video.mp4')

video = moviepy.editor.VideoClip(video)
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')