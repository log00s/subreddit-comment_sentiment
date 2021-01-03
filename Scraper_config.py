# -*- coding: utf-8 -*-
"""
Description:
    config for the Scraper.py
"""
# create a reddit personal use script and enter the credentials here https://ssl.reddit.com/prefs/apps/
client_id = ""
client_secret = ""
bot_username = ""

output_file = "scraped_data.pkl"

# Set unique id
uniq_id = ''

def comment_to_list(comment):
    return comment.body