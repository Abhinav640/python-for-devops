# Day 05 - Log Analyzer (Sample File For your Reference)

class LogAnalyzer:


    def __init__(self, log_file, error_code):
        self.log_file = log_file
        self.error_codes = {}
        self.error_code = error_code
        self.error_count = 0
    
    def read_logs(self):
        print(f"Reading log file: {self.log_file}")
        try:
            with open(self.log_file, "r") as file:
                return file.readlines()
        
        except FileNotFoundError:
            return False


    def error_codes_list(self):
        log_data = self.read_logs()

        for line in log_data:
            line = line.strip()
            if line == "".strip():
                continue
            part = line.split(" ", 3)
            if True:
                self.error_codes[part[2]] = self.error_codes.get(part[2], 0) + 1

        return self.error_codes
    
    def error_code_count(self):
        log_data = self.read_logs()

        for line in log_data:
            line = line.strip()
            if line == "".strip():
                continue
            part = line.split(" ", 3)
            if True:
                self.error_codes[part[2]] = self.error_codes.get(part[2], 0) + 1

        return self.error_codes[f"{self.error_code.upper()}"]
   
    def analyze(self):
        log_data = self.read_logs()
        for line in log_data:
            line = line.strip()
            if line == "".strip():
                continue
            part = line.split(" ", 3)
            if part[2] == self.error_code.upper():
                print(f"{self.error_code} : {line}")
                self.error_count += 1

            elif part[2] != self.error_code.upper():
                 continue
            else:
                print(f"There is no {self.error_code} error in the log file.")

        return (f"\nTotal {self.error_code.upper()} errors found: {self.error_count}")

def main():
    """
    Main Function as a single entrypoint to the program
    """
    logs = input("Enter the log file name (e.g., app.log): ")
    analyzer = LogAnalyzer(logs)
    lines = analyzer.read_logs()

    if not lines:
        print("No logs to analyze.")
        return

    result = analyzer.analyze(lines)

    print("Log Analysis Summary:")
    for level, count in result.items():
        print(f"{level}: {count}")


if __name__ == "__main__":
    main()
