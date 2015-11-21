# -*- coding: latin-1 -*-
# Author: elnerude

from bs4 import BeautifulSoup
from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import traceback
import re
import requests
import urllib2
import json
import sys
import urllib

log = CPLog(__name__)

class libertalia(TorrentProvider, MovieProvider):

    urls = {
        'base_url': 'https://libertalia.me',
        'search': 'https://libertalia.me/torrents.php?name=%s&cat%%5B%%5D=3.2&cat%%5B%%5D=3.3&cat%%5B%%5D=4.2&cat%%5B%%5D=4.3&cat%%5B%%5D=12.2&cat%%5B%%5D=12.3',
        'login': 'https://libertalia.me/login.php'
    }

    def getLoginParams(self):
        log.debug('Getting login params for libertalia')
        return {
            'username': self.conf('username'),
            'password': self.conf('password'),
            'submit' : 'Connexion'
        }

    def loginSuccess(self, output):
        loginFailPassphrase = 'mot de passe est incorrect'
        log.debug('Checking login success for libertalia: %s' % ('True' if not (loginFailPassphrase in output.lower()) else 'False'))
        return not loginFailPassphrase in output.lower()

    def _searchOnTitle(self, title, movie, quality, results):
        #log.debug("movie %s" % movie)
        #log.debug("quality %s" % quality)
        titleClean = title
        #search on 
        if len(titleClean) > 5 and (titleClean.startswith("the ") or titleClean.startswith("The ") or titleClean.startswith("les ") or titleClean.startswith("Les ")):
            titleClean = titleClean[4:]
        titleClean = titleClean + " " + str(movie['info']['year'])
        search_url = self.urls['search'] % titleClean.encode('utf-8')

        data = self.getHTMLData(search_url, cache_timeout = 30)
        if not data:
            log.error("Failed fetching data. Traceback: %s" % traceback.format_exc())
            return

        try:
            html = BeautifulSoup(data, features=["html", "permissive"])
            result_table = html.find("table", {"class" : "torrent_table"})

            if not result_table:
                log.debug("Data returned from provider does not contain any torrents")
                return

            if result_table:
                rows = result_table.findAll("tr", {"class" : "torrent_row"})
                log.debug("Found %d results for search %s" % (len(rows), titleClean))
                for row in rows:

                    columns = row.find('td', {"class" : "torrent_name"})
                    link = columns.find("a", href=re.compile("torrents"))

                    if link:
                        try:
                            result_title = link.text.encode("utf-8")
                            idt = link['href'].replace('torrents.php?id=','').replace('/','')
                            detail_url = self.urls['base_url'] + "/" + link['href']
                            download_url = row.find("a", href=re.compile("torrent_pass"))['href']
                        except (AttributeError, TypeError):
                            return

                        try:
                            seeders = int(row.find('td', {"class" : "seeders"}).text)
                            leechers = int(row.find('td', {"class" : "leechers"}).text)
                            size = self.parseSize(row.find('td', {"class" : "nobr"}).text)
                        except Exception:
                            log.debug("Unable to parse torrent id & seeders & leechers. Traceback: %s " % traceback.format_exc())
                            return

                        if not all([result_title, download_url]):
                            return

                        item = title, download_url, size, seeders, leechers

                        result = {
                            'id': idt,
                            'name' : result_title,
                            'url' : download_url,
                            'detail_url' : detail_url,
                            'size' : size,
                            'seeders' : seeders,
                            'leechers' : leechers
                            }

                        log.debug("Found result: %s" % result)

                        results.append(result)

        except Exception, e:
            log.error("Failed parsing provider. Traceback: %s" % traceback.format_exc())

