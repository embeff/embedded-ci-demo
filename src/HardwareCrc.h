#pragma once

#include "ICrc.h"
#include <SFR_Access.h>

namespace demo {
    class HardwareCrc : public ICrc {
    public:
        uint32_t crc32(uint8_t const* buffer, size_t len) override {
            uint32_t const* arr = reinterpret_cast<uint32_t const*>(buffer);
            uint32_t const* const end = arr + (len/4);
            CRC->CR = CRC_CR_RESET;

            while (arr < end) {
                uint32_t val = *arr++;
                CRC->DR = __builtin_bswap32(val);
            }
            return CRC->DR;
        }
    };
}
