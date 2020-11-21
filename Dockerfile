FROM ubuntu:latest

# Update and install packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
	wget \
    ca-certificates \
    git \
    build-essential \
	python3 \
    python3-pip \
    python3-venv \
    python3-wheel \
    ninja-build \
    && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*


# Add arm-none-eabi-gcc
RUN mkdir -p /opt/compilers &&\
    cd /opt/compilers && \
    wget -nv https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2 -O - | tar -xj

# Add cmake
RUN mkdir -p /opt/cmake &&\
    cd /opt/cmake && \
    wget -nv https://github.com/Kitware/CMake/releases/download/v3.18.4/cmake-3.18.4-Linux-x86_64.tar.gz -O - | tar -xz --strip-components=1

ENV PATH="/opt/cmake/bin:/opt/compilers/gcc-arm-none-eabi-9-2020-q2-update/bin:${PATH}"
    