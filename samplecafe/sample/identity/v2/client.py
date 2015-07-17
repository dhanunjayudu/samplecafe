from cafe.engine.http.client import AutoMarshallingHTTPClient

from sample.identity.v2.models import requests, responses


class IdentityV2Client(AutoMarshallingHTTPClient):
    def __init__(
        self, url, token=None, serialize_format="json",
            deserialize_format="json"):
        super(IdentityV2Client, self).__init__(
            serialize_format, deserialize_format)
        self. url = url
        self.token = token
        self.default_headers = {
            "x-auth-token": self.token,
            "Content-Type": "application/{ct}".format(ct=serialize_format),
            "Accept": "application/{accept}".format(accept=deserialize_format)}

    def authenticate(
        self, username=None, password=None, api_key=None, tenant_id=None,
            requestslib_kwargs=None):
        password_creds = (
            requests.PasswordCredentials(username, password)
            if password is not None else None)
        api_creds = (
            requests.APIKeyCredentials(username, api_key)
            if api_key is not None else None)
        model = requests.AuthenticateRequest(
            password_creds, api_creds, tenant_id)
        url = "{url}/tokens".format(url=self.url)
        return self.post(
            url, request_entity=model, requestslib_kwargs=requestslib_kwargs,
            response_entity_type=responses.AuthenticateResponse)
