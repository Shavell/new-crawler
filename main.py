import shutil
import unittest

from selenium import webdriver

from util import *

logger = logging.getLogger(__name__)


class Main(unittest.TestCase):

    def setUp(self):
        if shutil.which('phantomjs') is not None and Constants.use_phantomjs:
            self.driver = webdriver.PhantomJS()
            self.driver.set_window_size(1120, 550)
        else:
            options = webdriver.ChromeOptions()
            if Constants.use_headless_chrome:
                options.add_argument('headless')
            self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
        models.db.connect()
        self.test_id = fill_start_test_query(start=datetime.now())

    def tearDown(self):
        self.driver.quit()
        models.db.close()

    def check_tracking(self, err=False):
        driver = self.driver
        driver.get(Constants.url)
        tracking_codes = models.TrackingCode.select().where(models.TrackingCode.active == True)

        for code in tracking_codes:
            with self.subTest(code=code.tracking_id):
                barcode = code.tracking_id
                start = datetime.now()
                extracted_captcha_key = default_scenario(self, barcode)

                try:
                    check_success_response(self)
                except CaptchaErrorException as error:
                    logger.error("Captcha is wrong! tracking_code: {}".format(barcode))
                    fill_test_action_to_db(err, barcode, extracted_captcha_key, start, error, self.test_id)
                    default_scenario(self, barcode)
                except ScreenWaitException:
                    time.sleep(Constants.wait_for_sec)
                    logger.info("Screen is waiting! 5 sec. after call refresh ")
                    self.driver.refresh()
                except BarcodeErrorException as error:
                    logger.error("Barcode is wrong !")
                    err = True
                    fill_test_action_to_db(err, barcode, extracted_captcha_key, start, error, self.test_id)
                    self.assertFalse(error)
                except Exception as error:
                    err = True
                    fill_test_action_to_db(err, barcode, extracted_captcha_key, start, error, self.test_id)
                    self.assertFalse(error)

                action_id = fill_test_action_to_db(err, barcode, extracted_captcha_key, start, "", self.test_id)
                fill_test_result_to_db(self, action_id)

        assert err is not True


if __name__ == "__main__":
    unittest.main()
