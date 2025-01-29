def search_files(search_term, *file_paths):
    print(f"{file_paths = }")
    
    for spam in file_paths: # file_paths is tuple of arguments
        with open(spam) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    print(raw_line.rstrip()) # remove \n

search_files('wombat')
search_files("bird", "../DATA/alice.txt", "../DATA/parrot.txt")

