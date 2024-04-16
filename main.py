from google.oauth2 import service_account
from google.auth.transport.requests import Request


SERVICE_ACCOUNT_INFO = {
  // Account Info Goes here
}

 
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']

def get_access_token():
     
    credentials = service_account.Credentials.from_service_account_info(
        SERVICE_ACCOUNT_INFO,
        scopes=SCOPES
    )
 
    credentials.refresh(Request())

 
    return credentials.token

 
print("Your access token is: ", get_access_token())
