FILE_PATH = "../DATA/ctemps.txt"

with open(FILE_PATH) as ctemps_in:
    for raw_line in ctemps_in:
        c_temp = float(raw_line)
        f_temp = ((9 * c_temp) / 5) + 32
        print(f"{c_temp} C is {f_temp} F")