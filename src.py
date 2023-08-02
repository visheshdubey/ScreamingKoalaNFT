# from moviepy.editor import AudioFileClip, ImageClip
from moviepy.editor import *


def silence_generate():

    audio_clip = AudioFileClip("assets/track/silence.mp3")
    image_clip = ImageClip("assets/img/1.png")
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 25
    video_clip.write_videofile("output1.mp4")

def sound_generate():

    audio_clip = AudioFileClip("assets/track/burp.mp3")
    image_clip =""
    image_clip = ImageClip("assets/img/11.png")
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 25
    video_clip.write_videofile("output2.mp4")
def generate():

    clip1 = VideoFileClip("output1.mp4")
    clip2 = VideoFileClip("output2.mp4")
    final = concatenate_videoclips([clip1, clip2, clip1])
    final.fps =25
    final.write_videofile("merged.mp4")

def add_static_image_to_audio(image_path, audio_path, output_path):
    """Create and save a video file to `output_path` after 
    combining a static image that is located in `image_path` 
    with an audio file in `audio_path`"""
    # create the audio clip object
    audio_clip = AudioFileClip(audio_path)
    # create the silence clip object
    audio_clip2 = AudioFileClip("assets/track/silence.mp3")
    # create the image clip object
    image_clip2 = ImageClip(image_path)
    # create the silent image clip object
    image_clip = ImageClip("assets/img/11.png")
    # use set_audio method from image clip to combine the audio with the image
    video_clip = image_clip.set_audio(audio_clip)
    video_clip2 = image_clip2.set_audio(audio_clip2)
    # specify the duration of the new clip to be the duration of the audio clip
    video_clip.duration = audio_clip.duration
    video_clip2.duration = audio_clip2.duration

    final = concatenate_videoclips([video_clip, video_clip2, video_clip])
    # set the FPS to 1
    # final.fps = 1
    # write the resuling video clip
    final.write_videofile(output_path)


# add_static_image_to_audio("assets/img/1.png", "assets/track/burp.mp3", "output1.mp4")
silence_generate()
sound_generate()
generate()

# if __name__ == "__main__":
#     import argparse
#     parser = argparse.ArgumentParser(description="Simple Python script to add a static image to an audio to make a video")
#     parser.add_argument("image", help="The image path")
#     parser.add_argument("audio", help="The audio path")
#     parser.add_argument("output", help="The output video file path")
#     args = parser.parse_args()