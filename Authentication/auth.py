from urllib.parse import unquote

from google_auth_oauthlib.flow import Flow


def OAuthCall(SCOPES):
  creds = None

  #Ensure that the redirect_uri matches the one on client_secret.json
  #If it does not, then the auth_url will return a redirect_uri mismatch error when accessed
  flow = Flow.from_client_secrets_file(
      'Packages/client_secret.json',
      scopes=SCOPES,
    redirect_uri='https://OMDSPythonRepl.iddiche.repl.co')
  auth_url, _ = flow.authorization_url(prompt='consent')

  print(f'Please go to this URL: {auth_url}')
  code = input('\nEnter the authorization code: ')

  #decode percent-encoded sequences into Unicode characters
  #May not be necessary depending on the code returned.
  #I suggest not removing this unless it's certain that the auth code is not % encoded.
  flow.fetch_token(code=unquote(code)) 
  
  creds = flow.credentials
  print('Auth success\n')

  #Returns the generated credentials
  return creds


if __name__ == "__main__":
  OAuthCall(SCOPES)
