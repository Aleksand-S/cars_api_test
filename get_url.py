# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import random
import requests
import logging


def random_start():
    delta_datetime = random.randint(259200, 31536000)  # 3 days = 259.200 sec, 1 year = 31.536.000 sec
    now = datetime.now()
    return now - timedelta(seconds=delta_datetime)


def random_end(start):
    delta_datetime = random.randint(1, 259200)
    return start + timedelta(seconds=delta_datetime)


def get_url(cam_id_request, start_request, finish_request):
    pass


def main():
    logging.basicConfig(level=logging.DEBUG, filename='logging.log')
    logging.info("--- Program started ---")

    start = random_start()
    end = random_end(start)
    cam_id_request = input('Input camera ID: ')

    logging.info("--- Program is done ---!")


if __name__ == '__main__':
    main()


"""
def get_url(cam_id_request, start_request, finish_request):
    login = 'api'
    password = '1iGcg/AxRYPVAYRoJ2o7qcZL9aKZCFdYT+yVphmSKtQ='
    url_address = 'http://192.168.192.12:3030/archive'
    cam_id_request = input('Input camera ID: ')
    api_request = requests.get(url_address, auth=(login, password),
                               params={'id': cam_id_request, 'start': start_request, 'end': finish_request})

    if api_request.status_code == 200:
        api_response = api_request.json()  # response converted to Python dictionary
        url = api_response['url']
"""