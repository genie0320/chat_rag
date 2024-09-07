import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()


def main(GOOGLE_API):
    yt = build("youtube", "v3", developerKey=GOOGLE_API)
    request = yt.channels().list(part="statistics", forUsername="schafer5")

    response = request.execute()
    yt.close()

    return response


if __name__ == "__main__":
    GOOGLE_API = os.environ.get("GOOGLE_API_KEY_R")
    print(main(GOOGLE_API))
