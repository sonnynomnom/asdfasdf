# Celebrity Match

install packages:

```bash
$ pip install python-twitter
$ pip install watson-developer-cloud
```

verify that packages installed correctly:

```bash
$ pip freeze
```

```py
import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
```

```py
twitter_consumer_key = ''  
twitter_consumer_secret = ''  
twitter_access_token = ''  
twitter_access_secret = ''
```

```
twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
```
