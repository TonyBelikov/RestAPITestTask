from requests.exceptions import HTTPError


def response_checker(response, expected_code=200):

    try:

        if response.status_code != expected_code:
            raise Exception("Request done with unexpected code: {}. Expected status code is: {}".format(
                response.status_code, expected_code)
            )

    except HTTPError as http_err:
        raise Exception(f'HTTP error occurred: {http_err}')
    except Exception as err:
        raise Exception(f'Other error occurred: {err}')

