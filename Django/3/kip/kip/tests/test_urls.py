from django.test import TestCase
from mybackend  import functions
from selenium import webdriver
import re


class SiteUrlTest(TestCase):
    def test_URLs(self):
        print('-------------------------------- URL TEST ------------------------------')
        browser = webdriver.Chrome()
        try:

            sitemap = 'http://127.0.0.1:8000/sitemap.xml'
            browser.get(sitemap)
            sitemap_content = browser.page_source
            content_list = sitemap_content.split('<loc>')
            for cl in content_list:
                if re.search('</loc', cl):
                    currentUrl = re.split('</loc', cl)[0]

                    browser.get(currentUrl)
                    print('%s - good' % currentUrl)

        except Exception as e:
            e_message = e.message if hasattr(e, 'message') else ','.join(map(str, e.args))
            print(currentUrl)
            print(e_message)

        browser.close()
