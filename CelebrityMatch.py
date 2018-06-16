import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

user_handle = "@codecademy"
celebrity_handle = "@kanyewest"

def analyze(handle):

  # This code should include the Twitter credentials, IBM credentials, #statuses, and Personality Insights results

  twitter_consumer_key = '28MOCyLip8zTM5wckvJu1Xsaz'
  twitter_consumer_secret = 'KIheGxiS8yq1AjqGt3XUhr5ZbLbeU1dKrxv3e2m3hhaYD63IxO'
  twitter_access_token = '543851212-rW60OrvF40urRIVyWSkb0fHbWGq0q7RsUZUk1mhn'
  twitter_access_secret = 'YzpfBbOgZYz5d2Sk6QqhRcw6rIuZh8RYRZwwWpG26vgte'

  twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

  statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

  # Python 2: text = ""
  text = []

  for status in statuses:

    if (status.lang =='en'): # English tweets

      # Python 2: text += status.text.encode('utf-8')
      text.append(status.text)

      # The IBM Bluemix credentials for Personality Insights!

      pi_username = 'ae0335e6-0936-4314-a178-9d997f2ca16f'
      pi_password = 'jCybPYvdPk2J'

      personality_insights = PersonalityInsights(username=pi_username, password=pi_password)

      # Python 2: pi_result = personality_insights.profile(text)
      pi_result = personality_insights.profile(
        ' '.join(text).encode('utf8'),
        content_type='text/plain; charset=utf-8'
      )

def flatten(orig):

  data = {}

  for c in orig['tree']['children']:
    if 'children' in c:
      for c2 in c['children']:
        if 'children' in c2:
          for c3 in c2['children']:
            if 'children' in c3:
              for c4 in c3['children']:
                if (c4['category'] == 'personality'):
                  data[c4['id']] = c4['percentage']
                  if 'children' not in c3:
                    if (c3['category'] == 'personality'):
                      data[c3['id']] = c3['percentage']

  return data

def compare(dict1, dict2):

  compared_data = {}

  for keys in dict1:
    if dict1[keys] != dict2[keys]:
      compared_data[keys]=abs(dict1[keys] - dict2[keys])

  return compared_data

user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)

# First, flatten the results from the Watson PI API

user = flatten(user_result)
celebrity = flatten(celebrity_result)

# Then, compare the results of the Watson PI API by calculating the distance between traits

compared_results = compare(user,celebrity)

sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

for keys, value in sorted_result[:5]:
  print keys,
  print (user[keys]),
  print ('->'),
  print (celebrity[keys]),
  print ('->'),
  print (compared_results[keys])
