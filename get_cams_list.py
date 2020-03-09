import requests
import json
import logging
from datetime import datetime


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s : %(levelname)s : %(message)s",
    filename="log_cam_list.log")


def cam_list():
    logging.info('------ START SCRIPT GET CAMERAS LIST------')
    login = 'api'
    password = '1iGcg/AxRYPVAYRoJ2o7qcZL9aKZCFdYT+yVphmSKtQ='
    url_address = 'http://192.168.192.12:3030/list'
    time1 = datetime.now()

    try:
        logging.debug('Trying to sent request with data:\nlogin: {}\npassword: {}\nurl: {}'
                      .format(login, password, url_address))
        api_request = requests.get(url_address, auth=(login, password))
        logging.info('Request has been sent')

        if api_request.status_code == 200:
            time2 = datetime.now()
            waiting = (time2 - time1).total_seconds()
            logging.info('Response received in {} sec'.format(waiting))
            with open('response_cams_list.json', 'w') as outfile:
                json.dump(api_request.json(), outfile)
                logging.info('The response is written to a file response_cams_list.json')
                logging.info('------ FINISH SCRIPT GET CAMERAS LIST ------')
        else:
            time2 = datetime.now()
            waiting = (time2 - time1).total_seconds()
            resp_code = api_request.status_code
            logging.debug('Response received with code {} in {} sec'.format(resp_code, waiting))

    except requests.exceptions.ConnectionError:
        time2 = datetime.now()
        waiting = (time2 - time1).total_seconds()
        logging.debug('ConnectionError in {} sec'.format(waiting))
        logging.info('------ FINISH SCRIPT GET CAMERAS LIST ------')


if __name__ == '__main__':
    cam_list()
