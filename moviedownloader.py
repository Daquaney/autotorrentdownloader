# made by tristan edwards
import feedparser
import transmissionrpc
url = 'https://thepiratebay.org/rss/top100/207'
tc = transmissionrpc.Client('192.168.1.91', port=9091)


def link_in_db(link_db):
    with open('magnets.txt', 'r') as database:
        for line in database:
            if link_db in line:
                return True
    return False


feed = feedparser.parse(url)
links_to_grab = []
links_to_skip = []

for link in feed.entries:
    link = link.link
    if link_in_db(link):
        links_to_skip.append(link)
    else:
        links_to_grab.append(link)

link_file = open('magnets.txt', 'a')
for link in links_to_grab:
    if not link_in_db(link):
        if '720p' in link:
            continue
        link_file.write(link + "\n")
link_file.close()

for link in links_to_grab:
    if '720p' in link:
        continue
    print(link)
    tc.add_torrent(link)
