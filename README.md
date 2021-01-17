# Proxyscraper Demo

### by Griffin Hundley

## Info

This is a lightweight script I wrote for a previous data collection project.  It makes a GET request to free-proxy-list.net, parses the HTML for https elite proxies, and returns them as a list.  Proxies are useful because they can mask the identity of the original user, and bypass certain network restrictions.  Making too many requests from a particular IP address, or performing automated requests, can get that IP address blocked.  The use of proxies and spoofed user agents can alleviate these concerns.

The following packages are used:

fake_useragent - to simulate a headed browser

BeautifulSoup4 - to parse the HTML

Requests - to make a GET request