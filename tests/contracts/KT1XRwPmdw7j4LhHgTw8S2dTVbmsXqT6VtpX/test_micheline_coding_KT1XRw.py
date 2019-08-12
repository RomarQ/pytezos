from unittest import TestCase

from tests import get_data
from pytezos.michelson.coding import build_schema, encode_micheline, decode_micheline


class MichelineCodingTestKT1XRw(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        code = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/code_KT1XRw.json')
        cls.schema = dict(
            parameter=build_schema(code[0]),
            storage=build_schema(code[1])
        )

    def test_micheline_inverse_storage_KT1XRw(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/storage_KT1XRw.json')
        decoded = decode_micheline(expected, self.schema['storage'])
        actual = encode_micheline(decoded, self.schema['storage'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opAqc9(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opAqc9.json')
        decoded = decode_micheline(expected, self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooZibz(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooZibz.json')
        decoded = decode_micheline(expected, self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_oodMWj(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_oodMWj.json')
        decoded = decode_micheline(expected, self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooVH4y(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooVH4y.json')
        decoded = decode_micheline(expected, self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_opVkzg(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_opVkzg.json')
        decoded = decode_micheline(expected, self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooh2Qs(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooh2Qs.json')
        decoded = decode_micheline(expected, self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)

    def test_micheline_inverse_parameter_ooTejB(self):
        expected = get_data(
            path='contracts/KT1XRwPmdw7j4LhHgTw8S2dTVbmsXqT6VtpX/parameter_ooTejB.json')
        decoded = decode_micheline(expected, self.schema['parameter'])
        actual = encode_micheline(decoded, self.schema['parameter'])
        self.assertEqual(expected, actual)
