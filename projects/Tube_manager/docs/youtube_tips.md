# Things I wish I had known when I started.

## Awesome tutorial to start with
- [Python YouTube API Tutorial: Getting Started - Creating an API Key and Querying the API(by Corey Schafer)](https://www.youtube.com/watch?v=th5_9woFJmk)

### Bolier plate code
```python
# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    # - for server
    credentials = flow.run_console() 
    # - for local use
    # credentials = flow.run_local_server(port=xxx)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
```

### Tips to know.
[YouTube Data API v3](https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html)
**The daily API quota is 10,000 requests**
- Each request has different API consumption. Check it here.
    [YouTube Data API (v3) - Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)
- You can check [real-time API usage](https://console.cloud.google.com/apis/dashboard).
- It is possible to [request an increase in quota](https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits) (though I haven’t tested this myself, yet).