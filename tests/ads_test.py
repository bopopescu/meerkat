import smbus
from meerkat import ads
from time import sleep

i2c = smbus.SMBus(1)
dev = ads.ADS1115(bus=i2c)

print('Set Bus Pointer Test')
# test setting pointer register
dev.set_pointer('conversion')  # W 0x48, 0x00
# bus delay = 0.1807 ms
dev.set_pointer('config')      # W 0x48, 0x01
# bus delay = 0.1132 ms
dev.set_pointer('lo_thresh')    # W 0x48, 0x02
# bus delay = 0.1148 ms
dev.set_pointer('hi_thresh')   # W 0x48, 0x03
print('Done!')
print('-'*10)

print('Read 16 bit Registers')
dev.read_register_16bit('conversion')  # W 0x48 0x00
# bus delay = 10 us
# R 0x48 0xNN 0xMM
# bus delay = 0.1817 ms
dev.read_register_16bit('config')      # W 0x48 0x01
# bus delay = 10 us
# R 0x48 0xNN 0xMM
# bus delay = 0.1327 ms
dev.read_register_16bit('lo_thresh')  # W 0x48 0x02
# bus delay = 10 us
# R 0x48 0xNN 0xMM
# bus delay = 0.1197 ms
dev.read_register_16bit('hi_thresh')  # W 0x48 0x03
# bus delay = 10 us
# R 0x48 0xNN 0xMM
# total time: 2.36 ms
print('Done!')
print('-'*10)

print('Get & Set Config Register')
# this seems to work in Saleae Logic...
dev.get_config()
print(bin(dev.config_value))
dev.set_config()
sleep(0.1)  # a little delay to make sure write is done
dev.get_config()
print(bin(dev.config_value))
print('Done!')
print('-'*10)

### Write Test OLD

import smbus
from time import sleep

from meerkat import ads

i2c = smbus.SMBus(1)
dev = ads.ADS1115(bus=i2c)
# this seems to work in Saleae Logic...
dev.get_config()
print(bin(dev.config_value))
dev.set_config()
sleep(0.1)  # a little delay to make sure write is done
dev.get_config()
print(bin(dev.config_value))
sleep(0.1)  # a little delay to make sure write is done
dev.pga('6.144')
sleep(0.1)
dev.get_config()
print(bin(dev.config_value))
sleep(0.1)  # a little delay to make sure write is done
dev.pga('4.096')
sleep(0.1)
dev.get_config()
print(bin(dev.config_value))
sleep(0.1)  # a little delay to make sure write is done
dev.pga('2.048')
sleep(0.1)
dev.get_config()
print(bin(dev.config_value))
sleep(0.1)  # a little delay to make sure write is done
dev.pga('1.024')
sleep(0.1)
dev.get_config()
print(bin(dev.config_value))
sleep(0.1)  # a little delay to make sure write is done
dev.pga('0.512')
sleep(0.1)
dev.get_config()
print(bin(dev.config_value))
sleep(0.1)  # a little delay to make sure write is done
dev.pga('0.256')
sleep(0.1)
dev.get_config()
print(bin(dev.config_value))