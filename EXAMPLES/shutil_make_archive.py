import shutil
import os

folder = '../DATA'
archive_name = "datafiles"

for archive_type in 'zip', 'gztar':
    shutil.make_archive(archive_name, archive_type, folder)



