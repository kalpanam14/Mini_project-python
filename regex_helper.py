import re

class RegexTool:
    def __init__(self):
        self.source_text = ""
        self.regex_pattern = ""

    def get_user_input(self):
        self.source_text = input("Enter the source text: ")
        self.regex_pattern = input("Enter the regex pattern: ")

    def run_regex(self):
        try:
            matches = re.findall(self.regex_pattern, self.source_text)
            if matches:
                print("Matches found:")
                for match in matches:
                    print(match)
            else:
                print("No matches found.")
        except re.error as e:
            print("Invalid regex pattern. Error:", str(e))