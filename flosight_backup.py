import subprocess
import sys
import datetime
import os, pdb

current_time = datetime.datetime.now() 
backup_directory = f"{os.getcwd()}/backups/flosight/"

def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s'%(name,format), destination)

os.chdir(os.getcwd())
# Get list of all files only in the given directory
pdb.set_trace()
list_of_files = filter( lambda x: os.path.isfile(os.path.join(backup_directory, x)),os.listdir(backup_directory))

# Sort list of files based on last modification time in ascending order
list_of_files = sorted( list_of_files, key = lambda x: os.path.getmtime(os.path.join(backup_directory, x)))
print(list_of_files)


#result = subprocess.run([sys.executable, "-c", f"sudo docker cp c640f68b91be:/data/ /home/production/deployed/automated-backup-scripts/backups/flosight/flosight-backup-{current_time.year}-{current_time.month}-{current_time.day}-{current_time.hour}-{current_time.minute}-{current_time.second}"], capture_output=True, text=True)
#result = subprocess.check_output(f"sudo docker cp c640f68b91be:/data/ /home/production/deployed/automated-backup-scripts/backups/flosight/flosight-backup-{current_time.year}-{current_time.month}-{current_time.day}-{current_time.hour}-{current_time.minute}-{current_time.second}", stderr=subprocess.STDOUT, shell=True)
pdb.set_trace() 
print("stdout:", result.stdout)
print("stderr:", result.stderr)