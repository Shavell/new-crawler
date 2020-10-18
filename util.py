import logging
import time
from datetime import datetime

import pandas as pd
from beautifultable import BeautifulTable
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from db import models
from exceptions import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
fh = logging.FileHandler('logs.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


def check_success_response(self):
    wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
    wait.until(EC.element_to_be_clickable((By.XPATH, Constants.store_name_path)))

    if len(self.driver.find_elements(By.XPATH, Constants.loader_path)) > 0:
        raise ScreenWaitException("Page loader doesn't hide")

def crawl_store(self):
    time.sleep(Constants.wait_for_sec)





