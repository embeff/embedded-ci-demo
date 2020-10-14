SET(CMAKE_SYSTEM_NAME Generic)
SET(CMAKE_SYSTEM_PROCESSOR arm)

SET(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

SET(CMAKE_C_COMPILER arm-none-eabi-gcc)
SET(CMAKE_CXX_COMPILER arm-none-eabi-g++)

set(SELECTED_FPU_FLAGS "-mfloat-abi=hard -mfpu=fpv4-sp-d16")

SET(CMAKE_C_FLAGS "-mcpu=cortex-m4 -mthumb -mthumb-interwork -ffunction-sections -fdata-sections -g -fno-common -fmessage-length=0 ${SELECTED_FPU_FLAGS}")
SET(CMAKE_CXX_FLAGS "-mcpu=cortex-m4 -mthumb -mthumb-interwork -ffunction-sections -fdata-sections -g -fno-common -fmessage-length=0 ${SELECTED_FPU_FLAGS}")
SET(CMAKE_EXE_LINKER_FLAGS "--specs=nano.specs --specs=nosys.specs -mcpu=cortex-m4 -mthumb ${SELECTED_FPU_FLAGS}")
