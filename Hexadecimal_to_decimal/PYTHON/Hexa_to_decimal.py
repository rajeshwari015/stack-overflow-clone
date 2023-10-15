class HexadecimalToDecimal:

    def hexadecimalToDecimal(self, hex_num):
        decimal_num = int(hex_num, 16)
        return decimal_num

    def bubbleSort(self, hex_list):
        n = len(hex_list)

        for i in range(n):
            for j in range(0, n-i-1):
                if self.hexadecimalToDecimal(hex_list[j]) > self.hexadecimalToDecimal(hex_list[j+1]):
                    hex_list[j], hex_list[j+1] = hex_list[j+1], hex_list[j]

        return hex_list


# Example Usage
if __name__ == "__main__":
    # Example list of hexadecimal numbers
    hex_numbers = ["1A", "F", "3D", "B", "9"]

    # Creating an instance of the HexadecimalToDecimal class
    converter = HexadecimalToDecimal()

    # Sorting the list using bubble sort and converting to decimal representation
    sorted_decimal_numbers = converter.bubbleSort(hex_numbers)

    # Printing the sorted decimal numbers
    print("Sorted Decimal Numbers:")
    for num in sorted_decimal_numbers:
        print(converter.hexadecimalToDecimal(num))
