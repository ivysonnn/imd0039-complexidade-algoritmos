cmake_minimum_required(VERSION 3.16)

project(algorithms-complexity)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror")

add_library(edb INTERFACE)
target_include_directories(edb INTERFACE
  ${CMAKE_CURRENT_SOURCE_DIR}/src/include/
)

set(source_dir "${PROJECT_SOURCE_DIR}")
set(SOURCES 
    ${source_dir}/src/main.cpp
    ${source_dir}/src/binary_search.cpp
)

add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} PRIVATE edb)

