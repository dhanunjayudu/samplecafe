from cafe.engine.models.data_interfaces import ConfigSectionInterface


class IdentityConfig(ConfigSectionInterface):
    SECTION_NAME = "identity"

    @property
    def url(self):
        return self.get_raw("url")

    @property
    def serialize_format(self):
        return self.get("serialize_format", "json")

    @property
    def deserialize_format(self):
        return self.get("deserialize_format", "json")


class UserConfig(ConfigSectionInterface):
    SECTION_NAME = "user"

    @property
    def username(self):
        return self.get_raw("username")

    @property
    def password(self):
        return self.get_raw("password")

    @property
    def apikey(self):
        return self.get("apikey")

