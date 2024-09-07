# %%
import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


def conn_yt_auth():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = r"projects\Tube_manager\client_secret.json"
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )

    credentials = flow.run_local_server(port=11196)

    return googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )


def saveToFile(contents, file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8-sig") as f:
            json.dump(contents, f, indent=4, ensure_ascii=False)
    else:
        with open(file_name, "r", encoding="utf-8-sig") as f:
            new_contents = json.load(f)

        new_contents["items"].extend(contents["items"])

        with open(file_name, "w", encoding="utf-8-sig") as f:
            json.dump(new_contents, f, indent=4, ensure_ascii=False)

    print("file saved")


def get_playlist(pageToken):
    request = youtube.subscriptions().list(
        part="snippet,contentDetails",
        mine=True,
        maxResults=50,  # 5~50
        pageToken=pageToken if pageToken else None,
    )
    return request.execute()


def getItemCount(file_name):
    with open(file_name, "r", encoding="utf-8-sig") as f:
        items = json.load(f)
    return len(items["items"])


def getTitles(file_name):
    with open(file_name, "r", encoding="utf-8-sig") as f:
        items = json.load(f)
    return [item["snippet"]["title"] for item in items["items"]]


if __name__ == "__main__":
    youtube = conn_yt_auth()
    # %%
    nextPageToken = None
    result_file = r"projects\Tube_manager\result.json"
    while True:
        response = get_playlist(nextPageToken)
        saveToFile(response, result_file)
        nextPageToken = response["nextPageToken"]

        print(nextPageToken)

        if nextPageToken == None:
            print(response)
            break

    print(len(getTitles(result_file)))
