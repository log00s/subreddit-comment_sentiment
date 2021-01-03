# -*- coding: utf-8 -*-
"""
Description:
    1. Scrape all comments from a given reddit thread
    3. Store in pandas DataFrame

Original Author:
    Copyright (c) Ian Hussey 2016 (ian.hussey@ugent.be) 
    Released under the GPLv3+ license.

Modified by:
    Jack Pashley 2021 (Log0s, me@log0s.tech)

Known issues:
    None. 

Notes:
    1. Although the script only uses publicly available information, 
    PRAW's call to the reddit API requires a reddit login.
    2. Reddit API limits number of calls. 
    For a large thread (e.g., 1000s of comments) script execution time may therefore be c.1 hour.
    3. Because of this bottleneck, the entire data object is written to a pickle before anything is discarded. 
    This speeds up testing etc.
    4. Does not extract comment creation date (or other properties), which might be useful. 
"""
# Dependencies
import praw
import pandas as pd
import os
import csv
import sys
import pickle
import Scraper_config as cfg

r = praw.Reddit(client_id=cfg.client_id, client_secret=cfg.client_secret, user_agent=cfg.bot_username)
if hasattr(cfg, "comment_to_list"):
    comment_to_list = cfg.comment_to_list
else:
    comment_to_list = default_comment_to_list

def default_comment_to_list(comment):
    return [comment.body]

def get_submission_comments(uniq_id, r):
    """Extract the first level comments from a reddit submission.

    Args:
        uniq_id (str): The submission's reddit id. A sequence of numbers and letters.
        r (praw): Reddit client instance

    Returns:
        list: A list of reddit comments.
    """    
    submission = r.submission(id=uniq_id)  # UNIQUE ID FOR THE THREAD GOES HERE - GET FROM THE URL
    submission.comments.replace_more(limit=None, threshold=0)  # all comments, not just first page

    # Save object to pickle
    output = open(cfg.output_file, 'wb')
    pickle.dump(submission, output, -1)
    output.close()

    forest_comments = submission.comments.list()  # get comments tree
    already_done = set()
    all_comments = []
    for comment in forest_comments:
        if comment.id not in already_done:
            already_done.add(comment.id)  # add it to the list of checked comments
            all_comments.append (comment_to_list(comment))  # append to list for saving
        else:
            already_done.add(comment.id)
    return all_comments
 
# Change directory to that of the current script
absolute_path = os.path.abspath(__file__)
directory_name = os.path.dirname(absolute_path)
os.chdir(directory_name)

uniq_id = cfg.uniq_id
all_comments = get_submission_comments(uniq_id, r)

output = pd.DataFrame({'Statement': all_comments})