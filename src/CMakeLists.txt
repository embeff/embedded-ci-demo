SET(SOURCES
        ICrc.h
        SoftwareCrc.h
        HardwareCrc.h
        TestSoftwareCrc.cpp
        ViolateCppRuleOfThree.cpp
        )

if(TARGET_BUILD)
    list(APPEND SOURCES "TestHardwareCrc.cpp")
endif()

SET_SOURCE_FILES_PROPERTIES(ViolateCppRuleOfThree.cpp PROPERTIES COMPILE_FLAGS -Wextra)

add_executable(example_gtest ${SOURCES})
target_compile_options(example_gtest PUBLIC "-O2;-g0")
target_include_directories(example_gtest PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

if (TARGET_BUILD)
    # Link whole app library to make certain weak symbols are overwridden
    SET (TARGET_APP_WHOLE -Wl,--whole-archive target_runner_gtest -Wl,--no-whole-archive)
    target_link_libraries(example_gtest target_bsp ${TARGET_APP_WHOLE})
    add_bin_from_elf(example_gtest "example_gtest.bin")
else()
    target_link_libraries(example_gtest gtest_main)
endif()
