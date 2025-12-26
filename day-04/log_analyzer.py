with open("app.log", "r") as file:
    log_data = file.readlines()

error_codes = {}

for line in log_data:
    line = line.strip()
    if line == "".strip():
        continue
    part = line.split(" ", 3)
    if True:
        error_codes[part[2]] = error_codes.get(part[2], 0) + 1

        
error_code = input(f"Enter the error code to search in log file {error_codes}: ")

print(f"Log File Analysis:")

error_count = 0

for line in log_data:
    line = line.strip()
    if line == "".strip():
        continue

    part = line.split(" ", 3)    
    if part[2] == error_code.upper():
        print(f"{error_code} : {line}")
        error_count += 1

    elif part[2] != error_code.upper():
         continue
    else:
            print(f"There is no {error_code} error in the log file.")

print(f"\nTotal {error_code.upper()} errors found: {error_count}")