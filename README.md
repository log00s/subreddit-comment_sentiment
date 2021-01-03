Sentiment analysis of a reddit submission's comments <!-- omit in toc -->
====================================
VADER Sentiment analysis of all comments on a reddit submission. Licensed under GPLv3+

- [Example setup and use case](#example-setup-and-use-case)
- [Dependencies, credits](#dependencies-credits)
- [License](#license)

## Example setup and use case
1. Go to https://ssl.reddit.com/prefs/apps/ to create a reddit bot, and add the credentials on lines 11,12,13 of `Scraper_config.py`
2. Set a unique id for a submission on line 18. 
   - E.g. The unique id for https://www.reddit.com/r/funny/comments/5gn8ru/guardians_of_the_front_page/?ref=share&ref_source=link is `5gn8ru`
3. In `main.py`, you can change what will happen with the output. By default, it prints to the terminal. 

## Dependencies, credits
- Pandas
- Praw
- vaderSentiment
- pickle

## License
Licensed under GPLv3+