import requests
import os
import re
from jupyterhub.auth import Autehnticator

prints('Start: File Level Authentication.authenticate')

class SSoAuthenticataor(Authenticator):
  sync def authenticate(self,handler,data=None):
    url = os.getenv('URL of Service that will authenticate')
    try:
      #extract the cookie being generated 
      session = handler.cookies["COOKIE"].value
      # where "COOKIE" is the name of the COOKIE that was returned as response and which should be used to authenticate the user.
      # Every request first gets to SSO where a cookie gets generated and then the cookie in the session is used to identify the user details and their authorisation is verified against 
      # an authentication service
      response = requests.get(url, cookies={"COOKIE":session})
      print("Authorisation Service Status Code Response:" + str(response.status_code))
      print("Authorisation service content response:" + str(response.text))
      userid = self.sanitize(response.text)
      if response.status_code== 200:
        return(
          'name': userid,
          'auth_state':{
            'access_token': userid},
          }
       else:
          return None
    except KeyError as e;
          print("Missing cookie in the session")
          return None
     except Exception as e:
          print("Error"(
            return None
            
            
          
