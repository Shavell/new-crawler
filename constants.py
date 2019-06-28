
class Constants():
    app_name = "Test App"
    wait_for_sec = 5
    use_phantomjs = False
    use_headless_chrome = False
    url = 'http://gonderitakip.ptt.gov.tr/'
    barkod_id = 'barkod'
    security_id = 'security_code'
    security_image_path = "//td[@class='dataCell']/table[@class='table80']//img"
    sorgula_button = "//input[@name='Submit']"
    captcha_way = "captchas/captcha.png"
    captcha_path = "captchas"
    invalid_barkod_path = "//body/div[2]/h3[.='Barkod Numarasinda hata var:']"
    invalid_captcha_path = "//body/div[2]/h3[contains(text(), 'Güvenlik kodu hatalı girilmiştir. Lütfen tekrar deneyiniz.')]"
    wait_page_path = "//td[@class='dataCell'][contains(text(), 'Lüfen biraz bekleyip sayfayı tekrar güncelleyin.')]"

    last_process_comment_xpath = '//*[@id="pathway"]/ul/li/table/tbody/tr[9]/td[1]/div'
    last_process_date_xpath = '//*[@id="pathway"]/ul/li/table/tbody/tr[9]/td[2]/div'
    delivery_comment_xpath = '//*[@id="pathway"]/ul/li/table/tbody/tr[1]/td[1]/div[. !=""]'

    fee_table_xpath = "//li/table/../../../../h2[text()='ÜCRETLER']/..//table"
    _fee_table_xpath = "//form[@name='form']/div[3]//div[@id='pathway']//table[@border='0']"
    total_fee_xpath = "//body[@class='yjsgbody']/form[@name='form']/div[3]//div[@id='pathway']//table/tbody/tr[6]/td"

    # delivery_actions_xpath = "//li/table/../../../../h2[text()='GÖNDERİNİN HAREKETLERİ ']/..//table[@border='1']" # not working on selenium but if u want to check on browser any problem of that xpath

    list_of_table_xpath = "//li/table[@border='1']"
