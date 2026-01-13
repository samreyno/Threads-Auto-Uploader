import requests

THREADS_API_BASE = "https://graph.threads.net/v1.0"


class ThreadsClient:
    def __init__(self, access_token: str):
        self.access_token = access_token

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def publish_text(self, user_id: str, text: str):
        url = f"{THREADS_API_BASE}/{user_id}/threads"
        payload = {"text": text}

        response = requests.post(url, json=payload, headers=self._headers())
        response.raise_for_status()
        return response.json()
