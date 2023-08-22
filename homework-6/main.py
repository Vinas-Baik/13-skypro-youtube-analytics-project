from src.video import Video

if __name__ == '__main__':
    for video_url in ['broken_video_id', 'AWX4JnAnjBE', '4fObz_qw9u4',
                      '4fOasd_qw9u4']:
        broken_video = Video(video_url)
        print(broken_video.__repr__())
        print(broken_video.my_repr())
        if broken_video.title == None:
            assert broken_video.title is None
            assert broken_video.like_count is None
