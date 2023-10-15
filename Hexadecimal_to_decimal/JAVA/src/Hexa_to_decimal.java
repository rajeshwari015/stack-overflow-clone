public class Hexa_to_decimal {
    public int convertToDecimal(String hex) {
        // Convert hexadecimal to decimal
        int decimal = 0;
        int n = hex.length();
        for (int i = 0; i < n; i++) {
            char digit = hex.charAt(i);
            int digitValue;
            if (digit >= '0' && digit <= '9') {
                digitValue = digit - '0';
            } else if (digit >= 'A' && digit <= 'F') {
                digitValue = 10 + (digit - 'A');
            } else if (digit >= 'a' && digit <= 'f') {
                digitValue = 10 + (digit - 'a');
            } else {
                // Invalid hexadecimal digit
                throw new IllegalArgumentException("Invalid hexadecimal digit: " + digit);
            }
            decimal = decimal * 16 + digitValue;
        }
        return decimal;
    }
}
