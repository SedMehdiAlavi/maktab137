log_data = """
INFO: starting process...
DEBUG: Connecting to database.
ERROR: Connection timeout.
INFO: Process finished.
ERROR: file not found.
"""

def read_lines(data):
    for line in data.strip().split('\n'):
        yield line

def filter_errors(lines_gen):
    for line in lines_gen:
        if line.startswith('ERROR'):
            yield line

def extract_messages(errors_gen):
    for line in errors_gen:
        yield line[7:]

log_lines = read_lines(log_data)
errors_lines = filter_errors(log_lines)
error_message = extract_messages(errors_lines)


for msg in error_message:
    print(msg)