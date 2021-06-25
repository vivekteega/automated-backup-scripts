import shutil
import datetime
import glob,os
import pdb

def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s'%(name,format), destination)
    
# using now() to get current time 
current_time = datetime.datetime.now() 
backup_directory = f"{os.getcwd()}/backups/token-tracking"

os.chdir(os.getcwd())
# Get list of all files only in the given directory
list_of_files = filter( lambda x: os.path.isfile(os.path.join(backup_directory, x)),os.listdir(backup_directory))

# Sort list of files based on last modification time in ascending order
list_of_files = sorted( list_of_files, key = lambda x: os.path.getmtime(os.path.join(backup_directory, x)))
print(list_of_files)
pdb.set_trace()

# Flo Token Tracking 
folder_location = '/home/production/deployed/flo-token-tracking-apiErrorHandling'
#shutil.make_archive(f"flo-token-tracking-backup-{current_time.year}-{current_time.month}-{current_time.day}-{current_time.hour}-{current_time.minute}-{current_time.second}", 'zip', folder_location)
make_archive(folder_location, f"{os.getcwd()}/backups/flo-token-tracking-backup-{current_time.year}-{current_time.month}-{current_time.day}-{current_time.hour}-{current_time.minute}-{current_time.second}.zip")

if len(list_of_files) >= 3:
    os.remove(f"{os.getcwd()}/backups/token-tracking/{list_of_files[0]}")

# Flosight 
