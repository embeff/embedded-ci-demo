#include <gtest/gtest.h>
#include "SoftwareCrc.h"

class TestSoftwareCrc : public ::testing::Test {
protected:
    demo::SoftwareCrc m_cut;

    uint8_t const SampleData[128] = {0x34,0x7c,0x1b,0x18,0x90,0x80,0xbb,0xc7,0x99,0x2f,0x43,0xb9,0x5e,0xb8,0xb5,0x11,0xe6,0x3f,0xa1,0x34,0x9e,0x16,0x52,0x8f,0x4b,0xa6,0xa7,0x84,0x4c,0x58,0x3d,0x95,0x38,0xd1,0x7c,0x7c,0x1f,0x68,0xdf,0xaa,0xe1,0x1a,0x14,0xb0,0x73,0xde,0xc9,0x4f,0xf1,0x4a,0x36,0x2e,0x0b,0xba,0x09,0xf8,0xcc,0x0c,0xde,0xa1,0xd7,0xb7,0xf2,0x18,0x1c,0x00,0xad,0xc0,0x48,0x81,0x62,0x9f,0x60,0x67,0xfb,0xa7,0x34,0xb7,0x79,0x9d,0x94,0x2d,0x0b,0x8e,0xec,0x22,0xff,0x2e,0xd1,0x98,0xbd,0x6a,0xe4,0x01,0xd2,0x22,0xd2,0x65,0x47,0x7e,0x6d,0x3d,0xf9,0x93,0x84,0xf8,0x81,0x7c,0x00,0x94,0xf8,0x95,0xae,0xe3,0x6b,0xb1,0x33,0xc6,0xdb,0x37,0x7d,0x3a,0xa6,0x2c,0x2c,0xed,0x3c,0x82};

    void SetUp() override {

    }
};

TEST_F(TestSoftwareCrc, ZeroLength_Return0) {
    EXPECT_EQ(m_cut.crc32(SampleData, 0), 0xFFFFFFFFu);
}

TEST_F(TestSoftwareCrc, Length4_ReturPreCalculated) {
    EXPECT_EQ(0x7DF4E402u, m_cut.crc32(SampleData, 4));
}

TEST_F(TestSoftwareCrc, SampleData16Bytes_ReturnPreCalculatedValue) {
    EXPECT_EQ(m_cut.crc32(SampleData, 16), 0x0547A4CCu);
}

TEST_F(TestSoftwareCrc, SampleData15Bytes_ReturnPreCalculatedValue) {
    EXPECT_EQ(m_cut.crc32(SampleData, 15), 0xa7a2ff64u);
}