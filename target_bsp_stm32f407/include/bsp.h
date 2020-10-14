#pragma once

#ifdef __cplusplus
  #include <cstdint>
  extern "C" {
#endif

    #include <stdint.h>
    void ep_output_char(char c, uint8_t portNo);
    void ep_output(char const* s, uint8_t portNo);
    void ep_internal_reset_cache();
    void ep_internal_dwt_init();

#ifdef __cplusplus
};
#endif

