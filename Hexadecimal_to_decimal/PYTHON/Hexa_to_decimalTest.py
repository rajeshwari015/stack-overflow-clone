from Hexa_to_decimal import HexadecimalToDecimal

class HexadecimalToDecimalTest:

    def test(self, input_hex, expected_decimal):
        converter = HexadecimalToDecimal()
        result = converter.hexadecimalToDecimal(input_hex)
        return result == expected_decimal


# Example Usage
if __name__ == "__main__":
    # Test cases for hexadecimal to decimal conversion
    test_cases = [
        {"input": "1A", "expected_output": 26},
        {"input": "F", "expected_output": 15},
        {"input": "3D", "expected_output": 61},
        {"input": "B", "expected_output": 11},
        {"input": "9", "expected_output": 9}
    ]

    # Creating an instance of the HexadecimalToDecimalTest class
    tester = HexadecimalToDecimalTest()

    # Running the test cases
    for test_case in test_cases:
        input_hex = test_case["input"]
        expected_decimal = test_case["expected_output"]
        test_result = tester.test(input_hex, expected_decimal)

        if test_result:
            print(f"Test Passed for input '{input_hex}'. Decimal value: {expected_decimal}")
        else:
            print(f"Test Failed for input '{input_hex}'. Expected: {expected_decimal}")
