import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()

def get_proxies():
    '''
    This function makes a GET request to free-proxy-list.net, and scrapes the front page for IP address and port of elite type proxies that support https.
    Returns a list of IP addresses.
    '''
    # set the url for the GET request
    url_base = 'https://free-proxy-list.net/'
    # randomize the user agent sent with request
    real_user_agent = ua.random
    # structure request header
    headers = {'User-Agent': real_user_agent}
    # makes a GET request from the url, and saves it as a bs4 object
    soup = BeautifulSoup(requests.get(url_base,
                                      headers=headers).text,
                         'html.parser')
    # Within the soup, gets each row in the table where proxies are listed
    rows=[]
    for row in soup.findAll("tr"):
        rows.append(row)
    
    # For each row in the table, find the ones that have elite proxy tags and 'Yes' to the https column
    valid_ips = []
    for row in rows:
        i = row.findAll('td')
        try:
            if i[4].text == 'elite proxy' and i[6].text == 'yes':
                # Append each valid IP to a list
                valid_ips.append(i[0].text + ':' + i[1].text)
        except:
            continue
    # return the valid ip addresses
    return valid_ips