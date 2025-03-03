import random

def encode(character):
    '''
    Encodes the character to give a byte, which is an 8 character string containing only 1s and 0s.

    Parameters:
    character: a string containing a single character. 

    Returns:
    encoded_character: The character encoded into a bitstream.

    Example:
    For example, encode('a') will return the byte '01100001'. 
    '''

    # format checks
    if type(character) != str:
        raise TypeError('Input for encode function must be a string.')
    if len(character) != 1:
        raise ValueError('Input string for the encode function must contain exactly one character.')
    
    # encoding
    integer = ord(character)
    encoded_character = f'{integer:08b}'
    return encoded_character

def decode(byte):
    '''
    Decodes a byte back to a single character.

    Parameters:
    byte: a string of length 8 containing only 1s and 0s. 

    Returns:
    character: The character representing the decoded byte.

    Example:
    For example, decode('01100001') will return 'a'.
    '''

    # format checks
    if type(byte) != str:
        raise TypeError('Input for the decode function must be a string.')
    if len(byte) != 8:
        raise ValueError('Input string for the decode function must have 8 bits exactly.')
    
    # decoding
    for bit in byte:
        if bit not in '01':
            raise ValueError('Input string for the decode function includes incorrect characters. Can only consist of 1s and 0s.')
    integer = int(byte, 2)
    character = chr(integer)
    return character

def transmit_bitstream(bitstream, BER, seed=None):
    '''
    Simulates the process of transmitting a bitstream through a noisy communications channel.

    Parameters:
    bitstream: a string containing only 1s and 0s. 
    BER (bit error rate): the probability of a bit become incorrect during transmission.
    seed: integer allowing for controlled randomisation. Defaults to None.

    Returns:
    received_bitstream: The bitstream received after transmitting through the communications channel.
    '''

    # format checks
    if type(bitstream) != str:
        raise TypeError('Input for transmit_bitstream function must be a string.')
    if type(BER) not in (int, float):
        raise TypeError('BER must be numeric (integer or float).')
    if BER < 0 or BER > 1:
        raise ValueError('BER must be between 0 and 1 inclusive.')

    # initialisation
    random.seed(seed)
    received_bitstream = ''

    # transmission
    for bit in bitstream:
        # check bit is valid
        if bit not in '01':
            raise ValueError('Input string for the transmit_bitstream function includes incorrect characters. Can only consist of 1s and 0s.')

        # simulate random bit error    
        p = random.random()
        if p <= BER:
            bit = str((int(bit) + 1) % 2) # this expression swaps bits
        received_bitstream += bit

    return received_bitstream