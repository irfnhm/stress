# Stress
Send concurrent HTTP/TCP requests to a web server

## Note :warning:
This project is intended to be used only for testing purposes. 
Using these scripts with higher number of request counts could possibly lead to a DoS attack on the target system.
Also, don't use higher number of workers, it will use more CPU power and may freeze your system.

## Requirements
  1. Python - v3 for using python modules
  2. GCC - for using C++ module
  3. golang - for using Go module

## Usage

### Using python module
```bash
$ python stress.py
```

### Using C++ module
```bash
$ g++ stress.cc --std=c++11 -lcurl
$ ./a.out
```

### Using go module
```bash
$ go run stress.go
```
