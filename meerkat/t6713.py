"""Telaire 67xx CO2 sensor I2C Driver for Raspberry PI & MicroPython"""

from pyb import I2C
i2c = I2C(1, I2C.MASTER, baudrate=10000)

# Each portion of command is 16 bits = 2 bytes
# from firmware version tutorial in application note

device_address = 0x15

def combine(msb, lsb):
    return (msb << 8) | (lsb >> 8)

# this works
def firmware_version(verbose=False):
    i2c.send(b'\x04\x13\x89\x00\x01', 0x15)
    r = i2c.recv(4, 0x15)
    # function code, byte count, msb, lsb
    v = combine(r[2], r[3])
    if verbose:
        print('co2 replied:', r)
        print('co2 firmware: v', v)
    return v

def status(verbose=False):
    i2c.send(b'\04\x13\x8a\x00', 0x15)
    r = i2c.recv(4, 0x15)
    # function code, byte count, msb, lsb
    s = combine(r[2], r[3])
    if verbose:
        print('co2 replied:', r)
        print('co2 status:', s)
    return s

def measure(verbose=False):
    i2c.send(b'\x04\x13\x8b\x00\x01', 0x15)
    r = i2c.recv(8, 0x15)
    m = combine(r[2], r[3])
    if verbose:
        print('co2 replied:', r)
        print('co2 status:', m)
    return m
