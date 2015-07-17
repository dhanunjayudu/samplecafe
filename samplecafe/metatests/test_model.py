import unittest

from sample.identity.v2.models import responses


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()
        cls.access_json = """{
    "access": {
        "serviceCatalog": [
            {
                "endpoints": [
                    {
                        "publicURL": "testval1",
                        "region": "testval2",
                        "tenantId": "testval3"
                    },
                    {
                        "publicURL": "testval4",
                        "region": "testval5",
                        "tenantId": "testval6"
                    }
                ],
                "name": "cloudFeeds",
                "type": "rax:feeds"
            },
            {
                "endpoints": [
                    {
                        "internalURL": "https://snet-storage.stg.swift.racklabs.com/v1/StagingUK_17f3718b-c0cf-404f-b21e-e1e08f4f8a1a",
                        "publicURL": "https://storage.stg.swift.racklabs.com/v1/StagingUK_17f3718b-c0cf-404f-b21e-e1e08f4f8a1a",
                        "region": "STAGING",
                        "tenantId": "StagingUK_17f3718b-c0cf-404f-b21e-e1e08f4f8a1a"
                    }
                ],
                "name": "testval7",
                "type": "object-store"
            }
        ],
        "token": {
            "RAX-AUTH:authenticatedBy": ["PASSWORD"],
            "expires": "asdf",
            "id": "asdf",
            "tenant": {
                "id": "-16",
                "name": "-16"
            }
        },
        "user": {
            "RAX-AUTH:defaultRegion": "LON",
            "id": "173189",
            "name": "auth",
            "roles": [
                {
                    "description": "A Role that allows a user access to keystone Service methods",
                    "id": "684",
                    "name": "compute:default",
                    "tenantId": "-16"
                },
                {
                    "description": "A Role that allows a user access to keystone Service methods",
                    "id": "5",
                    "name": "object-store:default",
                    "tenantId": "StagingUK_17f3718b-c0cf-404f-b21e-e1e08f4f8a1a"
                }
            ]
        }
    }
}"""
        cls.access_xml = """
<access xmlns="http://docs.openstack.org/identity/api/v2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:ns7="http://docs.rackspace.com/identity/api/ext/RAX-KSGRP/v1.0" xmlns:os-ksadm="http://docs.openstack.org/identity/api/ext/OS-KSADM/v1.0" xmlns:os-ksec2="http://docs.openstack.org/identity/api/ext/OS-KSEC2/v1.0" xmlns:rax-auth="http://docs.rackspace.com/identity/api/ext/RAX-AUTH/v1.0" xmlns:rax-kskey="http://docs.rackspace.com/identity/api/ext/RAX-KSKEY/v1.0" xmlns:rax-ksqa="http://docs.rackspace.com/identity/api/ext/RAX-KSQA/v1.0">
    <token expires="asdf" id="asdf">
        <tenant id="-16" name="-16"/>
        <rax-auth:authenticatedBy>
            <rax-auth:credential>PASSWORD</rax-auth:credential>
        </rax-auth:authenticatedBy>
    </token>
    <user id="173189" name="auth" rax-auth:defaultRegion="LON">
        <roles>
            <role description="A Role that allows a user access to keystone Service methods" id="684" name="compute:default" rax-auth:propagate="true" tenantId="-16"/>
            <role description="A Role that allows a user access to keystone Service methods" id="5" name="object-store:default" rax-auth:propagate="true" tenantId="StagingUK_17f3718b-c0cf-404f-b21e-e1e08f4f8a1a"/>
        </roles>
    </user>
    <serviceCatalog>
        <service name="cloudFeeds" type="rax:feeds">
            <endpoint publicURL="testval1" region="testval2" tenantId="testval3"/>
            <endpoint publicURL="testval4" region="testval5" tenantId="testval6"/>
        </service>
        <service name="testval7" type="object-store">
            <endpoint internalURL="https://snet-storage.stg.swift.racklabs.com/v1/StagingUK_17f3718b-c0cf-404f-b21e-e1e08f4f8a1a" publicURL="https://storage.stg.swift.racklabs.com/v1/StagingUK_17f3718b-c0cf-404f-b21e-e1e08f4f8a1a" region="STAGING" tenantId="StagingUK_17f3718b-c0cf-404f-b21e-e1e08f4f8a1a"/>
        </service>
    </serviceCatalog>
</access>""".strip()


class TestReponse(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestReponse, cls).setUpClass()
        cls.access_json_model = responses.AuthenticateResponse._json_to_obj(
            cls.access_json)
        cls.access_xml_model = responses.AuthenticateResponse._xml_to_obj(
            cls.access_xml)

    def test_model_equivalence(self):
        assert self.access_xml_model == self.access_json_model
