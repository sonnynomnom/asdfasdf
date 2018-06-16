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
