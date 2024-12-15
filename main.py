import logging
import logging.handlers
import os
import time

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    logger.info("Run")

    url = "https://oap.ind.nl/oap/api/desks/AM/slots"
    params = {
        "productKey": "DOC",
        "persons": 1
    }
    response = requests.get(url, params=params, verify=False)
    if response.status_code == 200:
        text = '{' + response.text[21:]
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        if '"date":"2024-12-1' in text:
            # print(FOUND)
            # print(f"{current_time} -- FOUND.")
            logger.info(f'FOUND: {current_time}')
        else:
            logger.info('skip')
            # print(f"{current_time} -- NOTHING")
