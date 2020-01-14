# About
An external python module for Project Reality that provides optimized implementations of 
Project Reality's realitycore module. The library is meant to compile and work with [BF2CPython](https://github.com/yossizap/BF2-CPython).

The module was initially written as a builtin python module so I was restricted to only 
using ANSI C and having no external dependencies. An upgrade to C++14(w/ pybind) is
planned, contributions are welcome.

# Building
To compile against the BF2 CPython executables and libraries:

## Linux
    mkdir build; cd build
    cmake .. \
        -DPYTHON_LIBRARY=<Path to BF2-CPython>/libpython2.7.so \
        -DPYTHON_INCLUDE_DIR=<Path to BF2-CPython>/Include/ \
        -DPYTHON_EXECUTABLE=<Path to BF2-CPython>/python \
 
## Windows
    
    mkdir build; cd build
    cmake .. \
        -DPYTHON_LIBRARY=<Path to BF2-CPython>/PCBuild/dice_py.lib \
        -DPYTHON_INCLUDE_DIR=<Path to BF2-CPython>/Include/ \
        -DPYTHON_EXECUTABLE=<Path to BF2-CPython>/PCBuild/python.exe \
        -A"Win32" \

Prebuilt BF2CPython binaries can be obtained from [BF2Cpython releases page](https://github.com/yossizap/BF2-CPython/releases).

The module can also be compiled against regular python on both platforms with the
following commands:

    mkdir build; cd build
    cmake ..