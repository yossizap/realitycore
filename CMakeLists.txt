cmake_minimum_required(VERSION 3.10)
project(realitycore)

set(PYBIND11_CPP_STANDARD -std=c++14)
set(PYBIND11_PYTHON_VERSION 2.7 CACHE STRING "")

add_subdirectory(third_party/pybind11)

# To compile against the BF2 CPython executables:
## Linux
# Add the following args cmake:
# -DPYTHON_LIBRARY=<Path to BF2-CPython>/libpython2.7.so
# -DPYTHON_INCLUDE_DIR=<Path to BF2-CPython>/Include/
# -DPYTHON_EXECUTABLE=<Path to BF2-CPython>/python
#
## Windows
# You have to compile a static 32bit version of the dice_py.dll (See
# github.com/yossizap/CPython for more information) and move it to
# <Path to BF2-CPython>/lib/Python27.lib (Custom PYTHON_LIBRARY name doesn't work with pybind's find)
#
# Add the following args cmake:
# -DPYTHON_LIBRARY=<Path to BF2-CPython>/libpython2.7.lib
# -DPYTHON_INCLUDE_DIR=<Path to BF2-CPython>/Include/ ..
# -DPYTHON_EXECUTABLE=<Path to BF2-CPython>/PCBuild/python.exe
# -A"Win32"
pybind11_add_module(_realitycore
    src/realitycore.cpp
    MODULE
)

# Manually add the include library since pybind doesn't
target_include_directories(_realitycore PUBLIC
    ${PYTHON_INCLUDE_DIR}
)

if (WIN32)
    target_include_directories(_realitycore 
        PUBLIC
        ${PYTHON_INCLUDE_DIR}/../PC
    )

    # Copy test files to the build directory
    add_custom_command(TARGET _realitycore PRE_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy
        ${PYTHON_INCLUDE_DIR}/../PCBuild/dice_py.dll ${PYTHON_INCLUDE_DIR}/../PCBuild/dice_py.lib $<TARGET_FILE_DIR:_realitycore>
    )

    target_link_directories(_realitycore
        PUBLIC
        $<TARGET_FILE_DIR:_realitycore>
    )

    # Replace the python27.dll import that pybind adds into the binary
    add_custom_command(TARGET _realitycore
        POST_BUILD
        COMMAND python ${PROJECT_SOURCE_DIR}/scripts/fix_dll_import.py $<TARGET_FILE_DIR:_realitycore>/_realitycore.pyd
    )
endif (WIN32)

# Copy test files to the build directory
add_custom_command(TARGET _realitycore POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${CMAKE_CURRENT_LIST_DIR}/test $<TARGET_FILE_DIR:_realitycore>
)