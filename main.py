import shutil
import time
import unittest

from selenium import webdriver

from libs import models
from libs.util import *

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
            self.driver = webdriver.Chrome(executable_path=Constants.chrome_driver, options=options)
        models.db.connect()

    def tearDown(self):
        self.driver.quit()
        models.db.close()

    def test_doit(self):
        driver = self.driver
        from libs.models import StoreId
        store_ids = StoreId.select().where(models.StoreId.done == False)
        if StoreId.select().where(StoreId.done == False).count() == 0:
            print('There is no one undone test!')
        for store_id in store_ids:
            with self.subTest(comment=store_id.comment):
                driver.get(store_id.storeUrl)
                try:
                    check_success_response(self)
                except ScreenWaitException:
                    time.sleep(Constants.wait_for_sec)
                    logger.info("Page is loading! 5 sec. for refresh")
                    time.sleep(Constants.wait_for_sec)
                except InvalidStoreUrlException as error:
                    logger.error("StoreUrl is wrong !")
                    self.assertFalse(error)
                except Exception as error:
                    self.assertFalse(error)
                crawl_store(self, store_id)


if __name__ == "__main__":
    unittest.main()
