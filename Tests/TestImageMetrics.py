import requests

from common.APIRequests.ImageMetrics import ImageMetricsV1, ImageMetricsV2
import pytest
import allure
import time
from common.APIRequests.ResponseChecker import response_checker


@allure.epic("Тестирование API запросов ImageMetricsV1 и ImageMetricsV2")
class TestImageAPI:

    @allure.feature("ImageMetricsV2")
    @allure.severity("high")
    @allure.title("Проверка ImageMetricsV2 на работу с корректными данными")
    @pytest.mark.high
    def test_correct_data(self):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            response = ImageMetricsV2.post_image_metrics_v2(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url='https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png'
            )
            response_checker(
                response=response
            )

    @allure.feature("ImageMetricsV2")
    @allure.severity("high")
    @allure.title("Проверка ImageMetricsV2 на работу с некорректными данными")
    @pytest.mark.high
    def test_incorrect_data(self):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            response = ImageMetricsV2.post_image_metrics_v2(
                user_name='JuicyUser_12',
                password='JuicyPassword',
                image_url='https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png'
            )
            response_checker(
                response=response
            )
            response = response.json()
            if response['operationResult']['status'].lower() != 'error':
                raise Exception("Запрос ImageMetricsV2 некорректно обрабатывает запрос с отсутствующими данными")

    @allure.feature("ImageMetricsV2")
    @allure.severity("high")
    @allure.title("Проверка ImageMetricsV2 на работу с отсутствующими данными")
    @pytest.mark.high
    def test_empty_data(self):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            response = requests.post(
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Charset': 'utf-8',
                    'Connection': 'close'
                },
                url="https://qaquiz.juicyscore.net/api/getImageMetricsV2",
                json={
                    "userName": "JuicyUser",
                    "imageUrl": "https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png"
                }
            )
            response_checker(
                response=response,
                expected_code=400
            )

    @allure.feature("ImageMetricsV2")
    @allure.severity("medium")
    @allure.title("Проверка ImageMetricsV2 на считывание изображения через https протокол")
    @pytest.mark.medium
    def test_read_https_image(self):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            response = ImageMetricsV2.post_image_metrics_v2(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url='https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png'
            )
            response_checker(
                response=response,
                expected_code=200
            )

    @allure.feature("ImageMetricsV2")
    @allure.severity("medium")
    @allure.title("Проверка ImageMetricsV2 на считывание изображений в разных форматах")
    @pytest.mark.medium
    @pytest.mark.parametrize('image_url', [
        'https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png',
        'https://dadaviz.ru/wp-content/uploads/2018/02/1-12.jpg'
    ])
    def test_several_image_formats(self, image_url):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            response = ImageMetricsV2.post_image_metrics_v2(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url=image_url
            )
            response_checker(
                response=response,
                expected_code=200
            )

    @allure.feature("ImageMetricsV2")
    @allure.severity("critical")
    @allure.title("Проверка ImageMetricsV2 на корректное считывание разрешения изображения")
    @pytest.mark.critical
    def test_compare_resolution(self):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            response = ImageMetricsV2.post_image_metrics_v2(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url='https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png'
            )
            response = response.json()
            if response['imageMetrics']['height'] != 626 or response['imageMetrics']['width'] != 626:
                raise Exception("Считанное разрешение изображения не соответствует действительному")

    @allure.feature("ImageMetricsV2")
    @allure.severity("critical")
    @allure.title("Сравнение скорости работы ImageMetricsV1 и ImageMetricsV2")
    @pytest.mark.critical
    def test_v1_and_v2_speed(self):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            start_v2 = time.time()
            response_v2 = ImageMetricsV2.post_image_metrics_v2(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url='https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png'
            )
            end_v2 = time.time()
            response_checker(
                response=response_v2
            )
        with allure.step("Выполнение запроса ImageMetricsV1"):
            start_v1 = time.time()
            response_v1 = ImageMetricsV1.post_image_metrics_v1(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url='https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png'
            )
            end_v1 = time.time()
            response_checker(
                response=response_v1
            )
        with allure.step("Сравнение скорости выполнения ImageMetricsV1 и ImageMetricsV2"):
            time_v1 = end_v1 - start_v1
            time_v2 = end_v2 - start_v2
            if time_v2 > time_v1:
                raise Exception("Время выполнения ImageMetricsV2 больше, чем время выполнения ImageMetricsV1")

    @allure.feature("ImageMetricsV2")
    @allure.severity("critical")
    @allure.title("Проверка корректности результатов API запроса ImageMetricsV2")
    @pytest.mark.critical
    def test_correct_result_of_image_metrics_v2(self):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            response_v2 = ImageMetricsV2.post_image_metrics_v2(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url='https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png'
            )
        with allure.step("Выполнение запроса ImageMetricsV1"):
            response_v1 = ImageMetricsV1.post_image_metrics_v1(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url='https://avatanplus.com/files/resources/original/5d10f57eac2bd16b8a3ef6f1.png'
            )
        with allure.step("Сравнение результатов выполнения запросов ImageMetricsV1 и ImageMetricsV2"):
            if response_v1 != response_v2:
                raise Exception("Результаты выполнения запроса ImageMetricsV2 отличаются от результатов ImageMetricsV1")

    @allure.feature("ImageMetricsV2")
    @allure.severity("critical")
    @allure.title("Проверка корректной обработки ошибок с стороны ImageMetricsV2")
    @pytest.mark.critical
    def test_correct_errors_v2_proccessing(self):
        with allure.step("Выполнение запроса ImageMetricsV2"):
            response = ImageMetricsV2.post_image_metrics_v2(
                user_name='JuicyUser',
                password='JuicyPassword',
                image_url="https://dadaviz.ru/wp-content/uploads/2018/02/1-12.jpgf"
            )
            response_checker(
                response=response,
                expected_code=404
            )
