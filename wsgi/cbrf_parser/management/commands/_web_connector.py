__author__ = 'Alexey'

import urllib.request
import urllib.error

class web_connector:

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    def open_with_authentication(self, web_address):
        address_port = urllib.request.getproxies()['http']
        address_port = address_port.split("http://")[1]
        proxy = urllib.request.ProxyHandler({'http': r'http://'+self.login+':'+self.password+'@'+address_port})
        authentication = urllib.request.HTTPBasicAuthHandler()
        opener = urllib.request.build_opener(proxy, authentication, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        page = urllib.request.urlopen(web_address)
        return page

    def open_page(self, web_address):
        try:
            page = urllib.request.urlopen(web_address)
        except urllib.error.HTTPError as e:
            if e.code==407:
                try:
                    page = self.open_with_authentication(web_address)
                except:
                    raise IOError("Error:",e,"; can't open page", web_address)
                    return None
            else:
                raise IOError("Error:",e,"; can't open page", web_address)
                return None
        return page

