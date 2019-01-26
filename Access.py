from requests_oauthlib import OAuth1Session
import webbrowser

class Access:

    def __init__(self):

        #Consumer key's
        self.consumer_key = ''
        self.consumer_secret = ''

        #Create oAuth client
        oauth_client = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret, callback_uri='oob')

        #Try to request a temporal token for accessing the twitter app
        try:
            resp = oauth_client.fetch_request_token('https://api.twitter.com/oauth/request_token')
        except ValueError as e:
            raise 'Error response from Twitter requesting temp token: {0}'.format(e)

        #If everything is okey, call the twitter auth URL
        url = oauth_client.authorization_url('https://api.twitter.com/oauth/authorize')
        print('URL for obtaining the pincode is: ' + url)

        #Open url automarically in the default browser
        webbrowser.open(url)

        #Request user to copy/paste the pincode. Note that we can also do Web scraping in order to get
        #the pin automatically from the webpage,
        pincode = input('\nCopy/Paste the pincode from the web browser: ')

        #Make oauth
        oauth_client = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret, resource_owner_key=resp.get('oauth_token'),
                                     resource_owner_secret=resp.get('oauth_token_secret'), verifier=pincode)
        try:
            resp = oauth_client.fetch_access_token('https://api.twitter.com/oauth/access_token')
        except ValueError as e:
            raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)

        #Acces the accesToken and the TokenSecret from the response:
        self.atk = resp.get('oauth_token')
        self.ats = resp.get('oauth_token_secret')


#Instanciate this class in order to access from external classes
obj = Access()



