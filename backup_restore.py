import subprocess
import os
from datetime import datetime

def backup_database(host, user, password, database, backup_dir):
    try:
        # Create a backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Normalize the backup directory path to use forward slashes
        backup_dir = os.path.normpath(backup_dir)

        # Create a timestamp for the backup filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file = os.path.join(backup_dir, f"{database}_backup_{timestamp}.sql")

        # Ensure backup_file uses forward slashes
        backup_file = backup_file.replace("\\", "/")

        # Construct the mysqldump command
        dump_cmd = f'mysqldump -h {host} -u {user} -p{password} {database} > {backup_file}'

        # Print for debugging
        #print(f"Backup directory: {backup_dir}")
        #print(f"Backup file: {backup_file}")
        #print(f"Dump command: {dump_cmd}")

        # Execute the mysqldump command
        subprocess.run(dump_cmd, shell=True, check=True)
        print(f"Backup successful! Backup file created at: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")

def restore_database(host, user, password, database, backup_file):
    try:
        # Construct the mysql command
        restore_cmd = f"mysql -h {host} -u {user} -p{password} {database} < {backup_file}"

        # Execute the mysql command
        subprocess.run(restore_cmd, shell=True, check=True)
        print(f"Restore successful! Database {database} restored from: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during restore: {e}")

# Replace with your MySQL credentials and desired backup directory
host = 'localhost'
user = 'root'
password = '030709'
database = 'mansys'
backup_dir = '/Users/luian/Downloads'
backup_file = 'C:/Users/luian/Downloads/mansys_backup_20240625144451.sql'
#C:\Users\deini\OneDrive\Desktop\New folder
# Uncomment the following lines to perform backup or restore
#backup_database(host, user, password, database, backup_dir)
#restore_database(host, user, password, database, backup_file)
