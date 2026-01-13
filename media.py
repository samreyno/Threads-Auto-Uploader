import requests


class MediaUploader:
    def __init__(self, access_token: str):
        self.access_token = access_token

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}"
        }

    def upload_image(self, image_url: str, user_id: str):
        url = f"https://graph.threads.net/v1.0/{user_id}/threads"
        payload = {
            "image_url": image_url,
            "media_type": "IMAGE"
        }

        response = requests.post(url, json=payload, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def upload_video(self, video_url: str, user_id: str):
        url = f"https://graph.threads.net/v1.0/{user_id}/threads"
        payload = {
            "video_url": video_url,
            "media_type": "VIDEO"
        }

        response = requests.post(url, json=payload, headers=self._headers())
        response.raise_for_status()
        return response.json()
