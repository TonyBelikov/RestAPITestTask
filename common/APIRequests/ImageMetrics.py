import requests
from conftest import config


class ImageMetricsV1:

    @staticmethod
    def get_url():
        return f"{config.base_url.url}/api/getImageMetricsV1"

    @classmethod
    def post_image_metrics_v1(cls, user_name, password, image_url):
        url = ImageMetricsV1.get_url()
        request_data = {
            'userName': user_name,
            'password': password,
            'imageUrl': image_url
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Charset': 'utf-8',
            'Connection': 'close'
        }
        return requests.post(
            url=url,
            json=request_data,
            headers=headers
        )


class ImageMetricsV2:

    @staticmethod
    def get_url():
        return f"{config.base_url.url}/api/getImageMetricsV2"

    @classmethod
    def post_image_metrics_v2(cls, user_name, password, image_url):
        url = ImageMetricsV2.get_url()
        request_data = {
            'userName': user_name,
            'password': password,
            'imageUrl': image_url
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Charset': 'utf-8',
            'Connection': 'close'
        }
        return requests.post(
            url=url,
            json=request_data,
            headers=headers
        )