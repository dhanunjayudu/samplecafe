from sample.identity.v2.models.base import BaseIdentityModel


class AuthenticateResponse(BaseIdentityModel):
    def __init__(
            self, service_catalog=None, token_model=None, user_model=None):
        super(AuthenticateResponse, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        data = data.get("access")
        return cls(
            service_catalog=cls._build_list_model(
                data, "serviceCatalog", ServiceModel),
            token_model=TokenModel._dict_to_obj(data.get("token")),
            user_model=UserModel._dict_to_obj(data.get("user")))

    @classmethod
    def _xml_ele_to_obj(cls, data):
        return cls(
            service_catalog=cls._build_list_model(
                cls._find(data, "serviceCatalog"), "service", ServiceModel),
            token_model=TokenModel._xml_ele_to_obj(cls._find(data, "token")),
            user_model=UserModel._xml_ele_to_obj(cls._find(data, "user")))


class ServiceModel(BaseIdentityModel):
    def __init__(self, endpoints=None, name=None, type_=None):
        super(ServiceModel, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        return cls(
            endpoints=cls._build_list_model(
                data, "endpoints", EndpointModel),
            name=data.get("name"),
            type_=data.get("type"))

    @classmethod
    def _xml_ele_to_obj(cls, data):
        return cls(
            endpoints=cls._build_list_model(data, "endpoint", EndpointModel),
            name=data.attrib.get("name"),
            type_=data.attrib.get("type"))


class EndpointModel(BaseIdentityModel):
    def __init__(
        self, internal_url=None, public_url=None, tenant_id=None,
            version_id=None, version_info=None, version_list=None):
        super(EndpointModel, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        return cls(
            internal_url=data.get("internalURL"),
            public_url=data.get("publicURL"),
            tenant_id=data.get("tenantId"),
            version_id=data.get("versionId"),
            version_info=data.get("versionInfo"),
            version_list=data.get("versionList"))

    @classmethod
    def _xml_ele_to_obj(cls, data):
        version_element = cls._find(data, "version")
        return cls(
            internal_url=data.attrib.get("internalURL"),
            public_url=data.attrib.get("publicURL"),
            tenant_id=data.attrib.get("tenantId"),
            version_id=version_element.attrib.get("id"),
            version_info=version_element.attrib.get("info"),
            version_list=version_element.attrib.get("list"))


class UserModel(BaseIdentityModel):
    def __init__(
            self, default_region=None, id_=None, name=None, roles_model=None):
        super(UserModel, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        return cls(
            default_region=data.get("RAX-AUTH:defaultRegion"),
            id_=data.get("id"),
            name=data.get("name"),
            roles_model=cls._build_list_model(data, "roles", RoleModel))

    @classmethod
    def _xml_ele_to_obj(cls, data):
        return cls(
            default_region=data.attrib.get("defaultRegion"),
            id_=data.attrib.get("id"),
            name=data.attrib.get("name"),
            roles_model=cls._build_list_model(
                cls._find(data, "roles"), "role", RoleModel))


class RoleModel(BaseIdentityModel):
    def __init__(
        self, description=None, id=None, name=None, tenant_id=None,
            propagate=None):
        super(RoleModel, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        return cls(
            description=data.get("description"),
            id=data.get("id"),
            name=data.get("name"),
            tenant_id=data.get("tenantId"),
            propagate=data.get("rax-auth:propagate"))

    @classmethod
    def _xml_ele_to_obj(cls, data):
        return cls(
            description=data.attrib.get("description"),
            id=data.attrib.get("id"),
            name=data.attrib.get("name"),
            tenant_id=data.attrib.get("tenantId"),
            propagate=data.attrib.get("rax-auth:propagate"))


class TokenModel(BaseIdentityModel):
    def __init__(
        self, expires=None, id_=None, tenant_model=None,
            authenticated_by=None):
        super(TokenModel, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        return cls(
            expires=data.get("expires"),
            id_=data.get("id"),
            tenant_model=TenantModel._dict_to_obj(data.get("tenant")),
            authenticated_by=[x for x in data.get("RAX-AUTH:authenticatedBy")])

    @classmethod
    def _xml_ele_to_obj(cls, data):
        auth_by_ele = cls._find(data, "authenticatedBy")
        return cls(
            expires=data.attrib.get("expires"),
            id_=data.attrib.get("id"),
            tenant_model=TenantModel._dict_to_obj(cls._find(data, "tenant")),
            authenticated_by=[
                x.text for x in list(auth_by_ele) if x.tag == "credential"])


class TenantModel(BaseIdentityModel):
    def __init__(self, id_=None, name=None):
        super(TenantModel, self).__init__(locals())

    @classmethod
    def _dict_to_obj(cls, data):
        return cls(name=data.get("name"), id_=data.get("id"))

    @classmethod
    def _xml_ele_to_obj(cls, data):
        return cls(name=data.attrib.get("name"), id_=data.attrib.get("id"))
