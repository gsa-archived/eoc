from urllib.request import urlopen
from urllib.error import *

def check_link(x):
    try:
        html = urlopen(x)
    
    except HTTPError as e:
        print('HTTP error - \n{}'.format(e))
        
    except URLError as e:
        print('URL Error - \n{}'.format(e))

    else:
        print('it worked')