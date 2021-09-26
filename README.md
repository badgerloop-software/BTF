# Badgerloop Testing Framework
> Goal: Emulate devices in the solar car

Protocols to emulate:
- [ ] I2C *in progress...*
- [ ] SPI
- [ ] UART
- [ ] CAN

## Test
Compile the i2c testing branch executable then copy to beaglebone

on your computer, cd into pod-embedded-beta then:
```bash
git checkout BTF
./bloop-dev cross
rsync -a out debian@beaglebone.local:~/pod-embedded-beta/
```
on the pi, cd into BTF then:
```bash
./i2c.py
```
finally, on the beaglebone:
```bash
cd ~/pod-embedded-beta
./out/badgerloop
```
You will see output in the terminal of the raspberry pi as hexadecimal values.

### example:

`main.cpp`
```cpp
...
std::cout << morty.test_write_data(0xFA, 0xCE) << std::endl;
...
```

```
pi@raspberrypi:~ $ ./BTF/i2c.py 
--------------------
status: 18
num bytes read: 2
byte array: face
--------------------
```
