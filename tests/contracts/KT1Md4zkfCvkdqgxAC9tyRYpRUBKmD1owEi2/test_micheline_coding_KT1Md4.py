from unittest import TestCase

from tests import get_data
from pytezos.michelson.converter import build_schema, decode_micheline, encode_micheline


class MichelineCodingTestKT1Md4(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.code = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/code_KT1Md4.json')
        cls.schema = dict(
            parameter=build_schema(cls.code[0]),
            storage=build_schema(cls.code[1])
        )

    def test_micheline_inverse_storage_KT1Md4(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/storage_KT1Md4.json')
        decoded = decode_micheline(expected, self.code[1], self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oov3xH(self):
        expected = get_data(
            path='contracts/KT1Md4zkfCvkdqgxAC9tyRYpRUBKmD1owEi2/parameter_oov3xH.json')
        decoded = decode_micheline(expected, self.code[0], self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
