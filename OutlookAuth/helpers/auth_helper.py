import yaml
import msal

# Load the oauth_settings.yml file located in your app DIR
stream = open('OutlookAuth/oauth_setttings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)


def get_msal_app(cache=None):
    # Initialize the MSAL confidential client
    auth_app = msal.ConfidentialClientApplication(
        settings['app_id'],
        authority=settings['authority'],
        client_credential=settings['app_secret'],
        token_cache=cache)
    return auth_app


# Method to generate a sign-in flow
def get_sign_in_flow():
    auth_app = get_msal_app()
    return auth_app.initiate_auth_code_flow(
        settings['scopes'],
        redirect_uri=settings['redirect'])
