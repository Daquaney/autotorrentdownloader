# autotorrentdownloader
A python automated torrent downloader that filters out already downloaded torrents.
# About
Automatically downloads torrents from an rss feed and filters out the movies you have downloaded from the ones you don't. Inspiration was from me trying to download from an rss feed but not wanting to get the 720p videos. I looked and couldnt find anything to filter out 720p in my first google search, so I just made this.
# To Do
- Add a timestamp so old torrents get deleted after a period of time
# Installation
1. Install and setup transmission for a web interface here: https://www.smarthomebeginner.com/install-transmission-web-interface-on-ubuntu-1204/. 
2. Clone the repository
```
git clone https://github.com/Daquaney/autotorrentdownloader
```
3. Install requirements
```
cd autotorrentdownloader
pip install -r requirements.txt
```
# Running the project
```
python moviedownloader.py
```
