import sys
import time
import yaml
import importlib
import serialWrapper

serialWrapper.openSerial()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('You must specify the paths to the configuration files as arguments\n\nUsage: python3 testRunner.py </path/to/testConfig.yml> </path/to/setupConfig.yml>')
        sys.exit(1)
    
    # Veirify that files passed are yaml files (and are in the correct order)
    # TODO Test check
    with open(f'{sys.argv[1]}', 'r') as testFile, open(f'{sys.argv[2]}', 'r') as setupFile:
        testCfg = yaml.safe_load(testFile)
        setupCfg = yaml.safe_load(setupFile)
        if testCfg is None or setupCfg is None or list(setupCfg.keys())[0] != 'setup' or not all(e in list(setupCfg['setup'].keys()) for e in ['target', 'devices', 'drivers']) or list(testCfg.keys())[0] != setupCfg['setup']['target']:
            print('Improperly formatted configuration files')
            sys.exit(1)
        print(testCfg) # REMOVE
        print(setupCfg) # REMOVE
    
	# TODO IMPLEMENT Add serial_basic test check here
	
	# Loop over tests, running each as they are specified by the UUT
    target = setupCfg['setup']['target']
    while True:
        test = serialWrapper.readBytes(10)
        if test[:10] == "START TEST":
            # Get driver and test name from response
            driver, test = test.split()[-1].split('_')
            if testCfg[target][driver].keys().contains(test):
                # Test exists in test config. Import and run test
                module = importlib.import_module(f'{driver}.{test}')
                testClass = getattr(module, test)
                testInstance = testClass()
                testInstance.setup()
                testInstance.run()
                testInstance.teardown()
                testInstance.log() # TODO Record test log & result (compile into results summary table)
            else:
                # TODO Log error because test not found
                pass
        elif test == "END ALL TESTS" or test == "":
            # TODO Update "END ALL TESTS" string
            # Timed out or signalled to end all tests
            break
    
    
    print(f'Start tests in 5')
    for i in range(4):
        time.sleep(1)
        print(f'{4-i}')
    serialWrapper.writeString('Start now')
    time.sleep(1)
    # TODO We should adjust serialWrapper so that it can handle attempting to read an empty buffer. We should also make a readAll() function to read every line in the buffer
    try:
        print(serialWrapper.readBytes())
        print(serialWrapper.readBytes())
    except:
        print('Could not read two lines from Nucleo')
    print('Goodbye World!')
    serialWrapper.closeSerial()
    sys.exit(0)
