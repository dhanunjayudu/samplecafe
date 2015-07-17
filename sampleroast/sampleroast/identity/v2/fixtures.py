from cafe.drivers.unittest.fixtures import BaseTestFixture
from cafe.drivers.unittest.datasets import DatasetList, DatasetListCombiner
from cafe.drivers.unittest.decorators import (
    DataDrivenClass, data_driven_test, DataDrivenFixture)


from sample.identity.composites import IdentityComposite
from sample.identity.config import UserConfig


class SerializeDataset(DatasetList):
    def __init__(self):
        self.append_new_dataset("ser_json", {"ser_type": "json"}, tags=["ser_json"])
        self.append_new_dataset("ser_xml", {"ser_type": "xml"}, tags=["ser_xml"])


class DeserializeDataset(DatasetList):
    def __init__(self):
        self.append_new_dataset("des_json", {"deser_type": "json"}, tags=["deser_json"])
        self.append_new_dataset("des_xml", {"deser_type": "xml"}, tags=["deser_xml"])


@DataDrivenClass(DatasetListCombiner(SerializeDataset(), DeserializeDataset()))
class IdentityFixture(BaseTestFixture):
    @classmethod
    def setUpClass(cls):
        super(IdentityFixture, cls).setUpClass()
        cls.comp = IdentityComposite()
        cls.user_config = UserConfig()

    def test_status_entity(self):
        self.comp.client.serialize_format = self.ser_type
        self.comp.client.deserialize_format = self.deser_type
        headers = dict(self.comp.client.default_headers.items())
        headers["Content-Type"] = "application/{0}".format(self.ser_type)
        headers["Accept"] = "application/{0}".format(self.deser_type)
        requestslib_kwargs = {"headers": headers}
        r = self.comp.client.authenticate(
            self.user_config.username,
            self.user_config.password,
            self.user_config.apikey, requestslib_kwargs=requestslib_kwargs)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.entity)
