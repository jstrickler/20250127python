def search_files(search_term, *file_paths, ignore_case=False):
    for file_path in file_paths: # file_paths is tuple of arguments
        if ignore_case:
            search_term = search_term.lower()

        with open(file_path) as file_in:
            for raw_line in file_in:
                if ignore_case:
                    search_line = raw_line.lower()
                else:
                    search_line = raw_line

                if search_term in search_line:
                    print(raw_line.rstrip()) # remove \n

search_files("lizard", "../DATA/alice.txt", "../DATA/words.txt", ignore_case=True)
print()

def format_time(*, hour, minute):  # no parameters
    suffix = "AM" if hour < 12 else "PM"
    hour = hour % 12  #  AM/PM time
    return f"{hour:02d}:{minute:02d} {suffix}"

print(f"{format_time(hour=11, minute=40) = }")
print(f"{format_time(minute=40, hour=11) = }")
print(f"{format_time(hour=14, minute=1) = }")



