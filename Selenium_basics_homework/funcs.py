
def extract_from_file(filename='config.txt', str_number=1):
    with open(filename, 'r') as f:
        counter = 0
        for line in f:
            counter = counter + 1
            if counter == str_number:
                return line.removesuffix('\n')
        raise
