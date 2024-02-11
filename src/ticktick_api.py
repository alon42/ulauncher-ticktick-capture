import logging
import requests
import time


logger = logging.getLogger(__name__)
class TicktickApi:
    url = "https://api.ticktick.com/open/v1/task"
    token = None

    def set_token(self, token):
        self.token = token

    def add_task(self, task):
        response = requests.post(
            self.url,
            json={
                "title": task,
            },
            headers={
                "Authorization": "Bearer %s" % self.token,
                "X-Request-Id": str(time.time()),
                "Content-Type": "application/json",
            }
        )
        logger.info(self.token)
        logger.info(self.url)
        return None if response.status_code == 200 else "Error communicating with Ticktick. Repsonse code is %s. " % response.status_code
