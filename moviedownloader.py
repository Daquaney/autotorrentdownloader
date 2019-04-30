# made by tristan edwards
import feedparser
import transmissionrpc
# rss feed
url = 'https://thepiratebay.org/rss/top100/207'
# transmission client setup
tc = transmissionrpc.Client('localhost', port=9091)

# to check if magnet is in the database of magnets
def magnet_in_db(magnet):
    with open('magnets.txt', 'r+') as database:
        for line in database:
            if magnet in line:
                return True
    return False


feed = feedparser.parse(url)
magnets_to_print = []
magnets_to_skip = []
# if magnet already exists in database do nothing, otherwise add the magnet to the database
for magnet in feed.entries:
    magnet = magnet.link
    if magnet_in_db(magnet):
        magnets_to_skip.append(magnet)
    else:
        magnets_to_print.append(magnet)
# write to the database
magnet_file = open('magnets.txt', 'a+')
for magnet in magnets_to_print:
    if not magnet_in_db(magnet):
        if '720p' in magnet:
            continue
        magnet_file.write(magnet + "\n")
        print(magnet)
        tc.add_torrent(magnet)
magnet_file.close()
