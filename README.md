# Badgerloop Testing Framework
> Goal: Emulate devices in the solar car

Protocols to emulate:
- [ ] I2C *in progress...*
- [ ] SPI
- [ ] UART
- [ ] CAN

### Test
Compile the i2c testing branch executable then copy to beaglebone

cd into pod-embedded-beta then:
```bash
git checkout BTF
./bloop-dev cross
rsync -a out debian@beaglebone.local:~/pod-embedded-beta/
```
