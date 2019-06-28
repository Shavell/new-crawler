import os

from PIL import Image

from mllib.predict import Predictor
from util import *

logger = logging.getLogger(__name__)

class ImageExtractor():
    def translate_captcha(img_path):
        man = Predictor('trained')
        return man.identify(img_path)

    def get_captcha(self, element, path):
        location = element.location
        size = element.size

        if not os.path.exists(Constants.captcha_path):
            os.mkdir(Constants.captcha_path)

        self.driver.save_screenshot(path)
        image = Image.open(path)

        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        image = image.crop((left + 1, top, right + 1, bottom))  # defines crop points
        image.save(path, format='png', dpi=(300,300))