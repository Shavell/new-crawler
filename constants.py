import os


class Constants():
    app_name = "Shopee Crawler"
    wait_for_sec = 5 # Wait after finish per crawl
    use_phantomjs = False # False Default
    use_headless_chrome = False
    # TODO: Change according to which operating system you are using
    chrome_driver = os.path.join(os.path.dirname(__file__), 'chromedriver') # For windows change to 'chromedriver.exe'

    # Url Definitions
    urlPrefix = 'https://shopee.ph/shop/'
    allProductsPostfix = '/search'
    searchPageWithPagingParameter = '/search?page={}&sortBy=pop'

    # Selenium Definitions
    product_per_page = 30
    start_page = 1
    searchPageStartWith = 0
    loader_path = '//div[contains(@class,"stardust-spinner")]'

    # XPath Definitions

    # Store Page
    store_name_path = '//div[@role="main"]//h1'
    store_about_path = '//div[@class="shop-page-shop-description"]/span'
    store_products_count_path = '/html//div[@id="main"]/div//div[@role="main"]/div[@class="shop-page__info"]/div/div[2]/div[1]/div[2]/div[2]'
    store_following_path = '/html//div[@id="main"]/div//div[@role="main"]/div[@class="shop-page__info"]/div/div[2]/div[2]/div[2]/div[2]'
    store_chat_performance_path = '/html//div[@id="main"]/div//div[@role="main"]/div[@class="shop-page__info"]/div/div[2]/div[3]/div[2]/div[2]'
    store_cancellation_rate_path = '/html//div[@id="main"]/div//div[@role="main"]/div[@class="shop-page__info"]/div/div[2]/div[4]/div[2]/div[2]'
    store_followers_path = '/html//div[@id="main"]/div//div[@role="main"]/div[@class="shop-page__info"]/div/div[2]/div[5]/div[2]/div[2]'
    store_rating_path = '/html//div[@id="main"]/div//div[@role="main"]/div[@class="shop-page__info"]/div/div[2]/div[6]/div[2]/div[2]'
    store_joined_path = '/html//div[@id="main"]/div//div[@role="main"]/div[@class="shop-page__info"]/div/div[2]/div[7]/div[2]/div[2]'

    # Products Page

    search_items_path = '/html//div[@id="main"]/div//div[@role="main"]//div[@class="row"]/div'
    search_next_button_path = '//button[@class="shopee-button-outline shopee-mini-page-controller__next-btn"]'