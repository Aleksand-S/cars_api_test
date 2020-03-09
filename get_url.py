from datetime import datetime, timedelta
import random
import json
import threading
import requests
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s : %(levelname)s : %(message)s",
    filename="logging.log")


def random_start():
    delta_datetime = random.randint(259200, 31536000)  # 3 days = 259.200 sec, 1 year = 31.536.000 sec
    now = datetime.now()
    return now - timedelta(seconds=delta_datetime)


def random_end(start):
    delta_datetime = random.randint(1, 259200)
    return start + timedelta(seconds=delta_datetime)


def get_url(cam_id_request, start_request, finish_request):
    login = 'api'
    password = '1iGcg/AxRYPVAYRoJ2o7qcZL9aKZCFdYT+yVphmSKtQ='
    url_address = 'http://192.168.192.12:3030/archive'
    time1 = datetime.now()

    try:
        logging.debug('Trying to sent request with data:\nlogin: {}\npassword: {}\nurl: {}\nCamera ID: {}'
                      .format(login, password, url_address, cam_id_request))
        api_request = requests.get(url_address, auth=(login, password),
                                   params={'id': cam_id_request, 'start': start_request, 'end': finish_request})
        logging.info('Request for CamID-{} has been sent'.format(cam_id_request))

        if api_request.status_code == 200:
            time2 = datetime.now()
            waiting = (time2 - time1).total_seconds()
            api_response = api_request.json()  # response converted to Python dictionary
            url = api_response['url']
            logging.info('Response received for CamID-{} in {} sec\nURL: {}'
                         .format(cam_id_request, waiting, url))
        else:
            time2 = datetime.now()
            waiting = (time2 - time1).total_seconds()
            resp_code = api_request.status_code
            logging.debug('Response received for CamID-{} with code {} in {} sec'
                          .format(cam_id_request, resp_code, waiting))

    except requests.exceptions.ConnectionError:
        time2 = datetime.now()
        waiting = (time2 - time1).total_seconds()
        logging.debug('ConnectionError for CamID-{} in {} sec'.format(cam_id_request, waiting))


def get_cams_id_list():
    """
    :return: list of random 20 camera ID
    """
    logging.info('Trying to open file with cameras list')
    with open('response_cams_list.json', 'r') as file_data:
        data = json.load(file_data)
        cams_dict = data['cams']  # clarify the structure and keys of the input dictionary !!!
        all_id_list = [cam['id'] for cam in cams_dict]
        try:
            random_list = random.sample(all_id_list, 20)
        except ValueError:
            logging.error('Number of cameras less than 20')
            return all_id_list
        return random_list


def main():
    logging.info('------ START SCRIPT GET URL FOR 20 CAMERAS ------')
    start = random_start()
    end = random_end(start)
    logging.info('Start stream: {}. End stream: {}'.format(start.isoformat(), end.isoformat()))
    cameras_id_random_list = get_cams_id_list()
    logging.info('A list of cameras ID was generated.')

    for cam_id in cameras_id_random_list:
        threading.Thread(target=get_url, args=(cam_id, start.isoformat(), end.isoformat())).start()

    logging.info('------ FINISH SCRIPT GET URL FOR 20 CAMERAS ------')


if __name__ == '__main__':
    main()
