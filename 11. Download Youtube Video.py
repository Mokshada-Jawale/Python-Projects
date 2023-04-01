import pytube

#we save it in the current working dir
dnld_loc = './'

#to get url youtube video
def get_url():
    video_url = input("Enter url of youtube video: ")
    return video_url

def main(video_url):
    # create instance of yt video
    video_instance = pytube.YouTube(video_url)
    stream = video_instance.streams.get_highest_resolution()
    return stream

# Download the youtube video
def dnld_video(stream):
    stream.download()

if __name__ == '__main__':
    video_url = get_url()
    stream = main(video_url)
    dnld_video(stream)