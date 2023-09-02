import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('You must specify the path to the config file as an argument')
        sys.exit(1)
    

    print(sys.argv[1])
    sys.exit(0)