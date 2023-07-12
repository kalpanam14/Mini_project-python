from regex_helper import RegexTool
class RegexApp:
    def __init__(self):
        self.regex_tool = RegexTool()

    def run(self):
        try:
            self.regex_tool.get_user_input()
            self.regex_tool.run_regex()
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")

if __name__ == '__main__':
    regex_app = RegexApp()
    regex_app.run()