import subprocess


def main():
    while True:
        command = input('shell> ')
        if command.lower() == 'exit':
            break
        try:
            # Parse the command and its arguments
            args = command.split()

            # Check for input/output redirection
            stdin = None
            stdout = None
            if '>' in args:
                idx = args.index('>')
                output_file = args[idx + 1]
                args = args[:idx]
                stdout = open(output_file, 'w')
            if '<' in args:
                idx = args.index('<')
                input_file = args[idx + 1]
                args = args[:idx]
                stdin = open(input_file, 'r')

            # Execute the command
            process = subprocess.Popen(args, stdin=stdin, stdout=stdout)
            process.communicate()

            # Close any open files
            if stdin is not None:
                stdin.close()
            if stdout is not None:
                stdout.close()

        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()
