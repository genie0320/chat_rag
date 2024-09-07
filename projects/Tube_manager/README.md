# YouTube manager
This project is a Python-based application designed to help you manage your YouTube subscriptions, track your replies, and organize your playlists. The app provides an easy-to-use interface to access and manage your favorite channels, interact with videos, and curate playlists, all from one place.


## Features

- [WIP] **Subscriptions Management**: View and manage your YouTube subscriptions in a single dashboard.
- [ ] **Replies Tracking**: Easily track and manage replies you've left on videos.
- [ ] **Playlists Management**: Create, edit, delete, and organize your playlists with ease.
- [ ] **YouTube API Integration**: Seamlessly connect to YouTube to access real-time data.
- [ ] **Interactive UI**: A clean and simple interface for smooth navigation and user experience.

## What I learned from
- [Error handling](docs/youtube_error_handling.md) for YouTube authentication process.

## [Prerequisites](https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps#prerequisites)
1. [Enable APIs for your project](https://console.cloud.google.com/apis/dashboard)
2. [Create authorization credentials](https://console.cloud.google.com/apis/credentials)
3. Identify access scopes
4. Install the packages
```python
# for env
> pip install python-dotenv

# for auth
> pip install --upgrade google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
```

## Refs
- [Google api client - github](https://github.com/googleapis/google-api-python-client?tab=readme-ov-file)
- [Youtube data API v.3 Docs](https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html)
- [google cloud console](https://console.cloud.google.com/)

