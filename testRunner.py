import sys


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('You must specify the paths to the configuration files as arguments\n\nUsage: python3 testRunner.py </path/to/testConfig.yml> </path/to/setupConfig.yml>')
        sys.exit(1)
    
    print("Hello World!")
    sys.exit(0)
