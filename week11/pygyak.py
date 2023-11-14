import urllib.request


def get_page(url):
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")

    return html
