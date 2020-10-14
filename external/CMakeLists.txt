
if(TARGET_BUILD)
    SET(gtest_disable_pthreads ON CACHE BOOL "Disable pthreads for arm" FORCE)
endif()
SET(INSTALL_GTEST OFF CACHE BOOL "Enable installation of googletest." FORCE)

add_subdirectory(googletest EXCLUDE_FROM_ALL)

if(TARGET_BUILD)
    target_compile_definitions(gtest PUBLIC -DGTEST_HAS_STREAM_REDIRECTION=0)
    target_compile_options(gtest PRIVATE -Wno-psabi -Os -g0)
endif()

target_compile_options(gtest INTERFACE -Wno-sign-compare)

set_target_properties(gtest PROPERTIES CXX_EXTENSIONS ON)
set_target_properties(gmock PROPERTIES CXX_EXTENSIONS ON)
