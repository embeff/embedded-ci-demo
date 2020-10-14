add_library(target_runner_gtest STATIC IMPORTED GLOBAL)
set_property(TARGET target_runner_gtest PROPERTY IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/libtarget_runner_gtest.a)
target_compile_options(target_runner_gtest INTERFACE "-Os")
target_link_libraries(target_runner_gtest INTERFACE gtest gmock target_bsp)