import urllib.request,json
from .models import Quote

def getQuotes():
    '''
    method that consume API url and return quote object
    '''
    QUOTE_API_URL='http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(QUOTE_API_URL) as url:
        quotesData=url.read()
        quoteResponse= json.loads(quotesData)

        #outputs quote response

        id=quoteResponse.get('id')
        author=quoteResponse.get('author')
        quote=quoteResponse.get('quote')

        quoteObject= Quote(id,author,quote)

        return quoteObject
