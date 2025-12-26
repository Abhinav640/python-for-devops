from log_analyzer_class import LogAnalyzer

info_code = LogAnalyzer("app.log", "INFO")
error_code = LogAnalyzer("app.log", "ERROR")

logfile_status = info_code.read_logs()
# info_error_count = info_code.error_code_count()
if logfile_status == False:
    print("No logs to analyze.")
else:
    info_result = info_code.analyze()
    print("Log Analysis Summary for INFO:")
    print(info_result)

    error_result = error_code.analyze()
    print("\nLog Analysis Summary for ERROR:")
    print(error_result)

