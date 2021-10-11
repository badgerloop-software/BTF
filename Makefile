CC=g++
CFLAGS=-lpthread -lpigpio -Wall
make: slave.cpp
	$(CC) -o slave slave.cpp $(CFLAGS) 
	sudo ./slave

