import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


def get_auth(client_secret, scopes):
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = client_secret
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )

    credentials = flow.run_local_server(port=11196)

    return googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )
