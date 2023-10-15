#include "../include/Hex_to_decimal.hpp"
#include "../include/Hex_to_decimalTest.hpp"
#include <iostream>
#include <vector>

bool HexadecimalToDecimalTester::testHexToDecimal(std::string hexadecimal, int expectedDecimal) {
    HexadecimalToDecimal converter;
    int result = converter.hexToDecimal(hexadecimal);
    return result == expectedDecimal;
}