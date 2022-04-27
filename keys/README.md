# Keys
While for our final approach we finally didn't use twitter API to download tweets for this project, we follow the complete process to get a Twitter developer's account, and want to share this experience.

The very first step to use the twitter API, is to apply for a [Twitter's developer account](https://developer.twitter.com/en/apply-for-access).

If you don't know where to start or what you should write in the request to get a Twitter developer account, we recomend to look these resources:
- [Twitter API Data Collection](https://youtu.be/Jl-_dDqSaUQ?t=59) by Stevesie Data, see from 0:59 to 1:44 minute.
- [Example of the Twitter Developer Account Application Process](https://wptweetboost.com/example-of-the-twitter-developer-account-application-process/) by Hudson Atwell.

After the developer account application gets approved, you will find your authenication keys in [this link](https://developer.twitter.com/en/apps), where you will find your keys: `API key`, `API secret key`, `Access token` and `Access token secret`.

In the [witter-search_v1_TwitterAPI.ipynb](https://github.com/vcuspinera/Canada_response_covid/blob/master/src/twitter-search_v1_TwitterAPI.ipynb) Jupyter notebook, we share our very first attempt to download the tweets of this project using our personal Twitter's keys; however, if you want to run this code, you will need to clone the repo and add your authentication keys in [the `twitter_config.py` file](https://github.com/vcuspinera/Canada_response_covid/blob/master/keys/twitter_config.py).
