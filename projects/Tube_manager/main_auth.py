# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import json
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
    # 여기 파일주소는 꼭 full path를 입력해줘야 한다. 이유는 모름.
    client_secrets_file = "D:\Devn_src\chat_rag\Tube_manager\client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )

    # 로컬에서 실험할 때, 그리고 서비스로 올릴 때는 설정이 다르다.
    # 온라인 사용시 :
    # credentials = flow.run_console()

    # 오프라인 실험시 : 로컬에서 연결이 안되네 어쩌네... 그런 말이 있다면 port 번호를 설정해주면 된다.
    credentials = flow.run_local_server(port=11196)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )

    # request = youtube.search().list(part="snippet", maxResults=25, q="surfing")

    request = youtube.subscriptions().list(part="snippet,contentDetails", mine=True)
    response = request.execute()

    with open("result.json", "w") as f:
        json.dump(response, f, indent=4)


if __name__ == "__main__":
    main()
