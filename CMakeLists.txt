cmake_minimum_required(VERSION 3.10)

project(_realitycore)

set(CMAKE_C_STANDARD 99)

# To compile against the BF2 CPython executables:
# -DPYTHON_LIBRARY=<>/BF2-CPython/libpython2.7.so  
# -DPYTHON_INCLUDE_DIR=<>/BF2-CPython/Include/ ..
set(PYTHON_VERSION 2.7)
find_package(PythonLibs ${PYTHON_VERSION} REQUIRED)

add_library(_realitycore 
  SHARED 
    src/_realitycore.c
)

set_target_properties(_realitycore
  PROPERTIES
    PREFIX ""
    OUTPUT_NAME "_realitycore"
    LINKER_LANGUAGE C
)

if(WIN32)
    set_target_properties(_realitycore
        PROPERTIES
          SUFFIX ".pyd"
    )
endif()

target_include_directories(_realitycore
  PUBLIC
    ${PYTHON_INCLUDE_DIRS}
)

target_link_libraries(_realitycore
  PRIVATE
    ${PYTHON_LIBRARIES}
)

# Copy test files to the build directory
add_custom_command(TARGET _realitycore POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${CMAKE_CURRENT_LIST_DIR}/test $<TARGET_FILE_DIR:_realitycore>
)

install(TARGETS _realitycore
    LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
)
