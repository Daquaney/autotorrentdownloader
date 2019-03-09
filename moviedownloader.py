# made by tristan edwards
import feedparser
import transmissionrpc
# rss feed of top 100 movie torrents
url = 'https://thepiratebay.org/rss/top100/207'
# transmission client setup input ip!!!
tc = transmissionrpc.Client('IP HERE!!!', port=9091)

# to check if link is in the database of magnets
def link_in_db(link):
    with open('magnets.txt', 'r') as database:
        for line in database:
            if link in line:
                return True
    return False


feed = feedparser.parse(url)
links_to_print = []
links_to_skip = []
# if magnet already exists in database do nothing, otherwise add the link to the database
for link in feed.entries:
    link = link.link
    if link_in_db(link):
        links_to_skip.append(link)
    else:
        links_to_print.append(link)
# write to the database
link_file = open('magnets.txt', 'a')
for link in links_to_print:
    if not link_in_db(link):
        if '720p' in link:
            continue
        link_file.write(link + "\n")
link_file.close()
# if the link is 720p skip, otherwise start downloading the torrent
for link in links_to_print:
    if '720p' in link:
        continue
    print(link)
    tc.add_torrent(link)
