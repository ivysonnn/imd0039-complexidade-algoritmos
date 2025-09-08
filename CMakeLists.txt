cmake_minimum_required(VERSION 3.16)

project(algorithms-complexity)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

find_package(Python3 3.11 COMPONENTS Interpreter Development NumPy REQUIRED)

execute_process(
  COMMAND "${Python3_EXECUTABLE}" -c "import sysconfig; import numpy; print(sysconfig.get_path('include'))"
  OUTPUT_VARIABLE NUMPY_INCLUDE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

execute_process(
  COMMAND "${Python3_EXECUTABLE}" -c "import numpy; print(numpy.get_include())"
  OUTPUT_VARIABLE NUMPY_INCLUDE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

add_library(edb INTERFACE)
target_include_directories(edb INTERFACE
  ${PROJECT_SOURCE_DIR}/include/
  ${PROJECT_SOURCE_DIR}/lib/include/
  ${Python3_INCLUDE_DIRS} 
)

set(source_dir "${PROJECT_SOURCE_DIR}")
set(SOURCES 
    ${source_dir}/src/main.cpp
    ${source_dir}/src/binary_search.cpp
    ${source_dir}/src/quicksort.cpp
    ${source_dir}/src/usage.cpp
)

add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE
  ${Python3_INCLUDE_DIRS}
  ${NUMPY_INCLUDE_DIR}
)
target_link_libraries(${PROJECT_NAME} PRIVATE 
    edb
    Python3::Python
)

