# -*- coding: utf-8 -*-
"""
Description:
    1. Receives a DataFrame with sentences from the Scraper module by Ian Hussey
    2. Classifies the sentences according to vaderSentiment

Author:
    Copyright (c) Jack Pashley 2021 (me@log0s.tech) 
    Released under the GPLv3+ license.

Known issues:
    None. 

"""
# Dependencies 
import Scraper
from classify import classify

OUTPUT = Scraper.output
COLUMN_WITH_SENTENCES_INDEX = 0 # Set the column index that has all of the sentence data

# Classification Here 
OUTPUT = classify(OUTPUT, COLUMN_WITH_SENTENCES_INDEX)

print(OUTPUT)