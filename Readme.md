# Continuous Integration Pipeline mit versionierter Toolchain

## Build steps for target build
```
mkdir -p build-target
cd build-target
cmake -G Ninja -DCMAKE_TOOLCHAIN_FILE=cmake/arm_gcc_toolchain.cmake -DBSP_DIR=target_bsp_stm32f407  ..
ninja
```

## Build steps for host build
```
mkdir -p build-host
cd build-host
cmake -G Ninja -DBSP_DIR=target_bsp_stm32f407  ..
ninja
```

## Run tests on-target
```
bash ./ep-cli/ep.sh build-target/src/example_gtest.bin
```

## Run tests off-target
```
./build-target/src/example_gtest[.exe]
```