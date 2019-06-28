import logging
import time
from datetime import datetime

import pandas as pd
from beautifultable import BeautifulTable
from selenium.webdriver.common.by import By

from constants import Constants
from db import models
from exceptions import *
from extract_image import ImageExtractor

logging.basicConfig(level=logging.INFO)  # move to log.py
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
fh = logging.FileHandler('logs.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


def default_scenario(self, barcode):
    logger.info('start test with tracking id: {}'.format(barcode))
    time.sleep(Constants.wait_for_sec)
    barcode_input = self.driver.find_element(By.ID, Constants.barkod_id)
    security_input = self.driver.find_element(By.ID, Constants.security_id)
    query_button = self.driver.find_element(By.XPATH, Constants.sorgula_button)
    security_image = self.driver.find_element(By.XPATH, Constants.security_image_path)

    barcode_input.send_keys(barcode)

    ImageExtractor.get_captcha(self, security_image, Constants.captcha_way)
    extracted_captcha_key = ImageExtractor.translate_captcha(Constants.captcha_way)
    security_input.send_keys(extracted_captcha_key)
    query_button.submit()
    return extracted_captcha_key


def check_success_response(self):
    if (len(self.driver.find_elements(By.XPATH, Constants.invalid_barkod_path)) == 0 |
            len(self.driver.find_elements(By.XPATH, Constants.invalid_captcha_path)) |
            len(self.driver.find_elements(By.XPATH, Constants.wait_page_path)) == 0):
        return True
    elif len(self.driver.find_elements(By.XPATH, Constants.invalid_barkod_path)) > 0:
        raise BarcodeErrorException("Barcode Error")
    elif len(self.driver.find_elements(By.XPATH, Constants.invalid_captcha_path)) > 0:
        raise CaptchaErrorException("Captcha Error")
    elif len(self.driver.find_elements(By.XPATH, Constants.wait_page_path)) > 0:
        raise ScreenWaitException("Screen is waiting error")


def fill_test_action_to_db(err, barcode, key, start, err_desc, transaction_id):
    return models.LogAction.create(tracking_code=barcode, captcha_key=key, start=start, err=err, err_desc=err_desc,
                                   log_test_transaction=transaction_id).id


def fill_test_result_to_db(self, log_action_id):
    last_process_comment = self.driver.find_element(By.XPATH, Constants.last_process_comment_xpath)
    last_process_date = self.driver.find_element(By.XPATH, Constants.last_process_date_xpath)
    delivery_comment = self.driver.find_element(By.XPATH, Constants.delivery_comment_xpath)

    self.actions = None
    self.fee = None
    self.total_fee = None

    delivery_actions = self.driver.find_elements(By.XPATH, Constants.list_of_table_xpath)[2]
    fee_table = self.driver.find_elements(By.XPATH, Constants._fee_table_xpath)

    if len(fee_table):
        self.fee = extract_df_from_element(fee_table[0])
        self.total_fee = self.driver.find_element(By.XPATH, Constants.total_fee_xpath).text

    self.actions = extract_df_from_element(delivery_actions)

    models.LogResult.create(last_process_comment=last_process_comment.text, last_process_date=last_process_date.text,
                            delivery_comment=delivery_comment.text, total_fees=self.total_fee,
                            all_actions_result=self.actions, all_fees=self.fee, log_action=log_action_id)


def extract_df_from_element(element):
    return pd.read_html(element.get_attribute("outerHTML"))[0].dropna(axis=0, thresh=4).to_json()


def fill_start_test_query(start):
    return models.LogTestTransaction.create(start=start, end=datetime.now()).id


def print_result(headers, result):  # TODO: implement!
    table = BeautifulTable()
    table.column_headers = headers
    for row in result:
        table.append_row(row)
    print(table)
