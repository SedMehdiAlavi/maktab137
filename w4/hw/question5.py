def file_io(input_file, output_file):
    """
    It's triple-function decorator that creates two files named
    at arguments and writes the input of main function into the
    input_file and writes the output of main function
    into output_file.
    """
    def decorator(func):
        def wrapper(args):
            with open(input_file, 'w') as file:
                file.write(args)

            with open(output_file, 'w') as file:
                file.write(func(args))

        return wrapper
    return decorator


@file_io('input.txt', 'output.txt')
def process_data(data):
    """
    It's a simple function that takes an input and returns that
     as upper-cased.
    """
    return data.upper()

print(process_data('hello world'))