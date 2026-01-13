from threads_uploader.client import ThreadsClient
from threads_uploader.media import MediaUploader
from threads_uploader.config import THREADS_ACCESS_TOKEN, THREADS_USER_ID


class ThreadsUploader:
    def __init__(self):
        self.client = ThreadsClient(THREADS_ACCESS_TOKEN)
        self.media = MediaUploader(THREADS_ACCESS_TOKEN)

    def post_text(self, caption: str):
        return self.client.publish_text(
            user_id=THREADS_USER_ID,
            text=caption
        )

    def post_image(self, image_url: str, caption: str | None = None):
        result = self.media.upload_image(image_url, THREADS_USER_ID)
        if caption:
            self.post_text(caption)
        return result

    def post_video(self, video_url: str, caption: str | None = None):
        result = self.media.upload_video(video_url, THREADS_USER_ID)
        if caption:
            self.post_text(caption)
        return result
