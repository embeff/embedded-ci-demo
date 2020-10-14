#include "ICrc.h"

namespace demo {
    class SoftwareCrc : public ICrc {
    public:
        uint32_t crc32(uint8_t const* buffer, size_t len) override {
            const uint32_t POLY = 0x04C11DB7;
            uint32_t crc = -1;

            while( len-- ) {
                crc = crc ^ (*buffer++ << 24);
                for( int bit = 0; bit < 8; bit++ )
                {
                    if( crc & (1L << 31)) crc = (crc << 1) ^ POLY;
                    else                  crc = (crc << 1);
                }
            }
            return crc;
        }
    };
}
