def search_files(search_term, *file_paths):
    for file_path in file_paths: # file_paths is tuple of arguments
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    print(raw_line.rstrip()) # remove \n

search_files("bird", "../DATA/alice.txt", "../DATA/parrot.txt")

