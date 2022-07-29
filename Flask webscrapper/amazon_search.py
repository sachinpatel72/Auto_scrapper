# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:25:41 2021

@author: win10
"""

from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=iphones"

wanted_list=["58,400","Apple iPhone 11 (128GB) - Black"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))



scraper.set_rule_aliases({'rule_yd4cj':'Title'})
scraper.keep_rules(['rule_yd4c'])
scraper.save('amazon-search')