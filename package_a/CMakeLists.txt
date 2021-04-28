cmake_minimum_required(VERSION 3.18.0)
project(does_not_exist_on_pypi_project_a)
find_package(Python3 COMPONENTS Development.Module REQUIRED)

include(GNUInstallDirs)

Python3_add_library (pytestmodule MODULE WITH_SOABI src/example_project/application_a/pytestmodule.c)

install(
    TARGETS pytestmodule
    LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}
    RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX})

