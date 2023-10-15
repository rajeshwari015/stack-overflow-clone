import json
import os
from Hexa_to_decimalTest import HexadecimalToDecimalTest

class Util:
    def __init__(self):
        self.config = self.readConfig()
        self.testcases = self.readTestcases()

    def readConfig(self):
        with open(os.path.join(os.path.dirname(__file__), "../conf/config.json"), "r") as configFile:
            configJson = json.load(configFile)
        return configJson

    def readTestcases(self):
        testcaseFile = os.path.join(os.path.dirname(__file__), "../Resources/testcases.json")
        with open(testcaseFile, "r") as testcases:
            testcasesJson = json.load(testcases)
        return testcasesJson

    def writeTestCases(self, testcases):
        output_file_path = os.path.join(os.path.dirname(__file__), "../Resources/python_result.json")
        with open(output_file_path, "w") as resultFile:
            json.dump(testcases, resultFile, indent=4)

def main():
    util = Util()
    testcasesJson = util.testcases
    failures = []

   
    for index, testcase in enumerate(testcasesJson, start=1):
        tester = HexadecimalToDecimalTest()
        input_hex_list = testcase["input"]
        input_hex = ''.join(input_hex_list)
        expected_decimal = testcase["output"]
        res = tester.test(input_hex, expected_decimal)
        testcase["result"] = res

        if not res:
            failures.append(f"Testcase {index} failed: Input: {input_hex}, Expected: {expected_decimal}")

    util.writeTestCases(testcasesJson)

    if failures:
        print("Some Testcases failed:")
        for failure in failures:
            print(failure)
        raise Exception("Testcase(s) failed")
    else:
        print("All Testcases passed successfully.")

if __name__ == "__main__":
    main()
