set(CMSIS_DIR Drivers/CMSIS)

message("Using BSP for STM32F407")
set(DEVICE_NAME "STM32F4xx")
set(STARTUP_FILE "startup_stm32f407xx.s")
set(LINKER_FILE "${CMAKE_CURRENT_SOURCE_DIR}/STM32F407VGTx_FLASH.ld")
set(HAL_PREFIX stm32f4xx_hal)

string(TOLOWER ${DEVICE_NAME} DEVICE_NAME_LOWER)

set(DEVICE_DIR Drivers/CMSIS/Device/ST/${DEVICE_NAME})
set(HAL_DIR Drivers/${DEVICE_NAME}_HAL_Driver)



add_library(target_bsp_stm32f407 STATIC IMPORTED GLOBAL)
set_property(TARGET target_bsp_stm32f407 PROPERTY IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/libtarget_bsp_stm32f407.a)

add_library(target_bsp ALIAS target_bsp_stm32f407)

target_compile_definitions(target_bsp_stm32f407 INTERFACE -DCLOCK_SLOW -DUSE_HAL_DRIVER -DSTM32F407xx)
target_include_directories(target_bsp_stm32f407 INTERFACE include ${DEVICE_DIR}/Include ${CMSIS_DIR}/Include ${HAL_DIR}/Inc)
target_link_libraries(target_bsp_stm32f407 INTERFACE "-Xlinker -Map=output.map -u _printf_float -Wl,-gc-sections -T ${LINKER_FILE}")
