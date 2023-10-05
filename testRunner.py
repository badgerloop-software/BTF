import sys
import time
import yaml
import serialWrapper

serialWrapper.openSerial()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('You must specify the paths to the configuration files as arguments\n\nUsage: python3 testRunner.py </path/to/testConfig.yml> </path/to/setupConfig.yml>')
        sys.exit(1)
    # TODO Verify that files passed are yaml files (and are in the correct order)
    
    print("Hello World!")
    for i in range(20):
        if i == 15:
            serialWrapper.writeString("Start now")
            #if i == 16:
            print(serialWrapper.readBytes())
        print(f"{i}")
        time.sleep(1)
    with open(f'{sys.argv[1]}', 'r') as testFile, open(f'{sys.argv[2]}', 'r') as setupFile:
        testCfg = yaml.safe_load(testFile)
        setupCfg = yaml.safe_load(setupFile)
        print(testCfg)
        print(setupCfg)
    print("Goodbye World!")
    serialWrapper.closeSerial()
    sys.exit(0)
