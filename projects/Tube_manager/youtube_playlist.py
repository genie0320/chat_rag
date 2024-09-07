# %%
import os
import json

import get_youtube

SECRETS = r"projects\Tube_manager\client_secret.json"
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


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


def getPlaylist(pageToken):
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
    youtube = get_youtube.get_auth(SECRETS, scopes)

    nextPageToken = None
    result_file = r"projects\Tube_manager\result.json"

    while True:
        response = getPlaylist(nextPageToken)
        saveToFile(response, result_file)
        nextPageToken = response["nextPageToken"]

        print(nextPageToken)

        if nextPageToken == None:
            print(response)
            break

    print(len(getTitles(result_file)))
