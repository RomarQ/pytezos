prim_tags = {
    'parameter': b'\x00',
    'storage': b'\x01',
    'code': b'\x02',
    'False': b'\x03',
    'Elt': b'\x04',
    'Left': b'\x05',
    'None': b'\x06',
    'Pair': b'\x07',
    'Right': b'\x08',
    'Some': b'\x09',
    'True': b'\x0A',
    'Unit': b'\x0B',
    'PACK': b'\x0C',
    'UNPACK': b'\x0D',
    'BLAKE2B': b'\x0E',
    'SHA256': b'\x0F',
    'SHA512': b'\x10',
    'ABS': b'\x11',
    'ADD': b'\x12',
    'AMOUNT': b'\x13',
    'AND': b'\x14',
    'BALANCE': b'\x15',
    'CAR': b'\x16',
    'CDR': b'\x17',
    'CHECK_SIGNATURE': b'\x18',
    'COMPARE': b'\x19',
    'CONCAT': b'\x1A',
    'CONS': b'\x1B',
    '__CREATE_ACCOUNT__': b'\x1C',  # DEPRECATED
    'CREATE_CONTRACT': b'\x1D',
    'IMPLICIT_ACCOUNT': b'\x1E',
    'DIP': b'\x1F',
    'DROP': b'\x20',
    'DUP': b'\x21',
    'EDIV': b'\x22',
    'EMPTY_MAP': b'\x23',
    'EMPTY_SET': b'\x24',
    'EQ': b'\x25',
    'EXEC': b'\x26',
    'FAILWITH': b'\x27',
    'GE': b'\x28',
    'GET': b'\x29',
    'GT': b'\x2A',
    'HASH_KEY': b'\x2B',
    'IF': b'\x2C',
    'IF_CONS': b'\x2D',
    'IF_LEFT': b'\x2E',
    'IF_NONE': b'\x2F',
    'INT': b'\x30',
    'LAMBDA': b'\x31',
    'LE': b'\x32',
    'LEFT': b'\x33',
    'LOOP': b'\x34',
    'LSL': b'\x35',
    'LSR': b'\x36',
    'LT': b'\x37',
    'MAP': b'\x38',
    'MEM': b'\x39',
    'MUL': b'\x3A',
    'NEG': b'\x3B',
    'NEQ': b'\x3C',
    'NIL': b'\x3D',
    'NONE': b'\x3E',
    'NOT': b'\x3F',
    'NOW': b'\x40',
    'OR': b'\x41',
    'PAIR': b'\x42',
    'PUSH': b'\x43',
    'RIGHT': b'\x44',
    'SIZE': b'\x45',
    'SOME': b'\x46',
    'SOURCE': b'\x47',
    'SENDER': b'\x48',
    'SELF': b'\x49',
    'STEPS_TO_QUOTA': b'\x4A',  # DEPRECATED
    'SUB': b'\x4B',
    'SWAP': b'\x4C',
    'TRANSFER_TOKENS': b'\x4D',
    'SET_DELEGATE': b'\x4E',
    'UNIT': b'\x4F',
    'UPDATE': b'\x50',
    'XOR': b'\x51',
    'ITER': b'\x52',
    'LOOP_LEFT': b'\x53',
    'ADDRESS': b'\x54',
    'CONTRACT': b'\x55',
    'ISNAT': b'\x56',
    'CAST': b'\x57',
    'RENAME': b'\x58',
    'bool': b'\x59',
    'contract': b'\x5A',
    'int': b'\x5B',
    'key': b'\x5C',
    'key_hash': b'\x5D',
    'lambda': b'\x5E',
    'list': b'\x5F',
    'map': b'\x60',
    'big_map': b'\x61',
    'nat': b'\x62',
    'option': b'\x63',
    'or': b'\x64',
    'pair': b'\x65',
    'set': b'\x66',
    'signature': b'\x67',
    'string': b'\x68',
    'bytes': b'\x69',
    'mutez': b'\x6A',
    'timestamp': b'\x6B',
    'unit': b'\x6C',
    'operation': b'\x6D',
    'address': b'\x6E',
    'SLICE': b'\x6F',
    'DIG': b'\x70',
    'DUG': b'\x71',
    'EMPTY_BIG_MAP': b'\x72',
    'APPLY': b'\x73',
    'chain_id': b'\x74',
    'CHAIN_ID': b'\x75',
    # EDO
    'LEVEL': b'\x76',
    'SELF_ADDRESS': b'\x77',
    'never': b'\x78',
    'NEVER': b'\x79',
    'UNPAIR': b'\x7A',
    'VOTING_POWER': b'\x7B',
    'TOTAL_VOTING_POWER': b'\x7C',
    'KECCAK': b'\x7D',
    'SHA3': b'\x7E',
    'PAIRING_CHECK': b'\x7F',
    'bls12_381_g1': b'\x80',
    'bls12_381_g2': b'\x81',
    'bls12_381_fr': b'\x82',
    'sapling_state': b'\x83',
    'sapling_transaction_deprecated': b'\x84',
    'SAPLING_EMPTY_STATE': b'\x85',
    'SAPLING_VERIFY_UPDATE': b'\x86',
    'ticket': b'\x87',
    'TICKET': b'\x88',
    'READ_TICKET': b'\x89',
    'SPLIT_TICKET': b'\x8A',
    'JOIN_TICKETS': b'\x8B',
    'GET_AND_UPDATE': b'\x8C',
    # HANGZHOU
    'chest': b'\x8D',
    'chest_key': b'\x8E',
    'OPEN_CHEST': b'\x8F',
    'VIEW': b'\x90',
    'view': b'\x91',
    'constant': b'\x92',
    # ITHACA
    'SUB_MUTEZ': b'\x93',
    # JAKARTA
    'tx_rollup_l2_address': b'\x94',
    'MIN_BLOCK_TIME': b'\x95',
    'sapling_transaction': b'\x96',
    # KATHMANDU
    'EMIT': b'\x97',
    # Lima
    'Lambda_rec': b'\x98',
    'LAMBDA_REC': b'\x99',
    # FIXME: Dummy values for TZT, refactor macros
    'Stack_elt': b'\xEE',
    'Big_map': b'\xEE',
    'input': b'\xEE',
    'output': b'\xEE',
    'sender': b'\xEE',
    'amount': b'\xEE',
    'balance': b'\xEE',
    'self': b'\xEE',
    'now': b'\xEE',
    'source': b'\xEE',
    'big_maps': b'\xEE',
    # FIXME: Dummy values for Jupyter, refactor macros
    'DUMP': b'\xEE',
    'PRINT': b'\xEE',
    'DEBUG': b'\xEE',
    'DROP_ALL': b'\xEE',
    'BEGIN': b'\xEE',
    'COMMIT': b'\xEE',
    'RUN': b'\xEE',
    'EXPAND': b'\xEE',
    'PATCH': b'\xEE',
    'RESET': b'\xEE',
    'BIG_MAP_DIFF': b'\xEE',
}
