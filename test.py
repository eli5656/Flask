from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class test(unittest.TestCase):
    def test_selenium(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get('http://127.0.0.1:5000/?username=alex')
        body = driver.find_element(By.XPATH, "/html/body")
        list = body.text.split("Hello ")
        list[:] = [x for x in list if x]
        fullname = " ".join(list)
        url = driver.current_url
        name_in_url = url[url.find("username=") + len("username="):]
        self.assertEqual(fullname, name_in_url, "name of url and name in DOM is not same")


if __name__ == "__main__":
    unittest.main()
