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

```py
twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
```

```py
handle = "@kanyewest"
statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
```

```py
for status in statuses:
  print status.text
```
