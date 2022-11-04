from sys import argv
import billGenerator

def main():

    # check if the input file is provided
    if len(argv) != 2:
        raise Exception("File path not entered")
    
    # open the input file and processing the lines
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    print(billGenerator.billGenerator(lines))   

if __name__ == "__main__":
    main()
