from sample.identity.v2.client import IdentityV2Client
from sample.identity.config import IdentityConfig


class IdentityComposite(object):
    def __init__(self, config=None):
        self.config = config or IdentityConfig()
        self.client = IdentityV2Client(
            self.config.url, serialize_format=self.config.serialize_format,
            deserialize_format=self.config.deserialize_format)