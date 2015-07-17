from xml.etree import ElementTree as ET

from sample.identity.v2.models.base import BaseIdentityModel


class AuthenticateRequest(BaseIdentityModel):
    def __init__(
            self, password_credentials=None, api_key_credentials=None,
            tenant_id=None):
        super(AuthenticateRequest, self).__init__(locals())

    def _obj_to_dict(self):
        dic = {}
        dic["passwordCredentials"] = self._get_sub_model(
            self.password_credentials)
        dic["apiKeyCredentials"] = self._get_sub_model(
            self.api_key_credentials)
        dic["tenantId"] = self.tenant_id
        return {"auth": self._remove_empty_values(dic)}

    def _obj_to_xml_ele(self):
        ele = ET.Element("auth")
        ele.append(self._get_sub_model(self.password_credentials, False))
        ele.append(self._get_sub_model(self.api_key_credentials, False))
        ele.attrib["tenantId"] = self.tenant_id
        return self._remove_empty_values(ele)


class PasswordCredentials(BaseIdentityModel):
    def __init__(self, username=None, password=None):
        super(PasswordCredentials, self).__init__(locals())

    def _obj_to_dict(self):
        dic = {"username": self.username, "password": self.password}
        return self._remove_empty_values(dic)

    def _obj_to_xml_ele(self):
        ele = ET.Element("passwordCredentials")
        ele.attrib["username"] = self.username
        ele.attrib["password"] = self.password
        return self._remove_empty_values(ele)


class APIKeyCredentials(BaseIdentityModel):
    def __init__(self, username=None, api_key=None):
        super(APIKeyCredentials, self).__init__(locals())

    def _obj_to_dict(self):
        dic = {"username": self.username, "apiKey": self.api_key}
        return self._remove_empty_values(dic)

    def _obj_to_xml_ele(self):
        ele = ET.Element("apiKeyCredentials")
        ele.attrib["username"] = self.username
        ele.attrib["apiKey"] = self.api_key
        return self._remove_empty_values(ele)
