def main():
    try: infile = open('philosophers.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)
    
    except IOError:
        print ("An error occured trying to open the file.")
        
main()