#include "../include/Hex_to_decimal.hpp"
#include <cmath>
#include <cctype>

int HexadecimalToDecimal ::hexToDecimal(std::string hexadecimal) {
    int decimalNumber = 0;
    int position = 0;
    
    // Iterate through the hexadecimal string in reverse order
    for (int i = hexadecimal.length() - 1; i >= 0; --i) {
        char hexDigit = hexadecimal[i];
        int decimalValue;
        
        // Convert character to decimal value
        if (isdigit(hexDigit)) {
            decimalValue = hexDigit - '0';
        } else {
            // Convert uppercase letter to decimal value
            decimalValue = toupper(hexDigit) - 'A' + 10;
        }
        
        // Validate hexadecimal digit
        if (decimalValue < 0 || decimalValue > 15) {
            // Handle invalid input
            // You can throw an exception, return an error code, or handle it as appropriate for your application
        }
        
        // Convert hexadecimal digit to decimal and add it to the result
        decimalNumber += decimalValue * static_cast<int>(pow(16, position));
        ++position;
    }
    
    return decimalNumber;
}
