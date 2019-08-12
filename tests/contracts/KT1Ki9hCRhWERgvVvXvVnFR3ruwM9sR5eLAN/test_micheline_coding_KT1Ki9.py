from unittest import TestCase

from tests import get_data
from pytezos.michelson.coding import build_schema, encode_micheline, decode_micheline


class MichelineCodingTestKT1Ki9(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        code = get_data(
            path='contracts/KT1Ki9hCRhWERgvVvXvVnFR3ruwM9sR5eLAN/code_KT1Ki9.json')
        cls.schema = dict(
            parameter=build_schema(code[0]),
            storage=build_schema(code[1])
        )

    def test_micheline_inverse_storage_KT1Ki9(self):
        expected = get_data(
            path='contracts/KT1Ki9hCRhWERgvVvXvVnFR3ruwM9sR5eLAN/storage_KT1Ki9.json')
        decoded = decode_micheline(expected, self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)
