import logging

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
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


def get_text_from_xpath(self, xpath):
    return self.driver.find_element(By.XPATH, xpath).text


def check_success_response(self):
    wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
    wait.until(EC.element_to_be_clickable((By.XPATH, Constants.store_name_path)))

    if len(self.driver.find_elements(By.XPATH, Constants.loader_path)) > 0:
        raise ScreenWaitException("Page loader doesn't hide")


def crawl_store(self, store_id):
    from db.models import Store
    Store.create(storeId=store_id,
                 storeName=get_text_from_xpath(self, Constants.store_name_path),
                 products=get_text_from_xpath(self, Constants.store_products_count_path),
                 following=get_text_from_xpath(self, Constants.store_following_path),
                 chatPerformance=get_text_from_xpath(self, Constants.store_chat_performance_path),
                 cancellationRate=get_text_from_xpath(self, Constants.store_cancellation_rate_path),
                 joined=get_text_from_xpath(self, Constants.store_joined_path),
                 followers=get_text_from_xpath(self, Constants.store_followers_path),
                 rating=get_text_from_xpath(self, Constants.store_rating_path),
                 about=get_text_from_xpath(self, Constants.store_about_path))
