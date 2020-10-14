#pragma once

#include <cstdint>

namespace demo {

    class ICrc {
    public:
        // Expected standard: CRC-32/MPEG-2 (https://crccalc.com)
        virtual uint32_t crc32(uint8_t const* buffer, size_t len) = 0;
    };
}
